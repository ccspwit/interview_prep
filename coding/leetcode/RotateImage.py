# -*- coding: utf-8 -*-
"""
Created on May 30, 2017
LeetCode problem 542
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).
Follow up:
Could you do this in-place?
@author: K Li
"""

class Solution(object):
    def rotate(self, mat):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        N = len(mat)
        if N<=1:
            return
        for n in range(N//2):
            # outer ring from 0, to N//2
            for m in range(N-2*n-1):
                # kind like column index
                x1, y1 = n, n+m
                x2, y2 = n+m, N-1-n
                x3, y3 = N-1-n, N-1-n-m
                x4, y4 = N-1-n-m, n
                mat[x1][y1], mat[x2][y2], mat[x3][y3], mat[x4][y4] =\
                mat[x4][y4], mat[x1][y1], mat[x2][y2], mat[x3][y3]
        return
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[[1]],[[1,2,3],[4,5,6],[7,8,9]],
                  [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        a.rotate(test)
        print('Least number of bricks to cross ',test)
    t = list(range(1,1000))
    t[100] = 999