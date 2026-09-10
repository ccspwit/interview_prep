# -*- coding: utf-8 -*-
"""
Created on June 9, 2017
LeetCode problem 200
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
@author: K Li
"""

class Solution(object):
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Recursive BFS solution
        """
        def boundary(i, j):
            if (i<0) or (j<0) or i>=len(grid) or j>=len(grid[0]) or self.G[i][j]!="1":
                return
            self.G[i][j] = str(-count)
            boundary(i+1, j)
            boundary(i-1, j)
            boundary(i, j+1)
            boundary(i, j-1)
            return
        
        if not grid:
            return 0
        self.G = [list(s) for s in grid]
        N, M = len(grid), len(grid[0])
        count = 0
        for i in range(N):
            for j in range(M):
                if self.G[i][j] == "1":
                    count += 1
                    boundary(i, j)
        return count
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [["111","010","111"],
                  ["11110","11010","11000","00000"],
                  ["11000","11000","00100","00011"]]
    a = Solution()
    #testVector = [[10,3,4,11,12,13]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print("Number of islands is ",a.numIslands(test))

