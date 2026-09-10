# -*- coding: utf-8 -*-
"""
Created on May 15, 2017
Leetcode 257
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
@author: K Li
"""
from collections import deque

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
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        Iterative solution, DFS with stack
        """
        if root is None:
            return []
        result = []
        path = str(root.val)
        stack = [(root, path)]
        while stack:
            node, path = stack.pop()
            if node.left is None and node.right is None:
                #print(node.val)
                result.append(path)
            
            if node.left is not None:
                path1 = path+"->"+str(node.left.val)
                stack.append((node.left, path1))
            if node.right is not None:
                path2 = path+"->"+str(node.right.val)
                stack.append((node.right, path2))
            
        return result

    def binaryTreePathsQueue(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        Iterative solution, BFS with queue
        """
        if root is None:
            return []
        result = []
        path = str(root.val)
        queue = deque([(root, path)])
        while queue:
            node, path = queue.popleft()
            if node.left is None and node.right is None:
                #print(node.val)
                result.append(path)
            
            if node.left is not None:
                path1 = path+"->"+str(node.left.val)
                queue.append((node.left, path1))
            if node.right is not None:
                path2 = path+"->"+str(node.right.val)
                queue.append((node.right, path2))
            
        return result

    def binaryTreePathsR(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        Recursively get path from node to lead, add it to result list
        """
        if root is None:
            return []
        result = []
        self.getPathsR(root, str(root.val), result)
        
        return result

    def getPathsR(self, root, path, res):
        """
        Return a list of ancesters of a node in a binary tree recursively.
        """
        if root.left is None and root.right is None:
            res.append(path)
            #print(len(res),res)
            return
        
        if root.left is not None:
            path1 = path+"->"+str(root.left.val)
            self.getPathsR(root.left, path1, res)
        if root.right is not None:
            path2 = path+"->"+str(root.right.val)
            self.getPathsR(root.right, path2, res)
        return
    

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,2],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,1],
                  [10,6,14,16,2,8,12,18]]
    test = [5,3,6,2,4,1]
    a = Solution()
    print(test)
    x = None
    for j in range(len(test)):
        if j == 0:
            x = TreeNode(test[j])
        else:
            x.addNode(test[j])

    if x: x.showNode()
    print()
    print(a.binaryTreePaths(x))
    print(a.binaryTreePathsQueue(x))
