# -*- coding: utf-8 -*-
"""
Created on June 2nd, 2017
LeetCode problem 311
Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

A = [[ 1, 0, 0],
  [-1, 0, 3]]
B = [[ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]]

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
@author: K Li
"""

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        Use 1 hash map for A, which is equivalent to iterate over elements of
        A and compute multiplication for one-zero elements of A
        """
        if len(A)==0 or len(B)==0:
            return 0
        N, M, L = len(A), len(A[0]), len(B[0])
        smatA = {}
        for r in range(N):
            for c in range(M):
                val = A[r][c]
                if val != 0:
                    smatA[(r,c)] = val

        result = [[0 for l in range(L)] for n in range(N)]
        
        for r, c in smatA:
            valA = smatA[(r,c)]
            for l in range(L):
                result[r][l] += valA*B[c][l]
        return result

    def multiply1(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        Direct multiplication, do multiplication only if A[r][c]!=0
        """
        if len(A)==0 or len(B)==0:
            return 0
        N, M, L = len(A), len(A[0]), len(B[0])
        result = [[0 for l in range(L)] for n in range(N)]
        # Not normal order of multiplication
        for r in range(N):
            for c in range(M):
                val = A[r][c]
                if val != 0:
                    for l in range(L):
                        result[r][l] += val*B[c][l]
        return result
   
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [([[1,0,0],[-1,0,3]],
                  [[7,0,0],[0,0,0],[0,0,1]])]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('A*B is ',a.multiply(test[0],test[1]))
    t = list(range(1,1000))
    t[100] = 999