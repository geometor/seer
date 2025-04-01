# Multiprocessing Strategy for Parallel Prompt Execution

This document outlines the strategy for using process pools with rate limiting
controls to execute multiple prompts in parallel when interacting with the
Gemini API.

## Motivation

The Gemini API has rate limits that must be respected to avoid errors and ensure
reliable operation. These limits include:

*   **10 Requests Per Minute (RPM):** A limit on the number of API calls that
    can be made within a minute.
*   **4 Million Tokens Per Minute (TPM):** A limit on the number of tokens
    processed by the model per minute.
*   **1,500 Requests Per Day (RPD):** A daily limit on the number of requests.

To efficiently process multiple prompts, we can use Python's `multiprocessing`
module to distribute the workload across multiple processes. However, we must
also implement rate limiting to stay within the API's constraints.

## Strategy

The strategy involves using a process pool with a sleep-based rate limiting
mechanism.

### Process Pool

*   We use `multiprocessing.Pool` to create a pool of worker processes.
*   Each process will execute the `run` method of the `Seer` class, which makes
    a call to the Gemini API.
*   The `apply_async` method is used to submit tasks to the pool, and `get` is
    used to retrieve the results.

### Sleep-Based Rate Limiting

*   To control the request rate, we introduce a `sleep_duration` parameter to
    the `generate_content` method of the `Client` class.
*   Before making an API call, the `generate_content` method will call
    `time.sleep(sleep_duration)`.
*   The `sleep_duration` is calculated based on the desired request rate and the
    number of processes.

### Calculation of Sleep Duration

The sleep duration is calculated as follows:

``` 
sleep_duration = 60 / (10 / num_processes) ```

Where:

*   `sleep_duration` is the time in seconds to sleep before making an API call.
*   `num_processes` is the number of processes in the process pool.
*   10 is the Gemini API's RPM limit.

For example, if we have 4 processes, the sleep duration would be:

``` sleep_duration = 60 / (10 / 4) = 24 seconds ```

This ensures that the combined request rate across all processes does not exceed
10 RPM.

### Implementation

The following code snippets illustrate the implementation of this strategy:

```python # src/geometor/seer/client.py import abc from typing import List,
Callable, Any

class Client(abc.ABC): """Abstract base class for LLM clients."""

    @abc.abstractmethod def generate_content(self, prompt: List[str], tools:
    List[Callable] = None, sleep_duration: float = 0) -> Any: """Generates
    content from the LLM.""" ...

# src/geometor/seer/gemini_client.py import requests import time from typing
import List, Callable, Any

class GeminiClient(Client): """Client for interacting with the Gemini API."""
def __init__(self, model_name: str, instructions_file: str): ...

    def generate_content(self, prompt: List[str], tools: List[Callable] = None,
    sleep_duration: float = 0) -> Any: if sleep_duration > 0:
    time.sleep(sleep_duration) # Make the API call here response =
    requests.post( "https://api.example.com/gemini", json={"prompt": prompt},)
    response.raise_for_status() # You might want to check token usage here if
    the API provides it # response.headers.get("X-Gemini-Token-Usage") return
    response.json()

# src/geometor/seer/seer.py import multiprocessing from typing import List

class Seer: """The Seer class.""" def __init__(self, client): self.client =
client

    def run(self, prompt: str, sleep_duration: float = 0): """Runs a single
    prompt.""" # ... existing logic ...  result =
    self.client.generate_content([prompt], sleep_duration=sleep_duration) # ...
    process result ...  return result

    def run_many_pool(self, prompts: List[str], num_processes: int = 4,
    sleep_duration: float = 0): """Runs multiple prompts in parallel using a
    process pool.""" with multiprocessing.Pool(processes=num_processes) as pool:
    results = [pool.apply_async(self.run, (prompt, sleep_duration)) for prompt
    in prompts] return [res.get() for res in results]

# src/geometor/seer/__main__.py from geometor.seer.app import run from
geometor.seer.seer import Seer from geometor.seer.gemini_client import
GeminiClient

def main(): client = GeminiClient(model_name="gemini-pro",
instructions_file="instructions.txt") seer = Seer(client) prompts = ["prompt 1",
"prompt 2", "prompt 3", "prompt 4", "prompt 5", "prompt 6"] num_processes = 4
sleep_duration = 60 / (10 / num_processes) # Calculate sleep duration results =
seer.run_many_pool(prompts, num_processes=num_processes,
sleep_duration=sleep_duration) print(results)

if __name__ == "__main__": main() ```

## Considerations

*   **Token Limit:** Be mindful of the 4 million TPM limit, especially if you
    are using long prompts or generating long responses.
*   **Error Handling:** Implement robust error handling to catch API errors and
    handle rate limit exceptions.
*   **Backoff Strategy:** If you do hit a rate limit, consider implementing a
    backoff strategy (e.g., exponential backoff) to avoid overwhelming the API.
*   **Dynamic Rate Limiting:** For more advanced scenarios, you could implement
    a dynamic rate limiter that adjusts the sleep duration based on the API's
    response headers or error messages.

## Conclusion

This strategy provides a simple and effective way to use process pools with rate
limiting controls to execute multiple prompts in parallel when interacting with
the Gemini API. By carefully considering the API's rate limits and implementing
the appropriate sleep duration, we can efficiently process multiple prompts
while staying within the API's constraints.
