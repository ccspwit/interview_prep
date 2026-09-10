# -*- coding: utf-8 -*-
"""
Created on Thu June 6, 2017
LeetCode problem 515
You need to find the largest value in each row of a binary tree.

Example:
Input: 

          1
         / \
        3   2
       / \   \  
      5   3   9 

Output: [1, 3, 9]
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
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        DFS
        """
        if root is None:
            return []
        stack = [(root, 0)]
        result = []
        level = 0
        
        while stack:
            node, level = stack.pop()
            if len(result) <= level:
                result.append(node.val)
            else:
                result[level] = max(result[level],node.val)
    
            if node.left:
                stack.append((node.left,level+1))
            if node.right:
                stack.append((node.right, level+1))

        return result
    
    def largestValues1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        BFS, only beat 15% python submissions
        """
        if root is None:
            return []
        curLevel = [root]
        result = []
        
        while curLevel:
            result.append(max((node.val for node in curLevel)))
            nextLevel = [c for nd in curLevel for c in [nd.left, nd.right] if c]
            curLevel = nextLevel
        return result

        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,7],[10,2,4,6,8,12,14,16,18]]
    a = Solution()
    #testVector = [[10,3,4,11,12,13]]
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

        print(a.largestValues(x))
        #print(a.largestValues1(x))
