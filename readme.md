# Thread-Safe Cache

A Python implementation of a thread-safe cache system using a doubly linked list and a hash map for efficient operations. This project showcases techniques for maintaining thread safety while providing a caching solution suitable for concurrent environments.

## Features

* **Thread Safety**: Implements locking mechanisms to prevent race conditions in a multi-threaded environment.
* **Efficient Operations**: Uses a doubly linked list for managing access order and a hash map for O(1) lookups.
* **TTL (Time-To-Live) Support**: Automatically invalidates cache entries after a specified duration.
* **Concurrency**: Designed for multiple threads to safely interact with the cache.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ThermalDust095/thread_safe_cache.git
   ```
2. Navigate to the project directory:

   ```bash
   cd thread_safe_cache
   ```
3. Install dependencies (if any). The project requires Python 3.7+.

## Usage

Here's a quick example of how to use the `ThreadSafeCache`:

```python
from thread_safe_cache import LRUCache

# Create a cache with a capacity of 5 and a default TTL of 100 seconds
cache = LRUCache(capacity=5)

# Add items to the cache
cache.put("key1", "value1")
cache.put("key2", "value2")

# Retrieve items from the cache
value = cache.get("key1")  # Returns "value1"

# Check for expiration
cache.put("key3", "value3", ttl=50)  # Custom TTL for this entry

# Remove items
cache.remove("key2")

# Clear the cache
cache.clear()
```

## How It Works

1. **Doubly Linked List**: Maintains the order of access for items. The most recently accessed item is moved to the head of the list.
2. **Hash Map**: Provides O(1) access to the items in the cache.
3. **Locks**: Ensures that operations like `put`, `get`, and `remove` are thread-safe.
4. **TTL**: Each item in the cache has a `created_at` timestamp. Items are invalidated if their TTL expires.

## Modules

* **`node.py`**: Defines the `Node` class for the doubly linked list.
* **`lru_cache.py`**: Contains the main `LRUCache` class with methods for cache operations.
* **`tests/`**: Includes unit tests to verify the functionality and thread safety of the cache.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch:

   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:

   ```bash
   git commit -m "Add a descriptive message"
   ```
4. Push to your branch:

   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to open an issue or contact the repository owner directly.

---

Let me know if you'd like to customize this further!
