from datetime import datetime, timedelta
from threading import Lock

class Node:
    def __init__(self, key, value, ttl = None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.created_at = datetime.now()
        self.ttl = ttl
        
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} #Hashmap caching for O(1) retrieval
        self.head = Node(0, 0, None)
        self.tail = Node(0, 0, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lock = Lock()
        
    def __remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def __add(self, node):
        #Head of Node
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev = node
        self.head.next = node
    
    def __is_expired(self, node):
        if node.ttl is None:
            return False
        return datetime.now() > node.created_at + timedelta(seconds = node.ttl)
    
    def remove_expired(self):
        curr = self.head
        while curr != self.tail:
            next_node = curr.next
            if self.__is_expired(curr):
                self.__remove(curr)
            curr = next_node
        
    def get(self, key):
        with self.lock:
            if key in self.cache:
                node = self.cache[key]
                if not self.__is_expired(node):
                    self.__remove(node)
                    self.__add(node)
                    return node.value
                else:
                    self.__remove(node)
                    del self.cache[key]
                    print("Key has expired.")
        return -1
        
    def put(self, key, value, ttl = None):
        self.remove_expired()
        with self.lock:
            if key in self.cache:
                self.__remove(self.cache[key])
            elif len(self.cache) == self.capacity:
                lru = self.tail.prev
                self.__remove(lru)
                del self.cache[lru.key]
            new_node = Node(key, value, ttl)
            self.cache[key] = new_node
            self.__add(new_node)
        
    def display(self):
        with self.lock:
            current = self.head.next
            items = []
            while current != self.tail:
                items.append(f"{current.key}:{current.value}:{current.ttl}")
                # items.append(f"{current.key}:{current.value}:{current.ttl}:{current.created_at}")
                current = current.next
            print("Cache state: ", " <-> ".join(items))
        

if __name__ == "__main__":
    capacity = int(input("Enter the capacity of the LRU Cache: "))
    cache = LRUCache(capacity)
    
    while True:
        print("\nOptions: ")
        print("1. Put (key, value)")
        print("2. Get (key)")
        print("3. Display Cache")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1':
            key = int(input("Enter key: "))
            value = int(input("Enter value: "))
            ttl = input("Enter Expiry Time: ")
            ttl = None if ttl == "" else int(ttl)
            cache.put(key, value, ttl)
            print(f"Added ({key}, {value}) to the cache.")
        elif choice == '2':
            key = int(input("Enter key to retrieve: "))
            value = cache.get(key)
            if value != -1:
                print(f"Retrieved value: {value}")
            else:
                print("Key not found in cache.")
        elif choice == '3':
            cache.display()
        elif choice == '4':
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")
