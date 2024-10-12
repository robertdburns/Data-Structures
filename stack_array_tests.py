import unittest
from stack_array import Stack
        
class TestLab2(unittest.TestCase):

# WRITE TESTS FOR STACK OPERATIONS - PUSH, POP, PEEK, etc.

    def test_is_empty(self) -> None:
        stack = Stack(5)
        self.assertTrue(stack.is_empty())

    def test_is_empty2(self) -> None:
        stack = Stack(5)
        stack.push(None)
        self.assertFalse(stack.is_empty())

    def test_is_full(self) -> None:
        stack = Stack(1)
        stack.push("hello")
        self.assertTrue(stack.is_full())

    def test_is_full_push(self) -> None:
        stack = Stack(1)
        stack.push("hello")
        with self.assertRaises(IndexError):
            stack.push(14)

    def test_is_empty_peek(self) -> None:
        stack = Stack(1)
        stack.push("hello")
        stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()

    def test_is_empty_pop(self) -> None:
        stack = Stack(1)
        stack.push("hello")
        stack.pop()
        with self.assertRaises(IndexError):
            stack.pop()

    def test_peek(self) -> None:
        stack = Stack(5)
        stack.push("hello")
        stack.push(True)
        stack.push(None)
        stack.push(14)
        self.assertTrue(stack.peek(), 14)

    def test_pop(self) -> None:
        stack = Stack(5)
        stack.push("hello")
        stack.pop()
        self.assertEqual(stack.num_items, 0)

    def test_size(self) -> None:
        stack = Stack(5)
        stack.push("1")
        stack.push("hello")
        stack.push(True)
        self.assertEqual(stack.size(), 3)

    def test_pop_value(self) -> None:
        stack = Stack(5)
        stack.push("hello")
        self.assertEqual(stack.pop(), "hello")

if __name__ == '__main__': 
    unittest.main()
