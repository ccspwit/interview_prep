# -*- coding: utf-8 -*-
"""
Created on July 9, 2019
LeetCode problem 538
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.

Example:
Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13

Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
@author: K Li
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBSTR(self, root: TreeNode) -> TreeNode:
        # start from right most node. compute cumsum
        # add to current node
        def dfs(node):
            if node:
                if node.right:
                    dfs(node.right)
                val = node.val
                node.val = node.val + self.cumsum
                self.cumsum += val
                if node.left:
                    dfs(node.left)
            return
        
        self.cumsum = 0
        dfs(root)
        return root

    def convertBST(self, root):
        total = 0
        
        node = root
        stack = []
        while stack or node is not None:
            # push all nodes up to (and including) this subtree's maximum on
            # the stack.
            while node is not None:
                stack.append(node)
                node = node.right

            node = stack.pop()
            total += node.val
            node.val = total

            # all nodes with values between the current and its parent lie in
            # the left subtree.
            node = node.left

        return root