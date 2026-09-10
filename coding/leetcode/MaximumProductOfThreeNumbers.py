# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 628
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24

Note:

The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
@author: K Li
"""
class Solution(object):
    def maximumProduct(self, nums: List[int]) -> int:
        # using heap
        # complexity O(nlog(k)), space(k)
        import heapq
        little_2 = heapq.nsmallest(2, nums)
        big_3 = heapq.nlargest(3, nums)
        
        prod1 = little_2[0]*little_2[1]*big_3[0]
        prod2 = big_3[0]*big_3[1]*big_3[2]
        return max(prod1, prod2)
    
    def maximumProduct1(self, nums: List[int]) -> int:
        # compare with min1, min2, max1, max2, max3
        min_val, max_val = -1*(2**31), (2**31)-1
        min1, min2 = max_val, max_val
        max1, max2, max3 = min_val, min_val, min_val
        
        for val in nums:
            if val < min1:
                min2 = min1
                min1 = val
            elif val < min2:
                 min2 = val
            
            if val > max1:
                max3 = max2
                max2 = max1
                max1 = val
            elif val > max2:
                max3 = max2
                max2 = val
            elif val > max3:
                max3 = val

        return max(min1*min2*max1, max1*max2*max3)
