### Integration with Seer

To integrate context caching into the `Seer` class, we can:

1. Add a `cache_id` parameter to the `Seer.run()` method.
2. If a `cache_id` is provided, use `genai.GenerativeModel.from_cached_content()` to create a model that uses the cache.
3. If no `cache_id` is provided, create a new cache or use a default cache.
4. Store the cache id for future use.

### Notes on Context Caching

*   **Caching and Rate Limits:** Context caching does not change the API's rate limits. Cached tokens are still counted towards the token limits.
*   **Caching and Multiprocessing:** When using context caching with multiprocessing, each process will need to manage its own cache. Caches are not shared between processes.
*   **Cache Invalidation:** Cached content is invalidated when the TTL expires or when the cache is manually deleted.
*   **Cache Size:** The maximum size of a cache is determined by the model's maximum input token limit.
*   **Error Handling:** The Gemini API will return an error if you try to use a cache that does not exist or has expired.
*   **Security:** Cached content is stored securely by the Gemini API. However, you should be mindful of the sensitivity of the data you are caching.

