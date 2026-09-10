# -*- coding: utf-8 -*-
"""
Created on May 29 2019
LeetCode problem 54
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
@author: K Li
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return matrix
        if len(matrix[0]) == 0:
            return matrix
        
        N, M = len(matrix), len(matrix[0])
        r1, r2 = 0, N
        c1, c2 = 0, M
        dim_left = min(N, M)
        
        result = []
        while dim_left > 1:
            result.extend(matrix[r1][c1:c2])
            cols = [matrix[row][c2-1] for row in range(r1+1, r2)]
            result.extend(cols)
            result.extend(matrix[r2-1][c1:c2-1][::-1])
            cols = [matrix[row][c1] for row in range(r2-2, r1,-1)]
            result.extend(cols)
            
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
            dim_left -= 2
        
        if dim_left == 1:
            if N<=M:
                result.extend(matrix[r1][c1:c2])
            else:
                cols = [matrix[row][c1] for row in range(r1, r2)]
                result.extend(cols)
        
        return result

    def spiralOrder1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return matrix
        if len(matrix[0]) == 0:
            return matrix
        
        N, M = len(matrix), len(matrix[0])
        dim_left = min(N, M)
        
        ring_count = 0
        result = []
        while dim_left > 1:
            result.extend(matrix[ring_count][ring_count:M-ring_count])
            cols = [matrix[row][M-ring_count-1] for row in range(ring_count+1, N-ring_count)]
            result.extend(cols)
            result.extend(matrix[N-ring_count-1][ring_count:M-ring_count-1][::-1])
            cols = [matrix[row][ring_count] for row in range(N-ring_count-2,ring_count,-1)]
            result.extend(cols)
            
            ring_count += 1
            dim_left -= 2
        
        if dim_left == 1:
            if N<=M:
                result.extend(matrix[ring_count][ring_count:M-ring_count])
            else:
                cols = [matrix[row][M-ring_count-1] for row in range(ring_count, N-ring_count)]
                result.extend(cols)
        
        return result
