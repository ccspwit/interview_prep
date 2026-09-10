# -*- coding: utf-8 -*-
"""
Created on May 25, 2017
Leetcode 563
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between the
sum of all left subtree node values and the sum of all right subtree node
values. Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.

Example:
Input: 
         1
       /   \
      2     3
Output: 1
Explanation: 
Tilt of node 2 : 0
Tilt of node 3 : 0
Tilt of node 1 : |2-3| = 1
Tilt of binary tree : 0 + 0 + 1 = 1
Note:

The sum of node values in any subtree won't exceed the range of 32-bit integer.
All the tilt values won't exceed the range of 32-bit integer.
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
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def nodeSumTilt(node):
            """
            Recursively compute treeSum, tile of the current node
            """
            if node:
                lSum = nodeSumTilt(node.left)
                rSum = nodeSumTilt(node.right)
                theSum = lSum + rSum + node.val
                self.tiltSum.append(abs(lSum-rSum))
            else:
                return 0
            return theSum
        
        self.tiltSum=[]
        if root:
            nodeSumTilt(root)
        else:
            return 0
        return sum(self.tiltSum)

    def findTilt1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            tiltSum = abs(self.nodeSum(root.left)-self.nodeSum(root.right))
            tiltSum += (self.findTilt1(root.left)+self.findTilt1(root.right))
        else:
            return 0
        return tiltSum
    
    def nodeSum(self, node):
        """
        Recursively compute treeSum of the current node
        """
        if node:
            theSum = self.nodeSum(node.left)+self.nodeSum(node.right)+node.val
        else:
            return 0
        return theSum
    
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
        print(a.findTilt(x))
        print(a.findTilt1(x))
