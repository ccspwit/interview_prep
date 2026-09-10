# -*- coding: utf-8 -*-
"""
Created on Thu May 3rd 2017
LeetCode problem 101
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
But the following [1,2,2,null,3,null,3] is not:
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        Recursive solution
        """
        if root is None:
            return True
        left, right = root.left, root.right
        
        if (left is not None) and (right is not None):
            return self.isMirrorNR(left, right)
        else:
            return (left == right)
        
    def isMirrorNR(self, node1, node2):
        '''
        Decide if node1 and node2 are symmetric non-recursively
        '''
        stack = [(node1, node2)]
        result = True
        while len(stack)>0:
            (node1, node2) = stack.pop()
            if (node1 is None) and (node2 is None):
                continue
            elif(node1 is None) or (node2 is None):
                return False
            else:   # both are not None
                if(node1.val != node2.val):
                    return False
                left, right = node1.left, node2.right
                stack.append((left, right))
                left, right = node1.right, node2.left
                stack.append((left, right))
               
        return result

    def isMirror(self, node1, node2):
        '''
        Recursively decide if node1 and node2 are symmetric
        '''
        if (node1.val != node2.val):
            return False
        # else clause
        result = True
        left, right = node1.left, node2.right
        if (left is not None) and (right is not None):
            result & self.isMirror(left, right)
        else:
            result &= (left == right)

        left, right = node1.right, node2.left
        if (left is not None) and (right is not None):
            result & self.isMirror(left, right)
        else:
            result &= (left == right)
        
        return result
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [10,2,4,6,8,12,14,16,18]]
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

        print('Is tree symmetric: ', 'YES' if a.isSymmetric(x) else 'NO')
