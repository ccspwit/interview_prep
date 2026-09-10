# -*- coding: utf-8 -*-
"""
Created on May 25, 2017
Leetcode 543
Given a binary tree, you need to compute the length of the diameter of the
tree. The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of
edges between them.
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
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Not very efficient
        """
        def getDepth(root):
            """
            Find the maximal depth of a binary tree
            root: TreeNode
            rtype: int
            """
            left, right = 0, 0
            if root:
                left = getDepth(root.left)+1
                right = getDepth(root.right)+1
                diameter = left+right-2
                if diameter>self.result:
                    self.result = diameter
                return max(left, right)
            else:
                return 0

        self.result = 0
        if root:
            getDepth(root)
            return self.result
        else:
            return 0

        
    def diameterOfBinaryTree1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Not very efficient
        """
        if root:
            D1 = self.maxDepth(root.left)+self.maxDepth(root.right)
            D2 = self.diameterOfBinaryTree1(root.left)
            D3 = self.diameterOfBinaryTree1(root.right)
            return max([D1,D2,D3])
        else:
            return 0
    def maxDepth(self, root):
        """
        Find the maximal depth of a binary tree
        root: TreeNode
        rtype: int
        """
        left, right = 0, 0
        if root:
            left = self.maxDepth(root.left)+1
            right = self.maxDepth(root.right)+1
            return max(left,right)
        else:
            return 0
    
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
        print(a.diameterOfBinaryTree(x))
        print(a.diameterOfBinaryTree1(x))
