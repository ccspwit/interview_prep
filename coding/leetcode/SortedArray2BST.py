# -*- coding: utf-8 -*-
"""
Created on Thu May 3rd 2017
LeetCode problem 108
Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        N = len(nums)
        if N==0:
            return None
        if N==1:
            return TreeNode(nums[0])
        
        left, right = 0, N
        mid = (left+right-1)//2
        root = TreeNode(nums[mid])
        stack = [(root, left, right)]
        while len(stack)>0:
            node, left, right = stack.pop()
            mid = (left+right-1)//2
            if(mid>left):
                node.left = TreeNode(nums[(mid+left-1)//2])
                stack.append((node.left, left, mid))
            if(mid+1<right):
                node.right = TreeNode(nums[(right+mid)//2])
                stack.append((node.right, mid+1, right))
        
        return root

    def sortedArrayToBSTR(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        N = len(nums)
        if N==0:
            return None
        if N==1:
            return TreeNode(nums[0])
        
        left, right = 0, N
        mid = (left+right-1)//2
        root = TreeNode(nums[mid])
        if(mid>left):
            root.left = self.sortedArrayToBSTR(nums[left:mid])
        if(mid<right):
            root.right = self.sortedArrayToBSTR(nums[mid+1:right])
        
        return root

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,2],
                  [1,3,5,7,9],
                  [0,2,4,6,8,12,14,16,18]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)

        x = a.sortedArrayToBST(test)
        if x: x.showNode()
        print()

        x = a.sortedArrayToBSTR(test)
        if x: x.showNode()
        print()