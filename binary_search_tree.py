from dataclasses import dataclass
from typing import Union, TypeAlias, Tuple, Any, List
from queue_array import *

BTree: TypeAlias = Union[None, 'Node']

MaybeInt: TypeAlias = Union[None, int]
MaybeTuple: TypeAlias = Union[None, Tuple[Any, Any]]

@dataclass
class Node:
    key: Any                # key for Node, unique ID
    data: Any               # payload for Node
    left: BTree = None      # left child (Node or None)
    right: BTree = None     # right child (Node or None)

@dataclass
class BinarySearchTree:
    root: BTree = None      # root of BST

    # returns True if tree is empty, else False
    def is_empty(self) -> bool:
        if self.root is None:
            return True
        else:
            return False

    # returns True if key is in a node of the tree, else False
    def search(self, key: Any) -> bool:
        if self.is_empty():
            return False
        cur = self.root
        while cur.key != key:
            if key < cur.key:
                if cur.left is None:
                    return False
                cur = cur.left
            if key > cur.key:
                if cur.right is None:
                    return False
                cur = cur.right
        if cur.key == key:
            return True

    # Inserts new node w/ key and data
    # If an item with the given key is already in the BST,
    # the data in the tree will be replaced with the new data
    # Example creation of node: temp = Node(key, data)
    def insert(self, key: Any, data: Any = None) -> None:
        cur = self.root
        if self.is_empty():
            self.root = Node(key, data, None, None)
        else:
            self.insert_helper(key, data, cur)

    def insert_helper(self, key: Any, data: Any, position: Node) -> None:
        if key == position.key:
            position.data = data
        if key < position.key:
            if position.left is None:
                position.left = Node(key, data, None, None)
            else:
                return self.insert_helper(key, data, position.left)
        elif key > position.key:
            if position.right is None:
                position.right = Node(key, data, None, None)
            else:
                return self.insert_helper(key, data, position.right)

    # returns tuple with min key and associated data in the BST
    # returns None if the tree is empty
    def find_min(self) -> MaybeTuple:
        if self.is_empty():
            return None
        else:
            cur = self.root
            while cur.left is not None:
                cur = cur.left
            return (cur.key, cur.data)

    # returns tuple with max key and associated data in the BST
    # returns None if the tree is empty
    def find_max(self) -> MaybeTuple:
        if self.is_empty():
            return None
        else:
            cur = self.root
            while cur.right is not None:
                cur = cur.right
            return (cur.key, cur.data)

    # return the height of the tree
    # if tree is empty, return None
    def tree_height(self) -> MaybeInt:
        if self.is_empty():
            return None
        height = self.tree_height_helper(self.root)
        return height

    def tree_height_helper(self, pos: Node):
        if pos is None:
            return - 1
        else:
            return 1 + max(self.tree_height_helper(pos.left), self.tree_height_helper(pos.right))

    # return Python list of BST keys representing inorder traversal of BST
    def inorder_list(self) -> List:
        if self.is_empty():
            return []
        cur = self.root
        ret_list = []
        self.inorder_helper(cur, ret_list)
        return ret_list

    def inorder_helper(self, nodes, lst):
        if nodes.left is not None:
            self.inorder_helper(nodes.left, lst)
        lst.append(nodes.key)
        if nodes.right is not None:
            self.inorder_helper(nodes.right, lst)
        return lst

    # return Python list of BST keys representing preorder traversal of BST
    def preorder_list(self) -> List:
        if self.is_empty():
            return []
        cur = self.root
        ret_list = []
        self.preorder_helper(cur, ret_list)
        return ret_list

    def preorder_helper(self, nodes, lst):
        lst.append(nodes.key)
        if nodes.left is not None:
            self.preorder_helper(nodes.left, lst)
        if nodes.right is not None:
            self.preorder_helper(nodes.right, lst)

    # return Python list of BST keys representing level-order traversal of BST
    # You MUST use your queue_array data structure from lab 3 to implement this method
    def level_order_list(self) -> List:
        q = Queue(25000)  # Don't change this!
        if self.is_empty():
            return []
        ret_list = []
        q.enqueue(self.root)
        while not q.is_empty():
            top = q.dequeue()
            ret_list.append(top.key)
            if top.left is not None:
                q.enqueue(top.left)
            if top.right is not None:
                q.enqueue(top.right)
        return ret_list
