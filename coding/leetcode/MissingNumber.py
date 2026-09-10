# -*- coding: utf-8 -*-
"""
Created on May 15th, 2017
LeetCode problem 268
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n,
find the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you implement
it using only constant extra space complexity?
@author: K Li
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N= len(nums)
        if N==0:
            return 0
        expectedSum = (N+1)*N//2
        return expectedSum-sum(nums)
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[0],[1,2,3,4,5],
                  [5,4,0,1,2],
                  [2,3,4,5,6,8,9,1,0]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Missing number is ', a.missingNumber(test))

