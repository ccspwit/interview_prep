# -*- coding: utf-8 -*-
"""
Created on June 9, 2017
LeetCode problem 230
Given a binary search tree, write a function kthSmallest to find the kth
smallest element in it.

Note: 
You may assume k is always valid, 1 ? k ? BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to
find the kth smallest frequently? How would you optimize the it?
@author: K Li
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def addNode(self, val):
        '''
        Binary search Tree, compare with root value, add to left is smaller
        add to right if otherwise recursively
        '''
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
    
    def genTreeArray():
        pass

    def showNode(self):
        if self.left is not None:
            self.left.showNode()
        print(self.val, end=' ')
        if self.right is not None:
            self.right.showNode()

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        Straightforward solution. Do a inorder traversal which will yield
        sorted array. Get first k elements
        """
        stack = []
        node = root
        count = 0
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                if count == k-1:
                    return node.val
                count += 1
                root = node.right
        return None
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([1],1),
                  ([2,2,2,2,2],3),([9,7,5,3,1],3),
                  ([5,3,7,2,4,6,8],4),([10,2,4,6,8,12,14,16,18],5)]
    a = Solution()
    #testVector = [[5,3,7,2,4,6,8]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = None
        for j in range(len(test[0])):
            if j == 0:
                x = TreeNode(test[0][j])
            else:
                x.addNode(test[0][j])

        if x: x.showNode()
        print()

        print(a.kthSmallest(x,test[1]))
        #print(a.verticalOrder1(x))
