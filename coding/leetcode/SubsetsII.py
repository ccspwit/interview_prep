# -*- coding: utf-8 -*-
"""
Created on June 1 2019
LeetCode problem 90
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
@author: K Li
"""
class Solution(object):
    def subsetsWithDupRecursive(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # recursively build combination
        subsets = [[]]
        seen = set()
        nums.sort()
        for num in nums:
            for i in range(len(subsets)):
                subset = subsets[i] + [num]
                tup = tuple(subset)
                if tup not in seen:
                    seen.add(tup)
                    subsets.append(subset)

        return subsets

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # iteratively compute combination, de-diplicate
        result = [[]]
        ind_comb = []
        N = len(nums)
        sorted_nums = sorted(nums)
        stack = [(0, ind_comb)]
        while stack:
            k, ind_comb = stack.pop()
            val_comb = [sorted_nums[e] for e in ind_comb]
            if k==N:
                continue
            M = len(ind_comb)
            # temp = []
            for v in range(k, N):
                if M==0:
                    new_ind_comb = [v]
                    new_val_comb = [sorted_nums[v]]
                    if new_val_comb not in result:
                        stack.append((k+1, new_ind_comb))
                        result.append(new_val_comb)
                else:
                    if v > ind_comb[-1]:
                        new_ind_comb = ind_comb + [v]
                        new_val_comb = val_comb + [sorted_nums[v]]
                        #print('-'*8, ind_comb, new_ind_comb)
                        if new_val_comb not in result:
                            #print(M, new_val_comb)
                            stack.append((k+1, new_ind_comb))
                            result.append(new_val_comb)
        
        return result
