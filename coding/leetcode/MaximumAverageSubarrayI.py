# -*- coding: utf-8 -*-
"""
Created on July 12, 2019
LeetCode problem 645
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
 
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].
@author: K Li
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
        if k == 1: return max(nums)
        if k == N: return sum(nums)/N
        max_sum = sum(nums[:k])
        cur_sum = max_sum
        for n in range(N-k):
            cur_sum += nums[k+n]
            cur_sum -= nums[n]
            # print(max_sum, cur_sum)
            max_sum = max(max_sum, cur_sum)
        return max_sum/k
