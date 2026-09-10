# -*- coding: utf-8 -*-
"""
Created on June 8, 2019
LeetCode problem 872
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
Note:

Both of the given trees will have between 1 and 100 nodes.
@author: K Li
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leafSeq(node, seq):
            if not node:
                return
            if not node.left and not node.right:
                seq.append(node.val)
            if node.left:
                leafSeq(node.left, seq)
            if node.right:
                leafSeq(node.right, seq)
            return

        s1, s2 = [], []
        leafSeq(root1, s1)
        leafSeq(root2, s2)
        return s1==s2
