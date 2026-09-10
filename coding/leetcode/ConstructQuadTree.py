# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 427
We want to use quad trees to store an N x N boolean grid. Each
cell in the grid can only be true or false. The root node
represents the whole grid. For each node, it will be subdivided
into four children nodes until the values in the region it
represents are all the same.

Each node has another two boolean attributes : isLeaf and val.
isLeaf is true if and only if the node is a leaf node. The val
attribute for a leaf node contains the value of the region it
represents.

Your task is to use a quad tree to represent a given grid.
The following example may help you understand the problem
better:

Given the 8 x 8 grid below, we want to construct the
corresponding quad tree:
It can be divided according to the definition above:

The corresponding quad tree should be as following, where each
node is represented as a (isLeaf, val) pair.

For the non-leaf nodes, val can be arbitrary, so it is
represented as *.
Note:

N is less than 1000 and guaranteened to be a power of 2.
If you want to know more about the quad tree, you can refer to its wiki.
@author: K Li
"""
class Solution(object):
    def create(self, root, grid, tr, tc, size):
        if size == 1:
            return Node(grid[tr][tc], True, None, None, None, None)
        
        k = grid[tr][tc]
        validGrid = True
        for r in range(tr, tr + size):
            for c in range(tc, tc + size):
                if grid[r][c] != k:
                    validGrid = False
                    break
            if not validGrid:
                break
        
        if validGrid:
            return Node(grid[tr][tc], True)
        else:
            root = Node(None, False)
        
        h = size / 2
        root.topLeft     = self.create(None, grid, tr, tc, h)
        root.topRight    = self.create(None, grid, tr, tc + h, h)
        root.bottomLeft  = self.create(None, grid, tr + h, tc, h)
        root.bottomRight = self.create(None, grid, tr + h, tc + h, h)
        
        return root
        
    
    def construct(self, grid):
        # recursively create quadTree
        return self.create(None, grid, 0, 0, len(grid))
