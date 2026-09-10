# -*- coding: utf-8 -*-
"""
Created on May 28, 2017
LeetCode problem 554
There is a brick wall in front of you. The wall is rectangular and has several
rows of bricks. The bricks have the same height but different width. You want
to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of
integers representing the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered
as crossed. You need to find out how to draw the line to cross the least
bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall,
in which case the line will obviously cross no bricks.

Example:
Input: 
[[1,2,2,1],
 [3,1,2],
 [1,3,2],
 [2,4],
 [3,1,2],
 [1,3,1,1]]
Output: 2

Note:
The width sum of bricks in different rows are the same and won't exceed INT_MAX.
The number of bricks in each row is in range [1,10,000]. The height of wall
is in range [1,10,000]. Total number of bricks of the wall won't exceed 20,000.
@author: K Li
"""

class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        Beat 100% python submissions
        Is it because _cumsum was compiled as local?
        """
        csMap, maxGaps = {}, 0
        for row in wall:
            _cumsum = 0
            for brick in row[:-1]:
                _cumsum += brick
                curVal = csMap.get(_cumsum,0)+1
                csMap[_cumsum] = curVal
                if maxGaps<curVal:
                    maxGaps = curVal
        return len(wall) - maxGaps
    
    def leastBricks1(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        csMap = {}
        for row in wall:
            cumsum = 0
            for brick in row[:-1]:
                cumsum += brick
                csMap[cumsum] = csMap.get(cumsum,0)+1
        if csMap:
            return len(wall) - max(csMap.values())
        else:
            return len(wall)
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[[1],[1],[1],[1]],
                  [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]],
                  [[0,0],[1,1],[1,0],[0,1]]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Least number of bricks to cross ',a.leastBricks(test))
        #print('Reshaped maetrix: ',a.matrixReshape1(nums, r, c))

    t = list(range(1,1000))
    t[100] = 999