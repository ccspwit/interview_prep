# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 617
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.
Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
 
Note: The merging process must start from the root nodes of both trees.
@author: K Li
"""
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        # use ir-order traverse
        def inOrderTraverse(n1, n2):
            n1.val = n1.val + n2.val

            # left
            if n1.left and n2.left:
                inOrderTraverse(n1.left, n2.left)
            elif n1.left is None:
                n1.left = n2.left
            elif n2.left is None:
                pass
            # right
            if n1.right and n2.right:
                inOrderTraverse(n1.right, n2.right)
            elif n1.right is None:
                n1.right = n2.right
            elif n2.right is None:
                pass
            return
        
        if t1 is None:
            return t2
        if t2 is None:
            return t1
        inOrderTraverse(t1, t2)
        return t1
