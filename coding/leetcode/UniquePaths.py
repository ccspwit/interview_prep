# -*- coding: utf-8 -*-
"""
Created on June 5, 2017
LeetCode problem 62, 63 combined
---#62
A robot is located at the top-left corner of a m x n grid (marked 'Start' in
the diagram below).

The robot can only move either down or right at any point in time. The robot
is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Note: m and n will be at most 100.

---#63
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
@author: K Li
"""

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        Three are total of N=(m+n-2) steps to take. We can either pick m-1
        locations for down steps, the remaining positions for right steps.
        Or the other way around. The result will be C(m-1, N) or C(n-1, N).
        """
        if (m<=0) or (n<=0):
            return 0
        down, right = m-1, n-1
        if (down==0) or (right==0):
            return 1
        N = m+n-2
        K = min(m,n)-1
        num, den = 1, 1
        for i in range(K):
            num *= N-i
            den *= i+1
        return num//den

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        1D DP solution
        """
        if len(obstacleGrid)==0:
            return 0
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for m in range(M+1)]
        
        for n in range(N):
            for m in range(M):
                if obstacleGrid[n][m]==1:
                    dp[m+1] = 0
                else:
                    if (n==0) and (m==0):
                        dp[m+1] = 1
                    #top edge
                    elif n==0:
                        dp[m+1] = dp[m]
                    # middle point
                    else:
                        dp[m+1] = dp[m+1]+dp[m]
        #print(dp)
        return dp[M]
    
    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        2D DP solution
        """
        if len(obstacleGrid)==0:
            return 0
        N, M = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for m in range(M)] for n in range(N)]        
        
        for n in range(N):
            for m in range(M):
                if obstacleGrid[n][m]==1:
                    dp[n][m] = 0
                else:
                    if (n==0) and (m==0):
                        dp[n][m] = 1
                    # left edge
                    elif m==0:
                        dp[n][m] = dp[n-1][m]
                    #top edge
                    elif n==0:
                        dp[n][m] = dp[n][m-1]
                    # middle point
                    else:
                        dp[n][m] = dp[n-1][m]+dp[n][m-1]
        #print(dp)
        return dp[N-1][M-1]
        
if __name__ == '__main__':
    a = Solution()
    testVector = [(1,1),(1,2),(3,3),(7,3),(3,7)]
    for test in testVector:
        print(test)
        print("# of unique paths are: ",(a.uniquePaths(test[0],test[1])))
    
    testVector = [[[0]],[[1]],[[0,0,0],[0,1,0],[0,0,0]],
                  [[0,0,0,0],[0,1,0,0],[0,0,0,0],[0,1,0,0]]]
    for test in testVector:
        print(test)
        print("# of unique paths are: ",(a.uniquePathsWithObstacles(test)))
        print("# of unique paths are: ",(a.uniquePathsWithObstacles1(test)))
