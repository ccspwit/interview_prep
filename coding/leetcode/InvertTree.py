# -*- coding: utf-8 -*-
"""
Created on May 14th 2017
Leetcode 226
Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
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
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Iterative, DFS
        """
        if root is None:
            return None
        if (root.left is None) and (root.right is None):
            return root
        stack = [root]
        
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.extend([node.left, node.right])
        return root

    def invertTree1(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Iterative, BFS
        """
        from collections import deque
        if root is None:
            return None

        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root
    
    def invertTreeR(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Recursive, DFS
        """
        if root is None:
            return None
        if (root.left is None) and (root.right is None):
            return root

        if root.left is not None:
            self.invertTree(root.left)
        if root.right is not None:
            self.invertTree(root.right)
        tmp = root.right
        root.right = root.left
        root.left = tmp

        return root

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,2],[1,2,3,4,5],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [4,2,1,3,7,6,9],
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
        y = a.invertTree1(x)
        if y: y.showNode()
        print()