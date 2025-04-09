# Recommended Architecture for Parallel Gemini API Processing

## 1. Introduction

This document outlines a recommended architecture for processing a high volume of tasks involving Google Gemini API calls in parallel, while adhering to the API's multi-dimensional rate limits (RPM, RPD, TPM). The goal is to maximize throughput and scalability.

This architecture is based on the findings from the detailed analysis in "Architecting a Scalable Python Queuing System for Rate-Limited Gemini API Calls".

## 2. Core Architecture: Task Queuing

A task queuing system is essential to decouple task submission from execution and manage parallel processing.

*   **Producer:** The main application enqueues tasks (e.g., requests for Gemini API calls).
*   **Broker:** A message middleware (Redis recommended) holds the queue of tasks.
*   **Workers:** Independent processes consume tasks from the broker and execute them.
*   **Result Backend (Optional):** Stores task results (Redis or other).

## 3. Proposed Stack

*   **Task Queue:** **Dramatiq** is recommended for its balance of simplicity, reliability (ack-on-completion default), and useful features (middleware, locks).
    *   *Alternative:* **Celery** (with eventlet/gevent pool) is a mature option if its extensive ecosystem (Beat, Flower) is required, but adds complexity (monkey-patching).
*   **Broker:** **Redis** is strongly recommended due to its performance and crucial role as the backend for the distributed rate limiter.
*   **Concurrency Model:** **Asyncio** within worker processes is the most efficient model for handling numerous concurrent, I/O-bound Gemini API calls. Use `async def` actors (potentially with `async-dramatiq` extension if needed) or Celery's eventlet/gevent pool.
*   **Distributed Rate Limiter:** A dedicated Python library using **Redis + Lua scripts** for atomic, distributed rate limiting is critical.
    *   *Recommended Libraries:* `redis-rate-limiters` or `self-limiters`.
    *   *Algorithm:* **Token Bucket** is suitable for handling RPM and TPM limits, allowing bursts while controlling the average rate.
    *   *Implementation:* Must handle RPM, RPD, and TPM dimensions atomically within Lua scripts. TPM requires estimating token consumption per call.

## 4. Distributed Rate Limiting Implementation Details

*   **Atomicity:** Using Redis Lua scripts is non-negotiable to prevent race conditions between workers accessing shared limit counters. Libraries like `redis-rate-limiters` encapsulate this.
*   **Multi-Limit Handling:** A single Lua script should ideally check and update all relevant limits (RPM, RPD, TPM) atomically before allowing a request. Distinct Redis keys should track the state for each dimension (e.g., `project:X:rpm_tokens`, `project:X:tpm_tokens`, `project:X:rpd_count`).
*   **TPM Challenge:** Since output tokens are unknown beforehand, the TPM limiter must operate on estimated total tokens (input + estimated output) consumed atomically before the call. Input tokens can be estimated (heuristics) or determined via `count_tokens` (adds latency). Relying on the API client's internal retries is essential if the TPM estimate is slightly off, leading to an occasional 429.
*   **Coordination:** Workers acquire permits from the limiter before each API call. The limiter (via Redis Lua script) grants or denies access based on the shared state. Async-compatible limiters (`async with limiter.acquire(...)`) prevent blocking the worker's event loop while waiting.

## 5. Resilience

*   **API Client Retries:** Rely on the built-in retry mechanisms within the Google Gemini Python client (`google-generativeai`) or the underlying `google-api-python-client` / `google-auth` libraries. These libraries typically handle transient network errors and standard retryable HTTP codes (like 429, 500, 503) with exponential backoff. Ensure the client is configured appropriately if defaults need adjustment.
*   **Rate Limiter Timeouts:** The rate limiter itself should have a maximum wait time (`max_sleep` in `redis-rate-limiters`). If a task waits too long for a permit, it should likely be re-queued with a delay rather than failing outright.
*   **Task Queue Retries:** Configure Dramatiq/Celery retries carefully. It might be preferable to disable automatic task retries for API call failures and instead rely on the API client's internal retries, potentially implementing manual re-queueing logic within the task for specific failure scenarios (like rate limiter timeouts).

## 6. Scaling Strategy

*   **Workers:** Scale horizontally by adding more worker instances. The distributed rate limiter ensures coordination.
*   **Intra-Worker Concurrency:** Tune the number of concurrent asyncio tasks (or greenlets) per worker.
*   **Broker/Redis:** Ensure Redis can handle the message and rate-limiting load.
*   **API Quota:** The ultimate bottleneck is the Gemini API quota. Monitor usage and request increases if necessary.

## 7. Conclusion

This architecture (Dramatiq/Celery + Redis + Asyncio + Redis/Lua Rate Limiter) provides a scalable and robust foundation for parallel Gemini API processing. Key success factors are the atomic, distributed rate limiter correctly handling all API dimensions (RPM, RPD, TPM) and leveraging the API client's built-in resilience features. Careful implementation and monitoring are essential.
