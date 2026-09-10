# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 429
Given an n-ary tree, return the level order traversal of its nodes'
values. (ie, from left to right, level by level).

For example, given a 3-ary tree:
We should return its level order traversal:
[
     [1],
     [3,2,4],
     [5,6]
]

Note:
The depth of the tree is at most 1000.
The total number of nodes is at most 5000.
@author: K Li
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        result = []
        currLevel = [root]
        
        while currLevel:
            values = [node.val for node in currLevel]
            result.append(values)
            nextLevel = [child for node in currLevel for child in node.children]
            currLevel = nextLevel
        return result
