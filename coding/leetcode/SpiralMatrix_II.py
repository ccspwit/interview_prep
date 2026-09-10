# -*- coding: utf-8 -*-
"""
Created on May 29 2019
LeetCode problem 59
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
@author: K Li
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n<=0:
            return []
        N = n
        matrix = [[0]*N for m in range(N)]
        # values = list(range(1, N*2+1))
        i1, i2 = 0, N
        cur_val = 1
        index_left = N
        
        while index_left > 1:
            # fill top row
            for m in range(i1, i2):
                matrix[i1][m] = cur_val
                cur_val += 1
            # fill right col
            for m in range(i1+1, i2):
                matrix[m][i2-1] = cur_val
                cur_val += 1
            # fill bottom row
            for m in range(i2-2, i1-1, -1):
                matrix[i2-1][m] = cur_val
                cur_val += 1
            # fill left row
            for m in range(i2-2, i1, -1):
                matrix[m][i1] = cur_val
                cur_val +=1
            i1 += 1
            i2 -= 1
            index_left -= 2
        
        if index_left == 1:
            matrix[i1][i1] = cur_val
        
        return matrix
