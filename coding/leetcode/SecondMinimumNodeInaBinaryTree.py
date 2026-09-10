# -*- coding: utf-8 -*-
"""
Created on July 13, 2019
LeetCode problem 671
Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input: 
    2
   / \
  2   5
     / \
    5   7
Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.

Example 2:
Input: 
    2
   / \
  2   2
Output: -1
Explanation: The smallest value is 2, but there isn't any second smallest value.
@author: K Li
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(root):
            if root:
                if ans[0] < root.val < ans[1]:
                    # new root is min of subtree
                    # new root val as 2nd_min, stop recursion
                    ans[1] = root.val
                elif root.val == ans[0]:
                    # new root val == 2nd_min, recursion
                    dfs(root.left)
                    dfs(root.right)
                else:
                    # new root val > 2nd_min, stop recursion
                    pass
            return

        if not root:
            return -1

        # root.val is always min, initiaze 2nd_min as inf
        ans = [root.val, float('inf')]
        dfs(root)
        
        return ans[1] if ans[1]<float('inf') else -1
