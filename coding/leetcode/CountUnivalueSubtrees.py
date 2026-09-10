# -*- coding: utf-8 -*-
"""
Created on Feb 23, 2020
LeetCode problem 250
Given a binary tree, count the number of uni-value subtrees.
A Uni-value subtree means all nodes of the subtree have the same value.

Example :
Input:  root = [5,1,5,5,5,null,5]
              5
             / \
            1   5
           / \   \
          5   5   5
Output: 4
@author: K Li
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees1(self, root):
        self.count = 0
        self.is_valid_part(root, False)
        return self.count

    def is_valid_part(self, node, val):
        # check subtree using parent value
        # considered a valid subtree
        if node is None: return True

        # check if node.left and node.right are univalue subtrees of value node.val
        if not all([self.is_valid_part(node.left, node.val),
                    self.is_valid_part(node.right, node.val)]):
            return False

        # if it passed the last step then this a valid subtree - increment
        self.count += 1

        # at this point we know that this node is a univalue subtree of value node.val
        # pass a boolean indicating if this is a valid subtree for the parent node
        return node.val == val

    def countUnivalSubtrees(self, root: TreeNode) -> int:
        # DFS, my solution
        def dfs(node):
            if not node:
                return False, False
            if node.left is None and node.right is None:
                self.count += 1
                return (True, node.val)
            
            left, right = True, True
            # empty subtree does not impact univalue logic
            if node.left:
                left, left_val = dfs(node.left)
                if left is False or node.val != left_val:
                    left = False                    
            if node.right:
                right, right_val = dfs(node.right)
                if right is False or node.val != right_val:
                    right = False
            # check for valid univalue tree
            if left and right:
                self.count += 1
                return (True, node.val)
            else:
                return (False, False)

        self.count = 0
        dfs(root)
        return self.count
