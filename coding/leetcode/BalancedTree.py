# -*- coding: utf-8 -*-
"""
Created on Thu May 3rd 2017
Leetcode 110
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced binary tree is defined as a binary tree
in which the depth of the two subtrees of every node never differ by more
than 1.
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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Wrapper function, to extract balanced flag from the modified
        maxDepthBalance() function
        """
        if root == None:
            return True
        depth, flag = self.maxDepthBalance(root)
        return flag
        
    def maxDepthBalance(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Find maximal depth of a binary tree recursively
        At the same time, keep track of whether left/right subtrees are balanced
        """
        if root == None:
            return (0, True)
        depth = 0

        n1, f1 = self.maxDepthBalance(root.left)
        n2, f2 = self.maxDepthBalance(root.right)
        depth = max(n1,n2)+1
        flag = f1&f2&(abs(n1-n2)<=1)

        return depth, flag


if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,2],[1,2,3,4,5],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [10,6,14,16,2,8,12,18]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = None
        for j in range(len(test)):
            if j == 0:
                x = TreeNode(test[j])
            else:
                x.addNode(test[j])

        if x: x.showNode()
        print()
        print('Is tree balanced: ', 'YES' if a.isBalanced(x) else 'NO')