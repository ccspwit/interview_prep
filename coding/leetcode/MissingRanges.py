# -*- coding: utf-8 -*-
"""
Created on Feb 24, 2020
LeetCode problem 163
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

Example:
Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
@author: K Li
"""
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        ans = []
        # handle empty nums case
        if not nums:
            nums = [upper+1]
        # check lower bound
        if lower < nums[0]-1:
            ans.append(f"{lower}->{nums[0]-1}")
        elif lower == nums[0]-1:
            ans.append(f"{lower}")

        # loop over array
        for n in range(1, len(nums)):
            if nums[n] == nums[n-1]+2:
                ans.append(f"{nums[n]-1}")
            elif nums[n] > nums[n-1]+2:
                ans.append(f"{nums[n-1]+1}->{nums[n]-1}")

        # check upper bound
        if upper == nums[-1]+1:
            ans.append(f"{upper}")
        elif upper > nums[-1]+1:
            ans.append(f"{nums[-1]+1}->{upper}")
        return ans
