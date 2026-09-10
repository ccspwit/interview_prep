# -*- coding: utf-8 -*-
"""
Created on June 1st, 2017
Leetcode 156
Given a binary tree where all the right nodes are either leaf nodes with
a sibling (a left node that shares the same parent node) or empty, flip it
upside down and turn it into a tree where the original right nodes turned
into left leaf nodes. Return the new root.

For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5
return the root of the binary tree [4,5,2,#,#,3,1].
   4
  / \
 5   2
    / \
   3   1  
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
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Iterative solution
        """

        if not root:
            return None
        newroot = None
        stack = [(root, None, None)]
        node, parent, right = stack[-1]
        while node.left:
            stack.append((node.left, node, node.right))
            node = node.left
        newroot = node

        while stack:
            node, parent, right = stack.pop()
            node.left = right
            node.right = parent
        return newroot

    def upsideDownBinaryTreeR(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Recursive solution first
        """
        def flipTree(node, parent, rightNode):
            """
            """
            # node will not be None
            if node.left:
                flipTree(node.left, node, node.right)
                node.left = rightNode
                node.right = parent
            else:
                # left most node reached
                self.newroot = node
                node.left = rightNode
                node.right = parent
            return
                
        self.newroot = None
        if root:
            flipTree(root, None, None)
            return self.newroot
        else:
            return None
        
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[2,1],[2,1,3],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,1],
                  [10,6,14,16,2,8,12,18]]
    #testVector=[[2,1]]
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
        y = a.upsideDownBinaryTree(x)
        if y: y.showNode()
        print()
