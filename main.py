import time
import threading
from memory_cache import LRUCache

class ThreadedCacheMemoryInterface(LRUCache):
    remove_expired_worker = True
    
    def __init__(self, capacity):
        super().__init__(capacity)
        
    def interact(self):
        while True:
            print("\nOptions: ")
            print("1. Put (key, value)")
            print("2. Get (key)")
            print("3. Display Cache")
            print("4. Delete Key from Cache")
            print("5. Disable Background Process for removing expired Nodes")
            print("6. Exit")
            
            choice = input("Choose an option: ")
            if choice == '1':
                key = input("Enter key: ")
                value = input("Enter value: ")
                ttl = input("Enter Expiry Time: ")
                ttl = None if ttl == "" else int(ttl)
                self.put(key, value, ttl)
                print(f"Added ({key}, {value}) to the cache.")
            elif choice == '2':
                key = input("Enter key to retrieve: ")
                value = self.get(key)
                if value != -1:
                    print(f"Retrieved value: {value}")
                else:
                    print("Key not found in cache.")
            elif choice == '3':
                self.display()
            elif choice == '4':
                node_to_be_deleted = input("Enter Key to be Deleted: ")
                self.delete(node_to_be_deleted)
                print(f"Key is deleted from Cache")
            elif choice == '5':
                self.disable_remove_expired_nodes()
                print("Sucessfully Disabled Background process to remove expired nodes")
            elif choice == '6':
                print("Exiting.")
                self.disable_remove_expired_nodes()
                break
            else:
                print("Invalid choice. Please try again.")
    
    def remove_expired_nodes_process(self):
        while self.remove_expired_worker:
            time.sleep(5)
            self.remove_expired()
    
    def disable_remove_expired_nodes(self):
        self.remove_expired_worker = False
        
if __name__ == "__main__":
    capacity = int(input("Please mention the Capacity of your LRU Cache ->: "))
    cache_memory = ThreadedCacheMemoryInterface(capacity)
    
    interaction_thread = threading.Thread(target=cache_memory.interact)
    background_process_thread = threading.Thread(target=cache_memory.remove_expired_nodes_process)
    
    background_process_thread.start()
    interaction_thread.start()
    
    background_process_thread.join()
    interaction_thread.join()