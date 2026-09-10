# -*- coding: utf-8 -*-
"""
Created on May 31, 2017
LeetCode problem 276
There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence
posts have the same color. Therefore RRB is a valid combination

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.
@author: K Li
"""

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        DP solution
        """
        if (n==0) or (k==0):
            return 0
        if n<=2:
            return k**n
        #if k==1: return 0
        # first post is k
        # second post
        prev1 = k*(k-1)  # last 2 posts with different color
        prev2 = k     # last 2 posts with same color
        for i in range(2,n):
            prev1, prev2 = prev1*(k-1) + prev2*(k-1), prev1
        return prev1+prev2

if __name__ == '__main__':
    a = Solution()
    testVector = [(0,0),(2,0),(0,2),(1,3),(3,1),
                  (2,2),(3,2),(3,3),(5,3)]
    for test in testVector:
        print(test)
        print("Total number of ways to paint fence: ", a.numWays(test[0], test[1]))

