# NodeList version of ADT Queue
from dataclasses import dataclass
from typing import Union, Any, TypeAlias, List

NodeList: TypeAlias = Union[None, 'Node']

@dataclass
class Node:
    value: Any            # object reference stored in Node
    rest: NodeList        # reference to NodeList

"""Implements an efficient last-in first-out Abstract Data Type using a node list"""
@dataclass
class Queue:

    def __post_init__(self) -> None:
        self.num_items: int = 0             # number of items in stack
        self.rear: NodeList = None          # rear NodeList
        self.front: NodeList = None         # front NodeList

    # get_items returns array (Python list) of items in Queue
    # first item in the list will be front of queue, last item is rear of queue
    def get_items(self) -> List:
        items: List = []
        front = self.front
        while front is not None:
            items.append(front.value)
            front = front.rest
        if self.rear is not None:
            rear_items = []
            rear: NodeList = self.rear
            while rear is not None:
                rear_items.append(rear.value)
                rear = rear.rest
            rear_items.reverse()
            items.extend(rear_items)
        return items

    def is_empty(self) -> bool:
        """Returns true if the queue is empty and false otherwise
        Must be O(1)"""
        return self.num_items == 0

    def enqueue(self, item: Any) -> None:
        """enqueues item, adding it to the rear NodeList
        Must be O(1)"""

        self.rear = Node(item, self.rear)
        self.num_items += 1

    def dequeue(self) -> Any:
        """dequeues item, removing first item from front NodeList
        If front NodeList is empty, remove items from rear NodeList
        and add to front NodeList until rear NodeList is empty
        If front NodeList and rear NodeList are both empty, raise IndexError
        Must be O(1) - general case"""

        if self.front is None and self.rear is None:
            raise IndexError
        if self.front is None:
            while self.rear is not None:
                reartop = self.rear.value
                self.rear = self.rear.rest
                self.front = Node(reartop, self.front)
        deqd = self.front.value
        self.front = self.front.rest
        self.num_items -= 1
        return deqd

    def size(self) -> int:
        """Returns the number of items in the queue
        Must be O(1)"""
        return self.num_items
