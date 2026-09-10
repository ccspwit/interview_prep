# -*- coding: utf-8 -*-
"""
Created on June 4, 2019
LeetCode problem 687
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.

Example 1:
Input:
              5
             / \
            4   5
           / \   \
          1   1   5
Output: 2

Example 2:
Input:
              1
             / \
            4   5
           / \   \
          4   4   5
Output: 2

Note: The given binary tree has not more than 10000 nodes.
The height of the tree is not more than 1000.
@author: K Li
"""
class Solution:
    def longestUnivaluePath(self, root):
        # much cleaner code
        self.ans = 0

        def arrow_length(node):
            if not node: return 0
            left_length = arrow_length(node.left)
            right_length = arrow_length(node.right)
            left_arrow = right_arrow = 0
            if node.left and node.left.val == node.val:
                left_arrow = left_length + 1
            if node.right and node.right.val == node.val:
                right_arrow = right_length + 1
            self.ans = max(self.ans, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.ans

    def longestUnivaluePath1(self, root: TreeNode) -> int:
        def maxPathLen(node):
            if node.left is None and node.right is None:
                return (0, 0, node.val)
            m1, n1, v1 = 0, 0, None
            m2, n2, v2 = 0, 0, None
            val = node.val

            if node.left:
                m1, n1, v1 = maxPathLen(node.left)
            if node.right:
                m2, n2, v2 = maxPathLen(node.right)
            if (val == v1) and (val == v2):
                nCont = max(n1, n2) + 1
                newMax = n1+n2+2
                maxLen = max(newMax, max(m1, m2))
            elif val == v1:
                nCont = n1 + 1
                maxLen = max(nCont, max(m1, m2))
            elif val == v2:
                nCont = n2 + 1
                maxLen = max(nCont, max(m1, m2))
            else:
                maxLen = max(m1, m2)
                nCont = 0
                
            return maxLen, nCont, val

        if not root:
            return 0
        maxLen, currLen, val = maxPathLen(root)

        return maxLen

