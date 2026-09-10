# -*- coding: utf-8 -*-
"""
Created on May 14th, 2017
LeetCode problem 231
Given an integer, write a function to determine if it is a power of two.
@author: K Li
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n<2**31:
            return (n&(n-1)==0)
        else:
            return False

    def isPowerOfTwo1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        oneBits = 0
        bits = 31
        while (n>0) and (bits>0):
            oneBits += n&1
            n = n>>1
            bits -= 1
        return oneBits==1
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [0,1,2,3,4,2**30,2**30-1, 2**31-1, 2**31, 2**32]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Is power of 2? ',a.isPowerOfTwo(test))
        print('Is power of 2? ',a.isPowerOfTwo1(test))
