import unittest
from heap import *

'''
Consider...
tests for negative integers
tests for strings, other comparable
'''
class TestHeap(unittest.TestCase):
        
    def test_01_peek_and_dequeue_1_item(self) -> None:
        test_heap = MinHeap(10)
        test_heap.enqueue(25)
        self.assertEqual(test_heap.peek(), 25)
        self.assertEqual(test_heap.dequeue(), 25)

    def test_02_dequeue_2_item(self) -> None:
        test_heap = MinHeap(10)
        test_heap.enqueue(25)
        test_heap.enqueue(5)
        self.assertEqual(test_heap.dequeue(), 5)
        self.assertEqual(test_heap.dequeue(), 25)
        test_heap = MinHeap(10)
        test_heap.enqueue(5)
        test_heap.enqueue(25)
        self.assertEqual(test_heap.dequeue(), 5)
        self.assertEqual(test_heap.dequeue(), 25)

    def test_04_enqueue2(self) -> None:
        test_heap = MinHeap(6)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        with self.assertRaises(IndexError):
            test_heap.enqueue(10)

    def test_06_find_min1(self) -> None:
        test_heap = MinHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        test_heap.enqueue(10)
        self.assertEqual(test_heap.dequeue(), 2)
        self.assertEqual(test_heap.dequeue(), 5)

    def test_07_find_min3(self) -> None:
        test_heap = MinHeap()
        with self.assertRaises(IndexError):
            test_heap.dequeue()
        self.assertEqual(test_heap.size(),0)
        with self.assertRaises(IndexError):
            test_heap.peek()

    def test_08_del_min1(self) -> None:
        test_heap = MinHeap()
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.dequeue(), 2)
        self.assertEqual(test_heap.size(), 5)
        self.assertEqual(test_heap.contents(), [5, 6, 7, 8, 9])

    def test_10_heap_contents1(self) -> None:
        test_heap = MinHeap(8)
        test_heap.build_heap([3, 2, 1])
        self.assertEqual(test_heap.contents(), [1, 2, 3])

    def test_12_build_heap1(self) -> None:
        test_heap = MinHeap(8)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.contents(), [2, 5, 7, 6, 9, 8])

    def test_14_build_heap3(self) -> None:
        test_heap = MinHeap()
        test_heap.build_heap([3, 4, 5, 6, 7, 10, 8, 1, 2])
        self.assertEqual(test_heap.contents(), [1, 2, 5, 3, 7, 10, 8, 6, 4])

    def test_15_is_empty1(self) -> None:
        test_heap = MinHeap(5)
        self.assertTrue(test_heap.is_empty())
        test_heap.enqueue(10)
        self.assertFalse(test_heap.is_empty())
        test_heap.dequeue()
        self.assertTrue(test_heap.is_empty())        

    def test_16_is_full1(self) -> None:
        test_heap = MinHeap(5)
        test_heap.build_heap([1, 2, 3, 4, 5])
        self.assertTrue(test_heap.is_full())
        test_heap.dequeue()
        self.assertFalse(test_heap.is_full())
        test_heap.enqueue(10)
        self.assertTrue(test_heap.is_full())

    def test_17_get_heap_cap1(self) -> None:
        test_heap = MinHeap(7)
        self.assertEqual(test_heap.capacity(), 7)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.capacity(), 7)
        test_heap.enqueue(10)
        self.assertEqual(test_heap.capacity(), 7)
        test_heap = MinHeap()
        self.assertEqual(test_heap.capacity(), 50)

    def test_18_get_heap_size1(self) -> None:
        test_heap = MinHeap()
        self.assertEqual(test_heap.size(), 0)
        test_heap.build_heap([2, 9, 7, 6, 5, 8])
        self.assertEqual(test_heap.size(), 6)
        test_heap.enqueue(10)
        self.assertEqual(test_heap.size(), 7)

    def test_20_heap_sort_increase1(self) -> None:
        test_heap = MinHeap()
        list1 = [2, 9, 7, 6, 5, 8]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [2, 5, 6, 7, 8, 9])

    def test_01_extra(self) -> None:
        test_heap = MinHeap()
        list1 = [9, 3, 6, 8, 1, 6, 5, 1]
        test_heap.heap_sort_ascending(list1)
        self.assertEqual(list1, [1, 1, 3, 5, 6, 6, 8, 9])
        self.assertEqual(test_heap.size(), 0)
        test_heap.build_heap(list1)
        self.assertEqual(test_heap.size(), 8)
        test_heap.dequeue()
        self.assertEqual(test_heap.size(), 7)
        test_heap.enqueue(5)
        self.assertEqual(test_heap.size(), 8)
        test_heap.enqueue(13)
        test_heap.enqueue(33)
        test_heap.enqueue(47)
        test_heap.dequeue()
        self.assertEqual(test_heap.peek(), 3)
        self.assertEqual(test_heap.contents(), [3, 5, 6, 5, 6, 47, 8, 9, 13, 33])

if __name__ == "__main__":
    unittest.main()
