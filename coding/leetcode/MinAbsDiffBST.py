# -*- coding: utf-8 -*-
"""
Created on May 24, 2017
Leetcode 530
Given a binary search tree with non-negative values, find the minimum absolute
difference between values of any two nodes.

Example:
Input:

   1
    \
     3
    /
   2
Output: 1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1
(or between 2 and 3).
Note: There are at least two nodes in this BST.
@author: K Li
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def addNode(self, val):
        if val < self.val:  # add node to left
            if(self.left) is None:
                leftNode = TreeNode(val)
                self.left = leftNode
            else:
                self.left.addNode(val)
        else:   # add node to right
            if(self.right) is None:
                rightNode = TreeNode(val)
                self.right = rightNode
            else:
                self.right.addNode(val)
        return
    def showNode(self):
        if self.left is not None:
            self.left.showNode()
        print(self.val, end=' ')
        if self.right is not None:
            self.right.showNode()

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def inOrderT(root):
            if root is None:
                return
            if root.left:
                inOrderT(root.left)
            self.array.append(root.val)
            if root.right:
                inOrderT(root.right)
            return
        
        self.array = []
        inOrderT(root)
        N= len(self.array)
        if N <2:
            raise ValueError("BST shall have at least two nodes.")
        """minDist = float('inf')
        for n in range(N-1):
            dist = abs(self.array[n]-self.array[n+1])
            minDist = min(minDist, dist)
        return minDist"""
        return min([self.array[i+1]-self.array[i] for i in range(N-1)])
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [#[],[1],[1,2],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,1],
                  [10,6,14,16,2,8,12,18]]
    a = Solution()
    for n, test in enumerate(testVector):
        print('Test case ----- ', n)
        print(test)
        x = None
        for j in range(len(test)):
            if j == 0:
                x = TreeNode(test[j])
            else:
                x.addNode(test[j])
    
        if x: x.showNode()
        print()
        print(a.getMinimumDifference(x))
