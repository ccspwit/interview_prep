# -*- coding: utf-8 -*-
"""
Created on June 4, 2017
LeetCode problem 64
Given a m x n grid filled with non-negative numbers, find a path from top
left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
@author: K Li
"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        DP 1D solution.
        O(MN) time, O(M) space
        """
        N, M = len(grid), len(grid[0])
        dp = [0 for m in range(M)]
        dp [M-1] = grid[N-1][M-1]
        
        for row in range(N-1,-1,-1):
            for col in range(M-1,-1,-1):
                if (row==N-1) and (col==M-1):
                    continue
                if row == N-1:
                    dp[col] = grid[row][col]+dp[col+1]
                elif col == M-1:
                    dp[col] = grid[row][col]+dp[col]
                else:
                    dp[col] = min(grid[row][col]+dp[col+1],
                      grid[row][col]+dp[col])
        return dp[0]
    
    def minPathSum1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        DP 2D solution.
        O(MN) time, O(MN) space
        """
        N, M = len(grid), len(grid[0])

        dp = [[0 for m in range(M)] for n in range(N)]
        dp [N-1][M-1] = grid[N-1][M-1]
        for row in range(N-1,-1,-1):
            for col in range(M-1,-1,-1):
                if (row==N-1) and (col==M-1):
                    continue
                if row == N-1:
                    dp[row][col] = grid[row][col]+dp[row][col+1]
                elif col == M-1:
                    dp[row][col] = grid[row][col]+dp[row+1][col]
                else:
                    dp[row][col] = min(grid[row][col]+dp[row][col+1],
                      grid[row][col]+dp[row+1][col])
        return dp[0][0]
    
    def minPathSumTLE(self, grid):
        """
        :type grid: List[List[int]]u
        :rtype: int
        Recursive solution. TLE error
        """
        def nextSum(grid, i, j):
            N, M = len(grid), len(grid[0])
            if (i==N-1) and (j==M-1):
                return grid[i][j]
            if i==N-1:
                return grid[i][j]+nextSum(grid, i, j+1)
            elif j==M-1:
                return grid[i][j]+nextSum(grid, i+1, j)
            else:
                return grid[i][j]+min(nextSum(grid,i+1,j), nextSum(grid, i, j+1))

        N, M = len(grid), len(grid[0])
        minSum = nextSum(grid, 0, 0)
        return minSum
    
if __name__ == '__main__':
    a = Solution()
    testVector = [[[1]],[[1,0],[2,1]],[[9,1,4,8]],
                  [[2,3,1,1,4],[1,4,2,1,3],[0,1,2,3,4],[3,2,0,3,5]]]
    a = Solution()
    for test in testVector:
        print(test)
        print("Minimum path sum is ",(a.minPathSum(test)))
        print("Minimum path sum is ",(a.minPathSum1(test)))
    
    #test = np.random.randint(0,20,20)