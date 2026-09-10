# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 653
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9
Output: True
 
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
@author: K Li
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # travese BST, save visit node values, check if k-cur_val is set
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def traverse(node, k, st):
            if not node:
                return False
            if (k-node.val) in st:
                return True
            st.add(node.val)
            return traverse(node.left, k, st) or traverse(node.right, k, st)
        
        # flatten BST to a list
        store = set()
        return traverse(root, k, store)


    # flatten BST to a list, the check for two sum
    def findTarget1(self, root: TreeNode, k: int) -> bool:
        def traverse(node, st):
            if not node:
                return
            st.append(node.val)
            if node.left:
                traverse(node.left, st)
            if node.right:
                traverse(node.right, st)

        # flatten BST to a list
        store = []
        traverse(root, store)
        if len(store)<2:
            return False
        
        # check for two sum
        diffDict = {k-val:ind for ind,val in enumerate(store)}
        
        for ind, val in enumerate(store):
            if val in diffDict:
                if diffDict[val] != ind:
                    return True
        return False
