# -*- coding: utf-8 -*-
"""
Created on May 17, 2017
Leetcode 404
Find the sum of all left leaves in a given binary tree.

Example:
    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15
respectively. Return 24.
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
    def sumOfLeftLeaves(self, root, isLeft = False):
        """
        :type root: TreeNode
        :rtype: int
        cleaner version of sumOfLeftLeavesR, default value of isLeft is False
        """
        if root is None:
            return 0
        if (root.left is None) and (root.right is None):
            if isLeft:
                return root.val
        result = 0
        if root.left is not None:
            result += self.sumOfLeftLeaves(root.left, True)
        if root.right is not None:
            result += self.sumOfLeftLeaves(root.right, False)
        return result

    def sumOfLeftLeavesR(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Recursive solution, use a helper function with isLeft flag
        """
        if root is None:
            return 0
        result = self.sumLeftLeavesR(root, 0)
        return result
    
    def sumLeftLeavesR(self, root, isLeft):
        if root is None:
            return 0
        if (root.left is None) and (root.right is None):
            if isLeft:
                return root.val
        result = 0
        if root.left is not None:
            result += self.sumLeftLeavesR(root.left, 1)
        if root.right is not None:
            result += self.sumLeftLeavesR(root.right, 0)
        return result

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,2],
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
        print(a.sumOfLeftLeaves(x))
