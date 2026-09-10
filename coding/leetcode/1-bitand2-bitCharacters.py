# -*- coding: utf-8 -*-
"""
Created on Jan 18, 2020
LeetCode problem 717
We have two special characters. The first character can be represented by one bit 0. The second character can be represented by two bits (10 or 11).
Now given a string represented by several bits. Return whether the last character must be a one-bit character or not. The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:
1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
@author: K Li
"""
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # more concise solution
        N = len(bits)
        n = 0
        while n < N-1:
            n += bits[n]+1
        return n==N-1

    def isOneBitCharacter1(self, bits: List[int]) -> bool:
        # my original solution
        N = len(bits)
        n = 0
        while n < N-1:
            if bits[n] == 1:
                n += 2
            else:
                n += 1
        if n == N-1:
            return True
        if n > N-1:
            return False
