import unittest
from ordered_list import *
import sys

# Test cases - write more!

class TestLab4(unittest.TestCase):

    def test_00_init(self) -> None:
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())
        t_list.add(4)
        self.assertEqual(t_list.size(), 1)
        t_list.add(6)
        t_list.add(15)
        t_list.add(1)
        self.assertEqual(t_list.size(), 4)
        self.assertEqual(t_list.is_empty(), False)

    def test_02_add(self) -> None:
        t_list = OrderedList()
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())
        t_list.add(20)
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        self.assertEqual(t_list.size(), 2)
        t_list.add(30)
        self.assertEqual(t_list.python_list(), [10, 20, 30])
        self.assertEqual(t_list.size(), 3)
        t_list.add(5)
        self.assertEqual(t_list.python_list(), [5, 10, 20, 30])
        self.assertEqual(t_list.size(), 4)
        t_list.add(15)
        self.assertEqual(t_list.python_list(), [5, 10, 15, 20, 30])
        self.assertEqual(t_list.python_list_reversed(), [30, 20, 15, 10, 5])
        self.assertEqual(t_list.size(), 5)

    def test_03_remove(self) -> None:
        t_list = OrderedList()
        self.assertFalse(t_list.remove(5))
        self.assertEqual(t_list.size(), 0)
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertFalse(t_list.remove(5))
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(t_list.size(), 5)
        self.assertFalse(t_list.remove(55))
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(t_list.size(), 5)
        self.assertTrue(t_list.remove(40))
        self.assertEqual(t_list.python_list(), [10, 20, 30, 50])
        self.assertEqual(t_list.size(), 4)
        self.assertTrue(t_list.remove(10))
        self.assertEqual(t_list.python_list(), [20, 30, 50])
        self.assertEqual(t_list.size(), 3)
        self.assertTrue(t_list.remove(50))
        self.assertEqual(t_list.python_list(), [20, 30])
        self.assertEqual(t_list.size(), 2)
        self.assertTrue(t_list.remove(20))
        self.assertEqual(t_list.python_list(), [30])
        self.assertEqual(t_list.size(), 1)
        self.assertTrue(t_list.remove(30))
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)

    def test_04_index(self) -> None:
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        self.assertEqual(t_list.index(10), 0)
        self.assertEqual(t_list.index(20), 1)
        self.assertEqual(t_list.index(5), None)

    def test_04_index_02(self) -> None:
        tlist = OrderedList()
        tlist.add(50)
        tlist.add(49)
        self.assertEqual(tlist.index(49), 0)
        self.assertEqual(tlist.index(50), 1)
        self.assertEqual(tlist.index(5), None)
        tlist.add(4)
        self.assertEqual(tlist.index(4), 0)

    def test_05_pop(self) -> None:
        t_list = OrderedList()
        t_list.add(10)
        t_list.add(20)
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertRaises(IndexError, t_list.pop, -1)
        self.assertEqual(t_list.size(), 5)
        self.assertRaises(IndexError, t_list.pop, 5)
        self.assertEqual(t_list.size(), 5)
        self.assertEqual(t_list.pop(0), 10)
        self.assertEqual(t_list.python_list(), [20, 30, 40, 50])
        self.assertEqual(t_list.python_list_reversed(), [50, 40, 30, 20])
        self.assertEqual(t_list.size(), 4)
        self.assertEqual(t_list.pop(3), 50)
        self.assertEqual(t_list.python_list(), [20, 30, 40])
        self.assertEqual(t_list.size(), 3)
        self.assertEqual(t_list.pop(1), 30)
        self.assertEqual(t_list.python_list(), [20, 40])
        self.assertEqual(t_list.size(), 2)
        self.assertEqual(t_list.pop(0), 20)
        self.assertEqual(t_list.python_list(), [40])
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.pop(0), 40)
        self.assertEqual(t_list.python_list(), [])
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())

    def test_06_search(self) -> None:
        t_list = OrderedList()
        self.assertFalse(t_list.search(10))
        t_list.add(10)
        t_list.add(20)
        self.assertTrue(t_list.search(10))
        self.assertTrue(t_list.search(20))
        self.assertFalse(t_list.search(25))

    def test_07_python_list(self) -> None:
        t_list = OrderedList()
        self.assertEqual(t_list.python_list(),[])
        self.assertEqual(t_list.python_list_reversed(), [])
        t_list.add(10)
        self.assertEqual(t_list.python_list(), [10])
        self.assertEqual(t_list.python_list_reversed(), [10])
        t_list.add(20)
        self.assertEqual(t_list.python_list(), [10, 20])
        self.assertEqual(t_list.python_list_reversed(), [20, 10])
        t_list.add(30)
        t_list.add(40)
        t_list.add(50)
        self.assertEqual(t_list.python_list(), [10, 20, 30, 40, 50])
        self.assertEqual(t_list.python_list_reversed(), [50, 40, 30, 20, 10])

    def test_08_size_is_empty(self) -> None:
        t_list = OrderedList()
        self.assertEqual(t_list.size(),0)
        self.assertTrue(t_list.is_empty())
        t_list.add(10)
        self.assertEqual(t_list.size(), 1)
        self.assertFalse(t_list.is_empty())

    def test_09_add_remove_all_add(self) -> None:
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(200):
            self.assertTrue(t_list.remove(val))
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.size(), 0)
        for val in range(200):
            t_list.add(val)
        self.assertEqual(t_list.size(), 200)
        self.assertFalse(t_list.is_empty())

    def test_10_add_pop_all_add(self) -> None:
        t_list = OrderedList()
        for val in range(200):
            t_list.add(val)
        for val in range(199, -1, -1):
            self.assertEqual(t_list.pop(val), val)
        self.assertTrue(t_list.is_empty())
        self.assertEqual(t_list.size(), 0)
        for val in range(200):
            t_list.add(val)
        self.assertEqual(t_list.size(), 200)
        self.assertFalse(t_list.is_empty())

    def test_11_general(self) -> None:
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(14)
        self.assertFalse(t_list.is_empty())
        self.assertEqual(t_list.pop(0), 14)
        self.assertTrue(t_list.is_empty())
        t_list.add(77)
        t_list.add(14)
        t_list.add(55)
        self.assertEqual(t_list.size(), 3)
        self.assertTrue(t_list.remove(14))
        self.assertFalse(t_list.remove(44))
        self.assertFalse(t_list.remove(14))
        self.assertEqual(t_list.index(77), 1)
        self.assertEqual(t_list.index(55), 0)
        t_list.remove(77)
        self.assertEqual(t_list.index(55), 0)

    def test_12_add_remove_size_empty(self) -> None:
        t_list = OrderedList()
        self.assertTrue(t_list.is_empty())
        t_list.add(14)
        self.assertEqual(t_list.size(), 1)
        t_list.add(14)
        t_list.add(14)
        self.assertEqual(t_list.size(), 1)
        self.assertEqual(t_list.pop(0), 14)
        self.assertEqual(t_list.size(), 0)
        self.assertTrue(t_list.is_empty())

    def test_13_index(self) -> None:
        t_list = OrderedList()
        self.assertEqual(t_list.index(50), None)
        t_list.add(4)
        t_list.add(56)
        t_list.add(1)
        self.assertEqual(t_list.index(4), 1)
        self.assertEqual(t_list.index(1), 0)
        self.assertEqual(t_list.index(56), 2)
        self.assertEqual(t_list.index(0), None)
        self.assertEqual(t_list.index(89), None)
        self.assertEqual(t_list.index(23), None)


    def test_14_pop(self) -> None:
        t_list = OrderedList()
        t_list.add(4)
        t_list.add(56)
        t_list.add(1)
        self.assertEqual(t_list.pop(2), 56)
        with self.assertRaises(IndexError):
            t_list.pop(2)
        self.assertEqual(t_list.pop(0), 1)
        self.assertEqual(t_list.pop(0), 4)





if __name__ == '__main__': 
    unittest.main()
