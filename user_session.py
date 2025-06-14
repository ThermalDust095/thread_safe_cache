import sys
from memory_cache import LRUCache
from main import CacheMemoryInterface  # Import the main class

def user_session(cache_capacity):
    cache_memory = CacheMemoryInterface(cache_capacity)
    cache_memory.interact(user_id=sys.argv[1])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python user_session.py <user_id> <cache_capacity>")
        sys.exit(1)
    user_id = sys.argv[1]
    cache_capacity = int(sys.argv[2])
    user_session(cache_capacity)
