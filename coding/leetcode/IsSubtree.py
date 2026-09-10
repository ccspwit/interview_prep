# -*- coding: utf-8 -*-
"""
Created on May 26, 2017
Leetcode 572
Given two non-empty binary trees s and t, check whether tree t has exactly
the same structure and node values with a subtree of s. A subtree of s is a
tree consists of a node in s and all of this node's descendants. The tree s
could also be considered as a subtree of itself.

Example 1:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4 
  / \
 1   2
Return true, because t has the same structure and node values with a subtree of s.

Example 2:
Given tree s:
     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
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
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def isSame(s, t):
            if not (s and t):
                return s==t
            if s.val!=t.val:
                return False
            return isSame(s.left, t.left) and isSame(s.right, t.right)
                    
        if (s is None) and (t is None):
            return True
        if (s is None) or (t is None):
            return False
        if isSame(s,t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSubtree1(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        if (s is None) and (t is None):
            return True
        if (s is None) or (t is None):
            return False
        if self.isSame1(s,t):
            return True
        else:
            if s.left:
                if self.isSubtree1(s.left, t):
                    return True
            """else:
                return False"""

            if s.right:
                if s.right:
                    if self.isSubtree1(s.right, t):
                        return True
                """else:
                    return False"""
        return False

    def isSame1(self, s, t):
        """
        Check if s and t is identical, meaning both structure and values
        are the same
        s, t are TreeNode
        rtype: bool
        """
        if (s is None) and (t is None):
            return True
        if (s is None) or (t is None):
            return False
        if s.val!=t.val:
            return False
        if self.isSame1(s.left, t.left):
            return self.isSame1(s.right, t.right)
        else:
            return False
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([],[]),([1],[]),([],[1]),
                  ([2,2,2,2,2],[2,2,2]),
                  ([5,3,6,2,4,1],[3,2,4,1]),
                  ([5,3,6,2,4,1],[3,2,4]),
                  ([10,6,14,16,2,8,12,18],[8])]
    a = Solution()
    for n, test in enumerate(testVector):
        print('Test case ----- ', n)
        print(test)
        x, y = None, None
        for j in range(len(test[0])):
            if j == 0:
                x = TreeNode(test[0][j])
            else:
                x.addNode(test[0][j])
    
        if x: x.showNode()

        for j in range(len(test[1])):
            if j == 0:
                y = TreeNode(test[1][j])
            else:
                y.addNode(test[1][j])
    
        if y: y.showNode()

        print()
        print(a.isSubtree(x,y))
        print(a.isSubtree1(x,y))
