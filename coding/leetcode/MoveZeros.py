# -*- coding: utf-8 -*-
"""
Created on May 15th, 2017
LeetCode problem 283
Given an array nums, write a function to move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums
should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
@author: K Li
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        for loop, which is slightly more efficient than while loop
        """
        N = len(nums)
        nonZero = 0
        for n in range(N):
            if nums[n]!=0:
                nums[nonZero] = nums[n]
                nonZero += 1
        while nonZero<N:
            nums[nonZero] = 0
            nonZero += 1
        return

    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        while loop, use right pointer to skip '0' elements
        """
        N = len(nums)
        nZeros = 0
        left, right = 0, 0
        while right<N:
            while (nums[right] == 0):
                right += 1
                if right >= N:
                    break
            if (right<N):
                nums[left] = nums[right]
                left += 1
                right += 1
            #print(left, right, nZeros)
        while left<N:
            nums[left] = 0
            left += 1
        return
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[0],[1],[0,0,0],
                  [1,2,3,4,5],[5,4,0,1,2],
                  [0,1,2,3,4,5,6,0],
                  [1,2,3,4,5,6,7,8,9,0],
                  [0,0,1,2,3,4,5,0,0,6,0,0]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print('Before... ',test)
        a.moveZeroes(test)
        print('After... ',test)

