# -*- coding: utf-8 -*-
"""
Created on May 15th, 2017
LeetCode problem 263
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.
For example, 6, 8 are ugly while 14 is not ugly since it includes another
prime factor 7.

Note that 1 is typically treated as an ugly number.
@author: K Li
"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num>=(2**31):
            return False
        for x in [2,3,5]:
            while (num%x) == 0:
                num = num//x
        return num==1
    
    def isUgly1(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num==1:
            return True
        if num>=(2**31):
            return False
        while num>1:
            if num%2 == 0:
                num = num//2
            elif num%3 == 0:
                num = num//3
            elif num%5 ==0:
                num = num //5
            else:
                return False
            #print(num)
        return num==1
         
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [0,1,4,5,30,100,238,2**30,2**31-2, 2**31,
                  (2**3)*(3**5)*(5**2),849904, 218081, 302085]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Adding digits in %d is %s '%(test,a.isUgly(test)))
        print('Adding digits in %d is %s '%(test,a.isUgly1(test)))
