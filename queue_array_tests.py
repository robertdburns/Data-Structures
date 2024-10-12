import unittest
from queue_array import Queue

class TestLab1(unittest.TestCase):
    import unittest
    from queue_array import Queue

    def test_array(self) -> None:
        q = Queue(5)
        self.assertEqual(q.items, [None, None, None, None, None])
        self.assertEqual(q.get_items(), [])
        q.enqueue(1)
        self.assertEqual(q.items, [1, None, None, None, None])
        q.enqueue(2)
        self.assertEqual(q.items, [1, 2, None, None, None])

    def test_get_items(self) -> None:
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        self.assertEqual([1, 2, 3], q.get_items())
        q.enqueue(4)
        q.enqueue(5)
        q.dequeue()
        q.enqueue(6)
        self.assertEqual([2, 3, 4, 5, 6], q.get_items())

# WRITE MORE TESTS!

    def test_empty(self) -> None:
        q = Queue(5)
        self.assertEqual(q.is_empty(), True)

    def test_full(self) -> None:
        q = Queue(1)
        q.enqueue("abc")
        self.assertEqual(q.is_full(), True)

    def test_enqueue_full(self) -> None:
        q = Queue(1)
        q.enqueue("abc")
        with self.assertRaises(IndexError):
            q.enqueue("def")

    def test_dequeue_empty(self) -> None:
        q = Queue(1)
        with self.assertRaises(IndexError):
            q.dequeue()

    def test_size(self) -> None:
        q = Queue(5)
        q.enqueue("abc")
        q.enqueue("def")
        q.enqueue(True)
        self.assertEqual(q.size(), 3)

    def test_capacity(self) -> None:
        q = Queue(5)
        self.assertEqual(q.capacity, 5)
        q.enqueue(True)
        q.enqueue("123")
        q.enqueue(123)
        self.assertEqual(q.capacity, 5)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.capacity, 5)
        q.dequeue()
        self.assertEqual(q.capacity, 5)

    def test_enqueue_and_dequeue(self) -> None:
        q = Queue(2)
        q.enqueue("abc")
        q.enqueue("def")
        self.assertEqual(q.num_items, 2)
        self.assertEqual(q.is_full(), True)
        q.dequeue()
        q.dequeue()
        self.assertEqual(q.num_items, 0)
        self.assertEqual(q.is_empty(), True)

    def test_dequeue_return(self) -> None:
        q = Queue(5)
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.enqueue(4)
        q.enqueue(5)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.num_items, 3)


if __name__ == '__main__': 
    unittest.main()
