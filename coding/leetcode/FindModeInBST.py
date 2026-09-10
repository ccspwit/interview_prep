# -*- coding: utf-8 -*-
"""
Created on May 21, 2017
Leetcode 501
Given a binary search tree (BST) with duplicates, find all the mode(s)
(the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to
the node's key. The right subtree of a node contains only nodes with keys
greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.

For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the
implicit stack space incurred due to recursion does not count).
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
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        time O(n), space O(n)
        """
        def inOrderR(root):
            if root:
                inOrderR(root.left)
                self.cnt[root.val] = self.cnt.get(root.val,0)+1
                inOrderR(root.right)
            return

        if root is None:
            return []
        self.cnt = {}
        # since we are creating a counter dictionary, traversal order is not
        # relevant
        inOrderR(root)
        #self.result will contains a sorted array of node.val
        max_cnt = max(self.cnt.values())
        return [key for key, val in self.cnt.items() if val == max_cnt]
    
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
        print(a.findMode(x))
