# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 2017
LeetCode problem 1
Given an array of integers, return indices of the two numbers such that
they add up to a specific target. You may assume that each input would
have exactly one solution, and you may not use the same element twice.
@author: K Li
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        Create a dictionary (hash table) that has
        key: value --- target-num[i], i
        Lookup whether whether num[i] = target-num[i] take O(1) time.
        Complexity: O(n)
        Space: O(n)
        """
        if len(nums) <= 1:
            return False
        diffDict = {}
        for i in range(len(nums)):
            diffDict[target-nums[i]] = i
        for j in range(len(nums)):
            if nums[j] in diffDict:
                if(j!=diffDict[nums[j]]):
                    return [j, diffDict[nums[j]]]
        return False

    def twoSum_Old(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Complexity: O(n^2) 
        Space: O(1)
        """
        
        N = len(nums)
        findMatch = False
        for i in range(N):
            for j in range(i+1,N):
                if (nums[i]+nums[j]) == target:
                    findMatch = True
                    ret = [i,j]
        if(findMatch):
            print('Find matching two sum.')
            return ret
        else:
            print('Not match two sum found!')
            return None
    
    def twoSumFast(self, nums, target):
        """
        Create a dictionary (hash table) that has
        key: value --- target-num[i], i
        Lookup whether whether num[i] = target-num[i] take O(1) time.
        Complexity: O(n)
        Space: O(n)
        """
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__ == "__main__":
    nums = list(range(0,25196+1,2))
    target = 16021