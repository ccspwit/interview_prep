# -*- coding: utf-8 -*-
"""
Created on May 31, 2017
LeetCode problem 256
There are a row of n houses, each house can be painted with one of the three
colors: red, blue or green. The cost of painting each house with a certain
color is different. You have to paint all the houses such that no two adjacent
houses have the same color.

The cost of painting each house with a certain color is represented by a
n x 3 cost matrix. For example, costs[0][0] is the cost of painting house
0 with color red; costs[1][2] is the cost of painting house 1 with color
green, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.
@author: K Li
"""

class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        N = len(costs)
        if N==0:
            return 0
        if N==1:
            return min(costs[0])
        M0, M1, M2 = costs[0][0], costs[0][1], costs[0][2]
        for n in range(1,N):
            N0 = costs[n][0] + min(M1,M2)
            N1 = costs[n][1] + min(M0,M2)
            N2 = costs[n][2] + min(M0,M1)
            M0, M1, M2 = N0, N1, N2
        return min(M0, M1, M2)
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[[7, 3, 6],[3, 5, 1],[2, 8, 5]],
                  [[4, 7, 5],[5, 8, 9],[6, 1, 2],[6, 7, 2],[2, 8, 4]]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Least number of bricks to cross ',a.minCost(test))
    t = list(range(1,1000))
    t[100] = 999