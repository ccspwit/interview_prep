# -*- coding: utf-8 -*-
"""
Created on July 10, 2019
LeetCode problem 589
Given an n-ary tree, return the preorder traversal of its nodes' values.

For example, given a 3-ary tree:
        1
    3   2   4
  5 6 7    8 9
Return its preorder traversal as: [1,3,5,6,7,2,4,8,9].
@author: K Li
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # iterative solution, use stack
        ans, stack = [], []
        if root:
            stack.append(root)
            while stack:
                node = stack.pop()
                ans.append(node.val)
                # reverse push
                if node.children:
                    stack.extend(node.children[::-1])
        
        return ans
