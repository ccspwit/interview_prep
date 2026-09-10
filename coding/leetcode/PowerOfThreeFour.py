# -*- coding: utf-8 -*-
"""
Created on May 16th, 2017
LeetCode problem 326, 342 combined
---#326
Given an integer, write a function to determine if it is a power of three.

Follow up:
Could you do it without using any loop / recursion?

---#342
Given an integer (signed 32 bits), write a function to check whether it is
a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
@author: K Li
"""

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n>=2**31:
            return False
        rem = 0
        while (n>1):
            if (n%3)==0:
                n = n//3
            else:
                return False
        return n==1

    def isPowerOfFour(self, n):
        """
        Very concise and computational efficient!!!
        """
        return (n>0) & ((n & (n-1)) == 0) & ((n-1) % 3 == 0)
    
    def isPowerOfFour2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n>=2**31:
            return False
        binNum = bin(n)[2:]
        oneBits = binNum.count('1')
        zeroBits = binNum.count('0')
        return (oneBits==1)&((zeroBits%2)==0)

    def isPowerOfFour1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        if n>=2**31:
            return False
        rem = 0
        while (n>1):
            if (n&3)==0:
                n = n>>2
            else:
                return False
        return n==1
     
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [0,1,2,3,4,8,9,10,
                  2**9,2**10,3**10,3**10-1, 2**30, 2**31]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Is power of 3? ',a.isPowerOfThree(test))
        print('Is power of 4? ',a.isPowerOfFour(test))
