# -*- coding: utf-8 -*-
"""
Created on May 31 2019
LeetCode problem 78
Given a set of distinct integers, nums, return all possible subsets
(the power set).
Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
@author: K Li
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = [[]]
        comb = []
        N = len(nums)
        sorted_nums = sorted(nums)
        stack = [(0, comb)]
        while stack:
            k, comb = stack.pop()
            if k==N:
                continue
            M = len(comb)
            for v in range(k, N):
                if M==0:
                    new_comb = [sorted_nums[v]]
                    stack.append((k+1, new_comb))
                    result.append(new_comb)
                else:
                    if sorted_nums[v] > comb[-1]:
                        new_comb = comb + [sorted_nums[v]]
                        stack.append((k+1, new_comb))
                        result.append(new_comb)
        
        return result