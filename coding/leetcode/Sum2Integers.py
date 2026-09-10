# -*- coding: utf-8 -*-
"""
Created on May 16th, 2017
Calculate the sum of two integers a and b, but you are not allowed to use the
operator + and -.

Example:
Given a = 1 and b = 2, return 3.
@author: K Li
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        bit operation, 32-bit signed integer
        """
        
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        MAX32 = 4294967296   #2**32
        
        result = 0
        scale = 1
        carry = 0
        for n in range(32):
            LSB1, LSB2 = a&1, b&1
            if (LSB1 ^ LSB2 ^ carry):
                result = result | scale
            scale  = scale <<1
            carry = (LSB1&LSB2)|(LSB1&carry)|(LSB2&carry)
            a, b = a>>1, b>>1
        if result> MAX:
            result = result - MAX32
        return result 

if __name__ == '__main__':
    import numpy as np
    from numpy.random import randint
	# test case to generate ListNode and run test function
    testVector = [(0,0),(0,2),(1,1),(1,9),
                  (32767,1),(32767,32768),
                  (2147483647,1)]
    testVector = zip(randint(-2**31, 2**31, 100),randint(-2**31, 2**31, 100))
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        #print('Test case %d-----------'%i)
        #print(test)
        output = a.getSum(test[0],test[1])
        if (test[0]+test[1]) != output:
            print('Wrong answer')
            print('\t', test[0],'+',test[1],'!=',output)

