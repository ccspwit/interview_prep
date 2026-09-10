# -*- coding: utf-8 -*-
"""
Created on Mon May 8, 2017
LeetCode problem 74

Write an efficient algorithm that searches for a value in an m x n matrix.
This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:
[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        N = len(matrix)
        if (N==0):
            return False
        M = len(matrix[0])
        if (M==0):
            return False
        found  = False
        
        rowl, rowh = 0, N-1
        coll, colh = 0, M-1
        # row first search
        while rowl < rowh:
            midrow = (rowl+rowh)//2
            if target<matrix[midrow][0]:
                rowh = midrow-1
            elif target>matrix[midrow][M-1]:
                rowl = midrow+1
            else:
                break
        if rowl == rowh:
            midrow = rowh

        while coll<colh:
            midcol = (coll+colh)//2
            if target<matrix[midrow][midcol]:
                colh = midcol-1
            elif target>matrix[midrow][midcol]:
                coll = midcol+1
            else:
                return True
        if coll == colh:
            midcol = colh
        #print(rowl, rowh, coll, colh)
        return target == matrix[midrow][midcol]
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [ ([[1, 3, 5, 7],
                    [10, 11, 16, 20], 
                    [23, 30, 34, 50]], 50),
    ([[1]],1),([[1]],2)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        y = a.searchMatrix(test[0], test[1])
        print('Whether 2D Matrix contains %d is '%test[1], y)
    #test = sorted(random.randint(0,100,100))
