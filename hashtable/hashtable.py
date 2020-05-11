class HashTableEntry:
    """
    Hash Table entry, as a linked list node.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity

    def fnv1(self, key):
        """
        FNV-1 64-bit hash function

        Implement this, and/or DJB2.
        """
        hash = 0x811c9dc5
        fnv_32_prime = 0x01000193
        
        for e in key.encode():
            hash = hash ^ e
            hash = (hash * fnv_32_prime)
        return hash

    def djb2(self, key):
        """
        DJB2 32-bit hash function

        Implement this, and/or FNV-1.
        """
        hash = 5381
        for e in key.encode():
            hash = hash * 33 + e
        return hash & 0xFFFFFFFF

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        #return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        if self.storage[self.hash_index(key)]:
            current = self.storage[self.hash_index(key)]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if(current.next is None):
                    current.next = HashTableEntry(key, value)
                    return
                current = current.next
        else:
            self.storage[self.hash_index(key)] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        if self.storage[self.hash_index(key)].next == None:
            if self.storage[self.hash_index(key)].key == key:
                self.storage[self.hash_index(key)] = None
        else:
            current = self.storage[self.hash_index(key)]
            prev = current
            while current.next and current.key != key:
                prev = current
                current = current.next

            if (current.key == self.storage[self.hash_index(key)].key):
                self.storage[self.hash_index(key)] = current.next
            elif (current.key == key):
                prev.next = current.next

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        if (self.storage[self.hash_index(key)]):
            if(self.storage[self.hash_index(key)].next):
                current = self.storage[self.hash_index(key)]
                while current.key != key:
                    current = current.next
                return current.value
            else:
                return self.storage[self.hash_index(key)].value

        return None

    def resize(self):
        """
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Implement this.
        """
        newHashTable = HashTable(self.capacity*2)
        for i, v in enumerate(self.storage):
            while v:
                newHashTable.put(v.key, v.value)
                v = v.next

        self.capacity = newHashTable.capacity
        self.storage = newHashTable.storage

if __name__ == "__main__":
    ht = HashTable(2)

    ht.put("line_1", "Tiny hash table")
    ht.put("line_2", "Filled beyond capacity")
    ht.put("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.get("line_1"))
    print(ht.get("line_2"))
    print(ht.get("line_3"))

    print("")
