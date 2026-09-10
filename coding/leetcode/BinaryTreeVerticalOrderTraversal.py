# -*- coding: utf-8 -*-
"""
Created on Thu June 9, 2017
LeetCode problem 314
Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column). If two nodes are in the same row
and column, the order should be from left to right.

Examples:

Given binary tree [3,9,20,null,null,15,7],
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7
return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]

Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]

Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5] (0's right child is 2 and 1's left child is 5),
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2
return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
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
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Use regular DFS preorder, for each level, -1 if go left, +1 if go right
        save result in hashmap, then output accoring to vertical postions.
        """
        if root is None:
            return []
        stack = [(root,0,0)]
        posMap = {}
        result = []
        level = 0
        
        while stack:
            node, pos, depth = stack.pop()
            posMap[pos] = posMap.get(pos,[])+[(node.val, depth)]
            if node.right:
                stack.append((node.right, pos+1, depth+1))
            if node.left:
                stack.append((node.left, pos-1, depth+1))
        
        #print(posMap)
        for pos in sorted(posMap):
            row = sorted(posMap[pos], key=lambda x:x[1])
            result.append([r[0] for r in row])
        return result
    
    def verticalOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Use regular BFS, for each level, -1 if go left, +1 if go right
        save result in hashmap, then output accoring to vertical postions.
        """
        if root is None:
            return []
        curLevel = [(root,0)]
        posMap = {}
        result = []
        level = 0
        
        while curLevel:
            for node, pos in curLevel:
                posMap[pos] = posMap.get(pos,[])+[node.val]
            nextLevel = []
            for node, pos in curLevel:
                if node.left:
                    nextLevel.append((node.left, pos-1))
                if node.right:
                    nextLevel.append((node.right, pos+1))
            curLevel = nextLevel
            level += 1

        for pos in sorted(posMap):
            result.append(posMap[pos])
        return result
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,7,2,4,6,8],[10,2,4,6,8,12,14,16,18]]
    a = Solution()
    #testVector = [[5,3,7,2,4,6,8]]
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

        print(a.verticalOrder(x))
        print(a.verticalOrder1(x))
