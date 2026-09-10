# -*- coding: utf-8 -*-
"""
Created on June 8, 2019
LeetCode problem 897
Given a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.

Example 1:
Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \ 
1        7   9
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9  
Note:
The number of nodes in the given tree will be between 1 and 100.
Each node will have a unique integer value from 0 to 1000.
@author: K Li
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inOrder(node):
            if not node:
                return node
            # in order traverse
            # create a temp node to link and keep current node 
            if node.left:
                inOrder(node.left)
            # left most node
            node.left = None
            self.temp.right = node
            self.temp = node
            if node.right:
                inOrder(node.right)

            return

        self.temp = TreeNode(0)
        ans = self.temp
        inOrder(root)
        return ans.right

    def increasingBST1(self, root: TreeNode) -> TreeNode:
        # in order traverse, main head and tail of subtree
        def inOrder(node):
            if not node:
                return node
            head, tail = node, None
            # for each subtree, get head and tail
            # rearrange head/node/tail
            if node.left:
                lhead, ltail = inOrder(node.left)
                if ltail is None:
                    ltail = lhead
                ltail.right = node
                node.left = None
                head = lhead
                tail = node
            if node.right:
                rhead, rtail = inOrder(node.right)
                if rtail is None:
                    rtail = rhead
                node.right = rhead
                tail = rtail
            return head, tail
        
        return inOrder(root)[0]

    def increasingBST2(self, root):
        # in order. in place
        # maintain a global head node
        # cleaner, but hard to understand
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        self.cur = TreeNode(None)
        ans = self.cur

        inorder(root)
        return ans.right
