# -*- coding: utf-8 -*-
"""
Created on June 15, 2019
LeetCode problem 1022
Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path represents a binary number starting with the most significant bit.  For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf.
Return the sum of these numbers.

Example 1:
Input: [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
@author: K Li
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, path_val):
            if not node:
                return 
            new_val = path_val*2 + node.val
            if node.left is None and node.right is None:
                self.ans.append(new_val)
                return
            if node.left:
                dfs(node.left, new_val)
            if node.right:
                dfs(node.right, new_val)

        self.ans = []
        dfs(root, 0)
        return sum(self.ans)
