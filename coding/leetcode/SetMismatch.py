# -*- coding: utf-8 -*-
"""
Created on July 12, 2019
LeetCode problem 645
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
@author: K Li
"""
class Solution:
    def findErrorNumsDiff(self, nums: List[int]) -> List[int]:
        # computed difference between expected sum and real sum
        N = len(nums)
        e_sum = round(N*(N+1)/2)
        diff = e_sum - sum(nums)
        
        s = set()
        for n in nums:
            if n not in s:
                s.add(n)
            else:
                dup = n
                break
        return [dup, diff+dup]
    
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # use constant space
        
        for val in nums:
            pos = abs(val) - 1
            if nums[pos] < 0:
                dup = abs(val)
            else:
                nums[pos] = -1*nums[pos]
        
        for n, v in enumerate(nums):
            if v > 0:
                miss = n+1
                break
        return [dup, miss]
