# -*- coding: utf-8 -*-
"""
Created on May 20, 2017
LeetCode problem 476
Given a positive integer, output its complement number. The complement
strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed
integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits),
and its complement is 0. So you need to output 0.
@author: K Li
"""

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        1. determine the highest bits (MSB), for example, bit m<31
        2. 2**m-1-num
        """
        if num==0:
            return 1

        bitScale = 1
        while num>=bitScale:
            bitScale <<= 1
        return bitScale-1-num

    def findComplement1(self, num):
        """
        :type num: int
        :rtype: int
        1. determine the highest bits (MSB), for example, bit m<31
        2. then XOR with 2**m-1
        """
        if (num<0) & (num>=2**31):
            raise ValueError("Value out of range. 0<x<2**31")
        if num==0:
            return 1
        MASK = 0
        bitScale = 1
        while num>=bitScale:
            MASK = MASK | bitScale
            bitScale <<= 1
        return num^MASK
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [0,1,5,8,55,100,1000]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test, a.findComplement(test))
        print(test, a.findComplement1(test))
        

