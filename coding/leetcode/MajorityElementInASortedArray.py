# -*- coding: utf-8 -*-
"""
Created on Feb 22, 2020
LeetCode problem 1150
Given an array nums sorted in non-decreasing order, and a number target, return True if and only if target is a majority element.
A majority element is an element that appears more than N/2 times in an array of length N.

Example 1:
Input: nums = [2,4,5,5,5,5,5,6,6], target = 5
Output: true
Explanation: 
The value 5 appears 5 times and the length of the array is 9.
Thus, 5 is a majority element because 5 > 9/2 is true.

Example 2:
Input: nums = [10,100,101,101], target = 101
Output: false
Explanation: 
The value 101 appears 2 times and the length of the array is 4.
Thus, 101 is not a majority element because 2 > 4/2 is false.

Note:
1 <= nums.length <= 1000
1 <= nums[i] <= 10^9
1 <= target <= 10^9
@author: K Li
"""
class Solution:
    def isMajorityElement1(self, nums: List[int], target: int) -> bool:
        # find left/right boundary using binary search
        N = len(nums)
        #If it is not at the middle then there is no majority element
        mid = N//2        
        if nums[mid] != target:
            return False
        # find left boundary
        low, high = 0, mid
        while low < high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if nums[low] != target:
            return False
        left = low

        # find right boundary
        low, high = mid, N-1
        while low < high:
            mid = (low+high+1)//2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid
        if nums[low] != target:
            return False
        right = high

        return (right-left+1)*2>N

    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # find left/right boundary using binary search
        N = len(nums)
        # find left boundary
        low, high = 0, N-1
        while low < high:
            mid = (low+high)//2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if nums[low] != target:
            return False
        left = low
        # print(f'left={left}', low, high)

        # find right boundary
        low, high = 0, N-1
        while low < high:
            mid = (low+high+1)//2
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid
        if nums[low] != target:
            return False
        right = high
        # print(f'right={right}', low, high) 

        return (right-left+1)*2>N