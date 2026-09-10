# -*- coding: utf-8 -*-
"""
Created on May 25, 2017
LeetCode problem 561
Given an array of 2n integers, your task is to group these integers into n
pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of
min(ai, bi) for all i from 1 to n as large as possible.

Example 1:
Input: [1,4,3,2]

Output: 4
Explanation: n is 2, and the maximum sum of pairs is 4.
Note:
n is a positive integer, which is in the range of [1, 10000].
All the integers in the array will be in the range of [-10000, 10000].
@author: K Li
"""

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if (N&1)!=0:
            raise ValueError("The length of array input must be even number.")
        nums.sort()
        return sum(nums[::2])
    
if __name__ == '__main__':
    import numpy as np
	# test case to generate ListNode and run test function
    testVector = [[],[1,2],[2,1],
                  [1,4,3,2],
                  [10,3,9,4],
                  [8,9,10,1,2,3,4,0]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        test1 = test[:]
        print('Relative ranking is ',a.arrayPairSum(test))

    tc = np.random.randint(1,1000,100)