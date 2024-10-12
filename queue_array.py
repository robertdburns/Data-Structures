# Queue ADT - circular array implementation
from dataclasses import dataclass
from typing import Any, List

"""Implements an efficient first-in first-out Abstract Data Type using a Python List"""
@dataclass
class Queue:
    capacity: int                           # capacity of queue

    def __post_init__(self) -> None:
        self.items = [None]*self.capacity   # array for queue
        self.num_items = 0                  # number of items in stack
        self.front = 0                      # front index of queue (items removed from front)
        self.rear = 0                       # rear index of queue (items enter at rear)

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self) -> List:
        if self.num_items == 0:
            return []
        if self.front < self.rear:
            return self.items[self.front:self.rear]
        else:
            return self.items[self.front:] + self.items[:self.rear]

    def is_empty(self) -> bool:
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        return self.num_items == 0

    def is_full(self) -> bool:
        """Returns true if the queue is full and false otherwise
        Must be O(1)"""
        return self.capacity == self.num_items

    def enqueue(self, item: Any) -> None:
        """enqueues item, raises IndexError if Queue is full
        Must be O(1)"""
        if self.is_full() == True:
            raise IndexError
        else:
            self.items[self.rear] = item
            self.rear = (self.rear + 1) % self.capacity
            self.num_items += 1

    def dequeue(self) -> Any:
        """dequeues item, raises IndexError is Queue is empty
        Must be O(1)"""
        if self.is_empty() == True:
            raise IndexError
        else:
            value = self.items[self.front]
            self.items[self.front] = None
            self.front = (self.front + 1) % self.capacity
            self.num_items -= 1
            return value

    def size(self) -> int:
       """Returns the number of items in the queue
       Must be O(1)"""
       return self.num_items
