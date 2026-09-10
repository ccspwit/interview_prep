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
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        for n in range(1, int((c**0.5)+1)):
            rem = c-n*n
            sqrt_rem = round(rem**0.5)
            if sqrt_rem*sqrt_rem == rem:
                return True
        return False