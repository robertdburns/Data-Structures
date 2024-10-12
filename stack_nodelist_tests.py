import unittest
from stack_nodelist import *
        
class TestLab2(unittest.TestCase):

    # WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty(self) -> None:
        stack = Stack()
        self.assertTrue(stack.is_empty())

    def test_push(self) -> None:
        stack = Stack()
        stack.push(14)
        stack.push(True)
        stack.push("abc")
        self.assertEqual(stack, Stack(Node(value='abc', rest=Node(value=True, rest=Node(value=14, rest=None)))))

    def test_pop(self) -> None:
        stack = Stack()
        stack.push(15)
        stack.push("abc")
        stack.pop()
        self.assertEqual(stack.num_items, 1)

    def test_peek(self) -> None:
        stack = Stack()
        stack.push("abc")
        stack.push(True)
        stack.push(None)
        stack.push("def")
        self.assertEqual(stack.peek(), "def")

    def test_peek_empty(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_pop_empty(self) -> None:
        stack = Stack()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_size(self) -> None:
        stack = Stack()
        stack.push("hello")
        stack.push("abc")
        stack.push(None)
        self.assertEqual(stack.size(), 3)

if __name__ == '__main__': 
    unittest.main()
