# -*- coding: utf-8 -*-
"""
Created on May 31 2019
LeetCode problem 73
Given a m x n matrix, if an element is 0, set its entire row and
column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best
solution. Could you devise a constant space solution?
@author: K Li
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return matrix
        
        # the idea is to use first row and column to save 0 values
        R, C = len(matrix), len(matrix[0])
        is_col = False
        for r in range(R):
            if matrix[r][0] == 0:
                is_col = True
            for c in range(1, C):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0
                    
        for i in range(1, R):
            for j in range(1, C):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
        
        # see if th first row needs to be se to zero
        if matrix[0][0] == 0:
            for j in range(C):
                matrix[0][j] = 0
        if is_col:
            for i in range(R):
                matrix[i][0] = 0
        return
    
    def setZeroesBF(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # brute force solution
        if not matrix:
            return matrix
        
        M, N = len(matrix), len(matrix[0])
        min_dim = min(M, N)
        
        row_q = set()
        col_q = set()
        
        # scan for zero coordinate
        for row_ind, row in enumerate(matrix):
            for col_ind, ele in enumerate(row):
                if ele == 0:
                    row_q.add(row_ind)
                    col_q.add(col_ind)
        # fill zero values
        for row_ind, row in enumerate(matrix):
            for col_ind, ele in enumerate(row):
                if row_ind in row_q or col_ind in col_q:
                    matrix[row_ind][col_ind] = 0
        
        return