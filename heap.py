from dataclasses import dataclass
from typing import Any, List

@dataclass
class MinHeap:
    heap_capacity: int = 50          # default capacity of heap is 50

    def __post_init__(self):
        self.heap = [0]*(self.heap_capacity+1)      # index 0 not used for heap
        self.num_items = 0                          # empty heap

    def enqueue(self, item: Any) -> None:
        """inserts 'item' into the heap
        Raises IndexError if there is no room in the heap"""
        if self.num_items == self.capacity():
            raise IndexError
        else:
            self.heap[self.num_items + 1] = item
            self.num_items += 1
            self.perc_up(self.num_items)

    def peek(self) -> Any:
        """returns root of heap (highest priority) without changing the heap
        Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        else:
            return self.heap[1]

    def dequeue(self) -> Any:
        """returns item at root (highest priority) - removes it from the heap and restores the heap property
           Raises IndexError if the heap is empty"""
        if self.is_empty():
            raise IndexError
        else:
            root = self.heap[1]
            replace = self.heap[self.num_items]
            self.heap[1] = replace
            self.heap[self.num_items] = 0
            self.num_items -= 1
            self.perc_down(1)
            return root

    def contents(self) -> List:
        """returns a list of contents of the heap in the order it is stored internal to the heap.
        (This may be useful for in testing your implementation.)
        If heap is empty, returns empty list []"""
        if self.is_empty():
            return []
        else:
            return self.heap[1:self.num_items+1]

    def build_heap(self, alist: List) -> None:
        """Discards the items in the current heap and builds a heap from
        the items in alist using the bottom up method.
        If the capacity of the current heap is less than the number of
        items in alist, the capacity of the heap will be increased to accommodate the items in alist"""
        self.num_items = len(alist)
        if self.heap_capacity >= len(alist):
            for i in range(len(alist)):
                self.heap[i + 1] = alist[i]
        else:
            self.heap = [0] + alist[:]
        i = len(alist) // 2
        while i > 0:
            self.perc_down(i)
            i = i - 1

    def is_empty(self) -> bool:
        """returns True if the heap is empty, false otherwise"""
        return self.num_items == 0

    def is_full(self) -> bool:
        """returns True if the heap is full, false otherwise"""
        return self.num_items == self.capacity()

    def capacity(self) -> int:
        """This is the maximum number of a entries the heap can hold, which is
        1 less than the number of entries that the array allocated to hold the heap can hold"""
        return self.heap_capacity
    
    def size(self) -> int:
        """the actual number of elements in the heap, not the capacity"""
        return self.num_items

    def minChild(self, i):
        if i * 2 + 1 > self.num_items:
            return i * 2
        else:
            if self.heap[i * 2] < self.heap[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_down moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while (i * 2) <= self.num_items:
            mc = self.minChild(i)
            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp
            i = mc

    def perc_up(self,i: int) -> None:
        """where the parameter i is an index in the heap and perc_up moves the element stored
        at that location to its proper place in the heap rearranging elements as it goes."""
        while i // 2 > 0:
            if self.heap[i] < self.heap[i // 2]:
                tmp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = tmp
            i = i // 2

    def heap_sort_ascending(self, alist: List) -> None:
        """perform heap sort on input alist in ascending order
        This method will discard the current contents of the heap, build a new heap using
        the items in alist, and mutate alist to put the items in ascending order"""
        temp_heap = MinHeap()
        temp_heap.build_heap(alist)
        i = len(alist)
        alist.clear()
        while i > 0:
            deq = temp_heap.dequeue()
            alist.append(deq)
            i -= 1


