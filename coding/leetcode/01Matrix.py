# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 542
iven a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.

The distance between two adjacent cells is 1.
Example 1: 
Input:
0 0 0
0 1 0
0 0 0
Output:
0 0 0
0 1 0
0 0 0

Example 2: 
Input:
0 0 0
0 1 0
1 1 1
Output:
0 0 0
0 1 0
1 2 1
Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
@author: K Li
"""

class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        BFS search
        """
        from collections import deque
        
        N = len(matrix)
        if N==0:
            return matrix
        M = len(matrix[0])
        if M==0:
            return matrix
        MAX_VAL = 1000000000
        #dist = [[MAX_VAL for _ in range(M)] for _ in range(N)]
        Q = deque()
        neighbors = [(0,-1),(0,1),(-1,0),(1,0)]

        for n in range(N):
            for m in range(M):
                if matrix[n][m] == 0:
                    #dist[n][m] = 0
                    Q.append((n,m))
                else:
                    matrix[n][m] = -1

        while Q:
            i, j = Q.popleft()
            for di, dj in neighbors:
                ni, nj = i+di, j+dj
                #print(ni,nj)
                if (0<=ni<N) and (0<=nj<M):
                    if matrix[ni][nj] == -1:
                        matrix[ni][nj] = matrix[i][j]+1
                        Q.append((ni,nj))
        return matrix

    def updateMatrix1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        DP solution, 2-pass traversal
        """
        N = len(matrix)
        if N==0:
            return matrix
        M = len(matrix[0])
        if M==0:
            return matrix
        MAX_VAL = 1000000000
        dist = [[MAX_VAL for _ in range(M)] for _ in range(N)]
        
        for n in range(N):
            for m in range(M):
                if matrix[n][m]!=0:
                    if n>0:
                        dist[n][m] = min(dist[n][m], dist[n-1][m]+1)
                    if m>0:
                        dist[n][m] = min(dist[n][m], dist[n][m-1]+1)
                else:
                    dist[n][m] = 0
    
        for n in range(N-1,-1,-1):
            for m in range(M-1,-1,-1):
                if matrix[n][m]!=0:
                    if n<N-1:
                        dist[n][m] = min(dist[n][m], dist[n+1][m]+1)
                    if m<M-1:
                        dist[n][m] = min(dist[n][m], dist[n][m+1]+1)
                else:
                    dist[n][m] = 0
        return dist
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[[0]],[[1]],
                  [[0,0,0],[0,1,0],[0,0,0]],
                  [[0,0,0],[0,1,0],[1,1,1]]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Least number of bricks to cross ',a.updateMatrix(test))
        print(test)
        print('Least number of bricks to cross ',a.updateMatrix1(test))
    t = list(range(1,1000))
    t[100] = 999