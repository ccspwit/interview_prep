# -*- coding: utf-8 -*-
"""
Created on July 10, 2019
LeetCode problem 590
Given an n-ary tree, return the postorder  traversal of its nodes' values.

For example, given a 3-ary tree:
        1
    3   2   4
  5 6 7    8 9
Return its preorder traversal as: [5,6,7,3,2,8,9,4,1].
@author: K Li
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
tree = {"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6},{"$id":"7","children":[],"val":7}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[{"$id":"8","children":[],"val":8},{"$id":"9","children":[],"val":9}],"val":4}],"val":1}
class Solution:
    def postorderR(self, root: 'Node') -> List[int]:
        def dfs(node):
            if node:
                for ch in node.children:
                    dfs(ch)
                ans.append(node.val)

        ans, stack = [], []
        dfs(root)
        return ans

    def postorder(self, root: 'Node') -> List[int]:
        # compared with pre-order iteration
        # push children in normal order
        # reverse result
        ans, stack = [], [root]
        if root:
            # stack.append(root)
            node = root
            while stack:
                node = stack.pop()
                if node.children:
                    # stack.append(node)
                    stack.extend(node.children)
                ans.append(node.val)
     
        return ans[::-1]