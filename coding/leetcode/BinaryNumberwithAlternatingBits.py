# -*- coding: utf-8 -*-
"""
Created on July 13, 2019
LeetCode problem 693
Given a positive integer, check whether it has alternating bits: namely, if two adjacent bits will always have different values.

Example 1:
Input: 5
Output: True
Explanation:
The binary representation of 5 is: 101
Example 2:
Input: 7
Output: False
Explanation:
The binary representation of 7 is: 111.
Example 3:
Input: 11
Output: False
Explanation:
The binary representation of 11 is: 1011.
Example 4:
Input: 10
Output: True
Explanation:
The binary representation of 10 is: 1010.
@author: K Li
"""
class Solution:
    def hasAlternatingBits1(self, n: int) -> bool:
        # use builtin bin function
        bits = bin(n)[2:]
        status = True
        for n in range(1, len(bits)):
            if bits[n] == bits[n-1]:
                return False
        return True
    
    def hasAlternatingBits2(self, n: int) -> bool:
        # use builtin bin function
        bits = bin(n)[2:]
        if '11' in bits or '00' in bits:
            return False
        else:
            return True

    def hasAlternatingBits(self, n):
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2: return False
            n, cur = divmod(n, 2)
        return True
