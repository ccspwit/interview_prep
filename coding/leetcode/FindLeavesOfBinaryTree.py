# -*- coding: utf-8 -*-
"""
Created on June 2nd, 2017
Leetcode 366
Given a binary tree, collect a tree's nodes as if you were doing this:
    Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree 
          1
         / \
        2   3
       / \     
      4   5    
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         / 
        2          
2. Now removing the leaf [2] would result in this tree:

          1          
3. Now removing the leaf [1] would result in the empty tree:

          []         
Returns [4, 5, 3], [2], [1].@author: K Li
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
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Traverse binary tree, record maxDepth for each node
        """
        def depthFromLeave(node):
            depth = 0
            if node:
                if (node.left is None) and (node.right is None):
                    if depth >= len(result):
                        result.append([node.val])
                    else:
                        result[depth].append(node.val)
                    return 0
                if node.left is not None:
                    depth = max(depth, depthFromLeave(node.left)+1)
                    #node.left = None
                if node.right is not None:
                    depth = max(depth, depthFromLeave(node.right)+1)
                    #node.right = None
                if depth >= len(result):
                    result.append([node.val])
                else:
                    result[depth].append(node.val)
                return depth
            else:
                return 0
        result = []
        depthFromLeave(root)
        return result
    
    def findLeaves1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Traverse binary tree, record maxDepth for each node
        """
        def depthFromLeave(node):
            depth = 0
            if node:
                if (node.left is None) and (node.right is None):
                    if depth not in result:
                        result[depth] = [node.val]
                    else:
                        result[depth].append(node.val)
                    return 0
                if node.left is not None:
                    depth = max(depth, depthFromLeave(node.left)+1)
                    #node.left = None
                if node.right is not None:
                    depth = max(depth, depthFromLeave(node.right)+1)
                    #node.right = None
                if depth not in result:
                    result[depth] = [node.val]
                else:
                    result[depth].append(node.val)
                return depth
            else:
                return 0
        result = {}
        depthFromLeave(root)
        return result
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[2,1],[2,1,3],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,1]]
                  #[10,6,14,16,2,8,12,18]]
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
        print(a.findLeaves(x))
        print(a.findLeaves1(x))
