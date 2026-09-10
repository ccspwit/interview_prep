# -*- coding: utf-8 -*-
"""
Created on May 17th, 2017
LeetCode problem 405
Given an integer, write an algorithm to convert it to hexadecimal. For
negative integer, two’s complement method is used.

Note:

All letters in hexadecimal (a-f) must be in lowercase.
The hexadecimal string must not contain extra leading 0s. If the number is
zero, it is represented by a single zero character '0'; otherwise, the
first character in the hexadecimal string will not be the zero character.
The given number is guaranteed to fit within the range of a 32-bit signed
integer.

You must not use any method provided by the library which converts/formats
the number to hex directly.

Example 1:
Input:
26
Output:
"1a"

Example 2:
Input:
-1
Output:
"ffffffff"
@author: K Li
"""

class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        Use list to store hex mapping
        """
        hexMap = "0123456789abcdef"
        if num==0:
            return "0"
        # truncate for underflow and overflow
        """if num>=2**31:
            num = 2**31-1
        if num<-2**31:
            num = -2**31"""
        if num<0:
            num = 2**32+num
        result = ''
        while num>0:
            digit = num&0xf
            num = num>>4
            result += hexMap[digit]
        return result[::-1]

    def toHex1(self, num):
        """
        :type num: int
        :rtype: str
        Use dict to store hext mapping, compute hexMap each time toHex is called.
        Wasted computation.
        """
        hexMap = {n:hex(n)[2:] for n in range(16)}
        if num==0:
            return "0"
        # truncate for underflow and overflow
        if num>=2**31:
            num = 2**31-1
        if num<-2**31:
            num = -2**31
        if num<0:
            num = 2**32+num
        result = ''
        while num>0:
            digit = num&0xf
            num = num>>4
            result += hexMap[digit]
        return result[::-1]
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [0,1,5,10,17,2147483647,
                  -1,-2,-2147483647]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test, a.toHex(test))
        

