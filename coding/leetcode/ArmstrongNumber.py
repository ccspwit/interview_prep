# -*- coding: utf-8 -*-
"""
Created on Feb 22, 2020
LeetCode problem 1134
The k-digit number N is an Armstrong number if and only if the k-th power of each digit sums to N.
Given a positive integer N, return true if and only if it is an Armstrong number.

Example 1:
Input: 153
Output: true
Explanation: 
153 is a 3-digit number, and 153 = 1^3 + 5^3 + 3^3.

Example 2:
Input: 123
Output: false
Explanation: 
123 is a 3-digit number, and 123 != 1^3 + 2^3 + 3^3 = 36.

Note:
1 <= N <= 10^8
@author: K Li
"""
class Solution:
    # from math import ceil, log10
    def isArmstrong1(self, N: int) -> bool:
        cube_sum = 0
        num = N
        digits = []

        while num:
            num, rem = divmod(num, 10)
            digits.append(rem)
        K = len(digits)

        for n in digits:
            cube_sum += n**K
        return cube_sum==N
    
    def isArmstrong(self, N: int) -> bool:
        # use math or str len
        cube_sum = 0
        num = N
        K = len(str(num))

        while num:
            num, rem = divmod(num, 10)
            cube_sum += (rem**K)

        return cube_sum==N
