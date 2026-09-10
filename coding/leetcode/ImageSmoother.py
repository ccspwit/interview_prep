# -*- coding: utf-8 -*-
"""
Created on July 12, 2019
LeetCode problem 661
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
@author: K Li
"""
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:

        R, C = len(M), len(M[0])
        # possible surrounding indexes
        indices = [(-1,-1), (-1,0), (-1,1),
                    (0,-1),(0,1),
                    (1,-1), (1,0), (1,1)]
        ans = [[0 for c in range(C)] for r in range(R)]
        for r in range(R):
            for c in range(C):
                total, count = M[r][c], 1
                # iterate over valid indexes
                for ind in indices:
                    r1, c1 = r+ind[0], c+ind[1]
                    if 0<=r1<R and 0<=c1<C:
                        total += M[r1][c1]
                        count += 1
                    
                ans[r][c]  = total//count
        
        return ans
