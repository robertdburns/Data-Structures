import unittest
from binary_search_tree import *
import random

class TestLab4(unittest.TestCase):

    def test_01_simple(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.tree_height(), None)
        self.assertTrue(bst.is_empty())

    def test_02_insert_search(self) -> None:
        bst = BinarySearchTree()
        values = [99, -4, 167, 139, 55, -89, 13, 78, 128, 119]

        for val in values:
            bst.insert(val)

        for val in values:
            self.assertTrue(bst.search(val))
            self.assertFalse(bst.search(val - 1))
            self.assertFalse(bst.search(val + 1))
            
    def test_03_search_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertFalse(bst.search(999))

    def test_04_pre_in_level_order_empty_list(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(bst.preorder_list(), [])
        self.assertEqual(bst.inorder_list(), [])
        self.assertEqual(bst.level_order_list(), [])
                
    def test_07_test_min_max_empty(self) -> None:
        bst = BinarySearchTree()
        self.assertEqual(None, bst.find_max())
        self.assertEqual(None, bst.find_min())

    def test_08_test_inorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.inorder_list(), [-89, -4, 13, 55, 78, 99, 139, 167, 174, 178])

    def test_09_test_preorder(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.preorder_list(), [99, -4, -89, 55, 13, 78, 167, 139, 178, 174])

    def test_09_test_level_order(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])
      
        self.assertEqual(bst.level_order_list(), [99, -4, 167, -89, 55, 139, 178, 13, 78, 174])
        
    def test_14_insert_replace(self) -> None:
        bst = BinarySearchTree()
        bst.insert(30, 'aaa')
        bst.insert(40, 'bbb')
        bst.insert(35, 'ccc')
        bst.insert(50, 'ddd')
        bst.insert(60, 'eee')
        bst.insert(60, 'zzz')
        self.assertEqual(bst.find_max(), (60, 'zzz'))
        self.assertEqual(bst.tree_height(), 3)

    def test_16_test_tree_height(self) -> None:
        bst = BinarySearchTree()
        keys = [99, -4, 167, 139, 55, -89, 13, 78, 178, 174]
      
        for i in range(len(keys)):
            bst.insert(keys[i])            
        self.assertEqual(bst.tree_height(), 3)

    def test_min_max(self) -> None:
        bst = BinarySearchTree()
        keys = [8, 3, 10, 6, 1, 7, 4, 14, 13]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertEqual(bst.find_min(), (1, None))
        self.assertEqual(bst.find_max(), (14, None))

    def test_general_cases(self):
        bst = BinarySearchTree()
        keys = [55, -4, 15, 99, 108, 34, 19, 96, 91, 193, 216]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertFalse(bst.is_empty())
        self.assertFalse(bst.search(51))
        self.assertTrue(bst.search(15))
        self.assertEqual(bst.find_min(), (-4, None))
        self.assertEqual(bst.find_max(), (216, None))
        self.assertEqual(bst.tree_height(), 4)
        self.assertEqual(bst.inorder_list(), [-4, 15, 19, 34, 55, 91, 96, 99, 108, 193, 216])
        self.assertEqual(bst.level_order_list(), [55, -4, 99, 15, 96, 108, 34, 91, 193, 19, 216])

    def test_general_cases2(self) -> None:
        bst = BinarySearchTree()
        keys = [89, 93, 73, 99, 88, 35, 74, 70, 38, 75, 87]

        for i in range(len(keys)):
            bst.insert(keys[i])

        self.assertFalse(bst.is_empty())
        self.assertFalse(bst.search(759))
        self.assertTrue(bst.search(87))
        self.assertTrue(bst.search(89))
        self.assertFalse(bst.search(76))
        self.assertTrue(bst.search(99))
        self.assertEqual(bst.find_max(), (99, None))
        self.assertEqual(bst.find_min(), (35, None))
        self.assertEqual(bst.tree_height(), 5)
        self.assertEqual(bst.level_order_list(), [89, 73, 93, 35, 88, 99, 70, 74, 38, 75, 87])
        self.assertEqual(bst.inorder_list(), [35, 38, 70, 73, 74, 75, 87, 88, 89, 93, 99])
        self.assertEqual(bst.preorder_list(), [89, 73, 35, 70, 38, 88, 74, 75, 87, 93, 99])






if __name__ == '__main__': 
    unittest.main()
