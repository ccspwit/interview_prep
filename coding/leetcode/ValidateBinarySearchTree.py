# -*- coding: utf-8 -*-
"""
Created on June 1 2019
LeetCode problem 98
Given a binary tree, determine if it is a valid binary search
tree (BST).

Assume a BST is defined as follows:
The left subtree of a node contains only nodes with keys less
than the node's key.
The right subtree of a node contains only nodes with keys
greater than the node's key.
Both the left and right subtrees must also be binary search
trees.
 

Example 1:
    2
   / \
  1   3

Input: [2,1,3]
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right
child's value is 4.
@author: K Li
"""
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def preorder_traverse(node, seq):
            if node.left is not None:
                preorder_traverse(node.left, seq)
            seq.append(node.val)
            if node.right is not None:
                preorder_traverse(node.right, seq)
            return

        # first pre-oder traverse
        # check if sequence is in ascending order
        
        seq = []
        if root is None:
            return True
        preorder_traverse(root, seq)
        # check if seq if sorted
        if len(seq) == 1:
            return True
        valid = True
        for n in range(1, len(seq)):
            if seq[n-1] >= seq[n]:
                return False
        return valid
