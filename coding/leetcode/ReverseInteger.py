# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 2017
LeetCode problem 7
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321
Example2: x = 1200, return 21
The input is assumed to be a 32-bit signed integer. Your function should
return 0 when the reversed integer overflows.
@author: K Li
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # check for validity, polarity, and zero
        if not isinstance(x,int):
            raise ValueError('Input should be of integer time', x)
        if x==0:
            return 0
        negative = False
        if x<0:
            negative = True
            x *= -1
        
        # main body, one liner
        y = int(str(x)[::-1])
        
        # post processing
        if negative:
            y *= -1
        if (y >= 2**31) or (y < -2**31):
            y = 0
        return y

    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        # check for validity, polarity, and zero
        if not isinstance(x,int):
            raise ValueError('Input should be of integer time', x)
        if x==0:
            return 0
        negative = False
        if x<0:
            negative = True
            x *= -1
        
        # main body
        y = 0   # return value
        while x>0:
            tail = x % 10
            x = x//10
            y = y*10
            y += tail
        
        # post processing
        if negative:
            y *= -1
        if (y >= 2**31) or (y < -2**31):
            y = 0
        return y

if __name__ == '__main__':
    a = Solution()
    testVector = [(123, 321), (-123,-321),
                  (100, 1),(-1200,-12),
                  (0,0),(-0,0),
                  (1073741824, 0), (-1073741824, 0)]
    for test in testVector:
        print('original=%d, reversed=%d' %(test[0], a.reverse(test[0])))
    
