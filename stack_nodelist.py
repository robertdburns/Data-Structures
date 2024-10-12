from dataclasses import dataclass
from typing import Union, Any, TypeAlias

NodeList: TypeAlias = Union[None, 'Node']

@dataclass
class Node:
    value: Any            # object reference stored in Node
    rest: NodeList        # reference to NodeList

"""Implements an efficient last-in first-out Abstract Data Type using a node list"""
@dataclass
class Stack:
    top: NodeList = None                # top Node of stack or None

    def __post_init__(self) -> None:
        self.num_items: int = 0         # number of items in stack

    def is_empty(self) -> bool:
        """Returns True if the stack is empty, and False otherwise
           MUST have O(1) performance"""
        if self.num_items == 0:
            return True
        else:
            return False

    def push(self, item: Any) -> None:
        """Pushes item on stack.
           MUST have O(1) performance"""
        temp = self.top
        self.top = Node(item, temp)
        self.num_items += 1


    def pop(self) -> Any:
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError
           MUST have O(1) performance"""
        if self.is_empty() is False:
            temp = self.top.value
            Top = self.top.rest
            self.num_items -= 1
            return temp
        else:
            raise IndexError

    def peek(self) -> Any:
        """If stack is not empty, returns next item to be popped (but does not remove the item)
           If stack is empty, raises IndexError
           MUST have O(1) performance"""
        if self.is_empty() is False:
            return self.top.value
        else:
            raise IndexError

    def size(self) -> int:
        """Returns the number of elements currently in the stack, not the capacity
           MUST have O(1) performance"""
        return self.num_items