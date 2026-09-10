# -*- coding: utf-8 -*-
"""
Created on July 12, 2019
LeetCode problem 559
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest
path from the root node down to the farthest leaf node.
@author: K Li
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def dfs(node, level):
            if node:
                self.max_depth = max(self.max_depth, level)
                for ch in node.children:
                    dfs(ch, level+1)
        self.max_depth = 0
        dfs(root, 1)
        return self.max_depth

    def maxDepthBFS(self, root):
        # BFS
        queue = []
        if root: queue.append((root, 1))
        depth = 0
        for (node, level) in queue:
            depth = level
            queue += [(child, level+1) for child in node.children]
        return depth

    def maxDepthMAP(self, root):
        if not root: return 0
        return 1 + max(map(self.maxDepth, root.children or [None]))
