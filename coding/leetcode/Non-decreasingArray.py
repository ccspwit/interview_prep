# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 665
Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.
Note: The n belongs to [1, 10,000].
@author: K Li
"""
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        N = len(nums)
        if N<=2:
            return True
        minus2, minus1 = 0, 0
        if nums[1] < nums[0]:
            minus1 = 1
        for n in range(2, N):
            if nums[n] < nums[n-1]:
                minus1 += 1
                if minus1 > 1:
                    return False
            if nums[n] < nums[n-2]:
                minus2 += 1
                if minus2 > 1:
                    return False
        return True
