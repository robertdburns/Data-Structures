from dataclasses import dataclass
from typing import Any, Tuple, List

@dataclass
class MyHashTable:
    table_size: int = 11        # default table size is 11

    def __post_init__(self) -> None:
        self.hash_table: List = [[] for _ in range(self.table_size)]  # List of lists implementation
        self.num_items = 0          # No items in hash table at start
        self.num_collisions = 0     # No collisions at start

    def insert(self, key: int, value: Any) -> None:
        """Takes a key, and an item.  Keys are valid Python non-negative integers.
        If key is negative, raise ValueError exception
        The function will insert the key-item pair into the hash table based on the
        hash value of the key mod the table size (hash_value = key % table_size)"""
        if key < 0:
            raise ValueError
        else:
            pos = self.hash_pos(key)
            if self.hash_table[pos] == []:                                  #position is empty, can be inserted, empty np collision
                self.hash_table[pos] = [(key, value)]
                self.num_items += 1
                if self.load_factor() > 1.5:
                    num_new_lists = 2 * (len(self.hash_table)) + 1
                    old_collisions = self.num_collisions
                    temp = self.hash_table
                    self.hash_table = [[] for _ in range(num_new_lists)]
                    for i in range(len(temp)):
                        self.hash_table[i] = temp[i]
                    self.num_collisions = old_collisions

            else:                                                           #position is NOT empty, need to add in seperate chain
                in_hash = [False]
                for i in self.hash_table[pos]:
                    if i[0] == key:
                        in_hash[0] = True

                if in_hash[0] == False:                                     #item is not in hash, can add like normal, call collision
                    self.num_collisions += 1
                    self.hash_table[pos].append((key, value))
                    self.num_items += 1

                elif in_hash[0] == True:
                    for i in self.hash_table[pos]:
                        if i[0] == key:
                            i = (key, value)

    def get_item(self, key: int) -> Any:
        """Takes a key and returns the item from the hash table associated with the key.
        If no key-item pair is associated with the key, the function raises a LookupError exception."""
        pos = self.hash_pos(key)
        for i in self.hash_table[pos]:
            if i[0] == key:                                                 #if the key of the hash in the iteration is the key we are looking for...
                value = i[1]                                                #return its value
                return value

        raise LookupError                                                   #if the key is not in the correct place, raise LookupError

    def remove(self, key: int) -> Tuple[int, Any]:
        """Takes a key, removes the key-item pair from the hash table and returns the key-item pair.
        If no key-item pair is associated with the key, the function raises a LookupError exception.
        (The key-item pair should be returned as a tuple)"""
        pos = self.hash_pos(key)
        for i in self.hash_table[pos]:                                      #iterate over all tuples in the list at current pos
            if i[0] == key:                                                 #if current tuple has the key we are looking for...
                value = i[1]
                self.hash_table[pos].remove(i)                              #removes tuple from the list
                self.num_items -= 1
                return (key, value)                                         #return the item that has been removed

        raise LookupError                                                   #if the iteration completes without returning, raise error

    def load_factor(self) -> float:
        """Returns the current load factor of the hash table"""
        return self.num_items / len(self.hash_table)

    def size(self) -> int:
        """Returns the number of key-item pairs currently stored in the hash table"""
        return self.num_items

    def collisions(self) -> int:
        """Returns the number of collisions that have occurred during insertions into the hash table"""
        return self.num_collisions

    def hash_pos(self, key):
        return key % self.table_size
