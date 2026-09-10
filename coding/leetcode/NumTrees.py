# -*- coding: utf-8 -*-
"""
Created on Thu May 2nd 2017
LeetCode problem 96
Given n, how many structurally unique BST's (binary search trees) that store
values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.
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
    cache = {}
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        numTrees(n) = \sum_{i=0}^{n-1} numTrees(i)*numTrees(n-1-i)
        """
        Cache = type(self).cache
        Cache[0] = 1
        Cache[1] = 1
        
        if n<=0:
            return 1
        if n in Cache:
            return Cache[n]
        
        for i in range(2,n+1):
            nTrees = 0
            for j in range(i):
                nTrees += Cache[j]*Cache[i-j-1]
            Cache[i] = nTrees
            #if i not in cache:
        return nTrees

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [1,2,3,4,5,7,10]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        
        print('Number of unique BSTs is %d' %a.numTrees(test))
