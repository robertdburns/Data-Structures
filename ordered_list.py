from dataclasses import dataclass
from typing import Any, Union, TypeAlias, List

MaybeInt: TypeAlias = Union[None, int]

@dataclass
class Node:
    item: Any               # object reference stored in Node
    next: 'Node' = None     # type: ignore # reference to next Node
    prev: 'Node' = None     # type: ignore # reference to previous Node

# A doubly-linked ordered list of integers, from lowest (head of list, sentinel.next)
# to highest (tail of list, sentinel.prev)
@dataclass
class OrderedList:

    def __post_init__(self) -> None:
        self.sentinel: Node = Node(None)
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

    def is_empty(self) -> bool:
        """Returns back True if OrderedList is empty"""
        return self.size() == 0

    def add(self, item: Any) -> None:
        """Adds an item to OrderedList, in the proper location based on ordering of items
        from lowest (at head of list) to highest (at tail of list)
        If item is already in list, do not add again (no duplicate items)"""
        current = self.sentinel.next
        while current is not self.sentinel and item > current.item:
            current = current.next
        if item != current.item:
            temp = Node(item)
            temp.next = current
            temp.prev = current.prev
            current.prev.next = temp
            current.prev = temp

    def remove(self, item: Any) -> bool:
        """Removes an item from OrderedList. If item is removed (was in the list) returns True
        If item was not removed (was not in the list) returns False"""
        current = self.sentinel.next
        while current is not self.sentinel and item > current.item:
            current = current.next
        if item == current.item:
            current.prev.next = current.next
            current.next.prev = current.prev
            return True
        else:
            return False

    def index(self, item: Any) -> MaybeInt:
        """Returns index of an item in OrderedList (assuming head of list is index 0).
        If item is not in list, return None"""
        if self.is_empty() is True:
            return None
        idx = 0
        current = self.sentinel.next
        while current is not self.sentinel and item > current.item:
            current = current.next
            idx += 1
        if current.item is None or item < current.item:
            return None
        if item == current.item:
            return idx
        else:
            return None

    def pop(self, index: int) -> Any:
        """Removes and returns item at index (assuming head of list is index 0).
        If index is negative or >= size of list, raises IndexError"""
        if index >= self.size() or index < 0:
            raise IndexError
        else:
            i = 0
            current = self.sentinel.next
            while i < index:
                current = current.next
                i += 1
            ret = current.item
            current.prev.next = current.next
            current.next.prev = current.prev
            return ret

    def search(self, item: Any) -> bool:                                                                                #######################
        """Searches OrderedList for item, returns True if item is in list, False otherwise - USE RECURSION"""
        cur = self.sentinel.next
        return self.search_helper(item, cur)

    def search_helper(self, item, ord_list) -> bool:
        if ord_list == self.sentinel:
            return False
        if ord_list.item == item:
            return True
        return self.search_helper(item, ord_list.next)

    def python_list(self) -> List:
        """Return a Python list representation of OrderedList, from head to tail
        For example, list with integers 1, 2, and 3 would return [1, 2, 3]"""
        py_list = []
        current = self.sentinel.next
        while current is not self.sentinel:
            py_list.append(current.item)
            current = current.next
        return py_list

    def python_list_reversed(self) -> List:
        """Return a Python list representation of OrderedList, from tail to head, USING RECURSION
        For example, list with integers 1, 2, and 3 would return [3, 2, 1]"""
        py_list: List[int] = []
        self.rec_python_list_(self.sentinel.prev, py_list)
        return py_list

    def rec_python_list_(self, node: Node, py_list: List) -> None:
        if node is not self.sentinel:
            py_list.append(node.item)
            self.rec_python_list_(node.prev, py_list)

    def size(self) -> int:
        """Returns number of items in the OrderedList - USE RECURSION"""
        items: List[int] = []
        self.size_helper(self.sentinel.next, items)
        return len(items)

    def size_helper(self, node: Node, items: list) -> None:
        if node is not self.sentinel:
            items.append(node.item)
            self.size_helper(node.next, items)

