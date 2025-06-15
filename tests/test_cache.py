import pytest
import threading
import random
import logging
from main import ThreadedCacheMemoryInterface

class TestMemorySafeCache:
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        capacity = 1000
        self.__class__.cache = ThreadedCacheMemoryInterface(capacity)
        
    @classmethod
    def add_item_in_cache(cls):
        key = random.randint(1, 1000)
        value = random.randint(1, 10)
        ttl = random.randint(1, 100)
        logging.info(f"\n\nAdding Key: {key} and Value: {value} and ttl: {ttl}")
        cls.cache.put(key, value, ttl)
        logging.info(f"\n\nState of Cache after adding key value to cache: {cls.cache.display()}")
    
    @pytest.mark.unitTest
    def test_adding_10_items_in_cache_simultaneously(self):
        background_process_thread = threading.Thread(target=self.cache.remove_expired_nodes_process, daemon=True).start()
        
        threads = []
        for i in range(10):
            t = threading.Thread(target=TestMemorySafeCache.add_item_in_cache)
            threads.append(t)
            t.start()
            
        for t in threads:
            t.join()
        self.cache.disable_remove_expired_nodes()