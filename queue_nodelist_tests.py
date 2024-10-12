import unittest
from queue_nodelist import *

class TestLab1(unittest.TestCase):

    def test_nodelist(self) -> None:
        q = Queue()
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, None)
        q.enqueue(1)
        self.assertEqual(q.rear, Node(1, None))
        self.assertEqual(q.front, None)
        q.enqueue(2)
        self.assertEqual(q.rear, Node(2, Node(1, None)))
        self.assertEqual(q.dequeue(),1)
        self.assertEqual(q.rear, None)
        self.assertEqual(q.front, Node(2, None))

    def test_get_items(self)->None:
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        q.dequeue()
        q.enqueue(6)
        self.assertEqual([2,3,4,5,6], q.get_items())

    def test_is_empty(self) -> None:
        q = Queue()
        self.assertTrue(q.is_empty())
        q.enqueue(True)
        q.dequeue()
        self.assertTrue(q.is_empty())

    def test_size(self) -> None:
        q = Queue()
        q.enqueue(1)
        q.enqueue("abc")
        q.enqueue(True)
        q.enqueue(None)
        self.assertEqual(q.size(), 4)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.size(), 2)

    def test_both_empty(self) -> None:
        q = Queue()
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_enqueue_some_stuff(self) -> None:
        q = Queue()
        q.enqueue("abc")
        q.dequeue()
        q.enqueue(None)
        q.enqueue(True)
        q.dequeue()
        q.enqueue(1234)
        q.enqueue(5678)
        q.enqueue("def")
        self.assertEqual(q.get_items(), [True, 1234, 5678, "def"])
# WRITE MORE TESTS!

if __name__ == '__main__': 
    unittest.main()
