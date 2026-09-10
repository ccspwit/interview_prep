# -*- coding: utf-8 -*-
"""
Created on May 20, 2017
LeetCode problem 463
You are given a map in form of a two-dimensional integer grid where 1
represents land and 0 represents water. Grid cells are connected
horizontally/vertically (not diagonally). The grid is completely surrounded
by water, and there is exactly one island (i.e., one or more connected land
cells). The island doesn't have "lakes" (water inside that isn't connected
to the water around the island). One cell is a square with side length 1.
The grid is rectangular, width and height don't exceed 100. Determine the
perimeter of the island.

Example:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]
Answer: 16

@author: K Li
"""

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        We can count all 1 in the grid (cnt), and then find all continuous
        one in x axis and y axis (dec). The perimeter is just 4cnt - 2dec.
        which is more efficient is grid is sparse
        """
        if not grid:
            return 0
        width = len(grid[0])
        height = len(grid)
        cnt = 0
        dec = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    cnt += 1
                    if j != width - 1 and grid[i][j+1] == 1:
                        dec += 1    #continuous 1 in x axis
                    if i != height -1 and grid[i+1][j] == 1:
                        dec += 1    #continuous 1 in y axis
        return 4*cnt - 2*dec
    
    def islandPerimeter1(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        For row edge count:
            fist non empty row, for each 1, add 2 row edge counts
            following row, if jth column of last row is '0', add 2
            otherwise, add 0
        For edge count:
            count disjoint segment of '1's, for each segment, add 2
        Inefficient if grid is sparse
        """
        N = len(grid)
        if N == 0:
            return 0
        M = len(grid[0])

        lastRow = [0 for i in range(M)]
        perimeter = 0
        #firstRow = 0
        for i in range(N):
            emptyRow = True
            colSegmentStart = 0
            for j in range(M):
                if grid[i][j]==1:
                    perimeter += 0 if (lastRow[j]) else 2
                    lastRow[j] = grid[i][j]
                    emptyRow = False
                    if colSegmentStart==0:
                        perimeter += 2
                        colSegmentStart = 1
                else:
                    lastRow[j] = grid[i][j]
                    if colSegmentStart==1:
                        colSegmentStart = 0
            """if not emptyRow:
                perimeter += 2"""
                    
        return perimeter

    def islandPerimeter2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Each island cell contribute 4 perimeter, but will subtract 1 whenever
        it sees a shared edge with another island.
        not very efficient
        """
        r = len(grid)
        if r == 0:
            return 0
        c=len(grid[0])

        l=0
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    l+=4
                    if i<r-1 and grid[i+1][j]==1:
                        l-=1
                    if j<c-1 and grid[i][j+1]==1:
                        l-=1
                    if i>0 and grid[i-1][j]==1:
                        l-=1
                    if j>0 and grid[i][j-1]==1:
                        l-=1
        return l

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[],[[1]],[[1,1,1],[1,0,1]],
                  [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]],
                  [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]],
                  [[0,0,0,0],[0,0,0,0],[0,1,0,0],[0,0,0,0]],
                  [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]],
                  [[1,1,1,1],[1,0,0,1],[1,1,1,1],[0,1,0,1],[0,1,1,0]]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Number of boomerangs is: ',a.islandPerimeter(test))
        print('Number of boomerangs is: ',a.islandPerimeter1(test))

    t = list(range(1,1000))
    t[100] = 999