# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 637
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
Note:
The range of node's value is in the range of 32-bit signed integer.
@author: K Li
"""
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        level = [root]
        result = []
        
        while level:
            values = [node.val for node in level]
            result.append(sum(values)/len(values))
            next_level = [next_node for node in level for next_node in [node.left, node.right] if next_node]
            level = next_level
        return result
