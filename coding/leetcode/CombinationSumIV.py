# -*- coding: utf-8 -*-
"""
Created on Oct 16th, 2022
LeetCode problem 377
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:
Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:
Input: nums = [9], target = 3
Output: 0

Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000

Follow up: What if negative numbers are allowed in the given array? How does it change the problem? What limitation we need to add to the question to allow negative numbers?
@author: K Li
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # dp with iteration
        dp = [0] * (target + 1)
        dp[0] = 1

        for comb_sum in range(1, target+1):
            for num in nums:
                if comb_sum - num >= 0:
                    dp[comb_sum] += dp[comb_sum-num]
        
        return dp[-1]

    def combinationSum4_recursive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def dp(nums, target):
            # dp with recursion
            if target <= 0 or len(nums)==0:
                return 0

            if target in cache:
                return cache[target]
            count = 0
            for ind in range(len(nums)):
                if nums[ind] == target:
                    count += 1
                else:
                    count += dp(nums, target-nums[ind])
            cache[target] = count
            return count
        
        cache = {}
        total_count = dp(nums, target)
        return total_count
