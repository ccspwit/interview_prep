# -*- coding: utf-8 -*-
"""
Created on June 1st, 2017
Leetcode 270
Given a non-empty binary search tree and a target value, find the value in
the BST that is closest to the target.

Note:
Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest
to the target.
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
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        minDiff = abs(root.val - target)
        closetValue = root.val
        
        while root:
            diff = abs(root.val-target)
            if diff < minDiff:
                minDiff = diff
                closetValue = root.val
            if target < root.val:
                root = root.left
            elif target > root.val:
                root = root.right
            else:
                closetValue = root.val
                break
        return closetValue

    def closestValue1(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        minLeft, minRight = float('inf'), float('inf')
        closetValue = None
        node = root
        
        while node:
            if target < node.val:
                minRight = min(minRight, node.val - target)
                if minRight < minLeft:
                    closetValue = node.val
                node = node.left
            elif target > node.val:
                minLeft = min(minLeft, target - node.val)
                if minLeft < minRight:
                    closetValue = node.val
                node = node.right
            else:
                minLeft = 0
                closetValue = node.val
                break
        return closetValue
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([1],2.1),([2,1],1.6),([2,1,3],2.8),
                  ([2,2,2,2,2],2.2),([9,7,5,3,1],5.5),
                  ([5,3,6,2,4,1],3.6)]
                  #[10,6,14,16,2,8,12,18]]
    a = Solution()
    for n, test in enumerate(testVector):
        print('Test case ----- ', n)
        print(test)
        x = None
        for j in range(len(test[0])):
            if j == 0:
                x = TreeNode(test[0][j])
            else:
                x.addNode(test[0][j])
    
        if x: x.showNode()
        print("\n closest value to %f is %f"%(test[1],a.closestValue(x,test[1])))
