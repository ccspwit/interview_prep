# -*- coding: utf-8 -*-
"""
Created on May 15th, 2017
LeetCode problem 258
Given a non-negative integer num, repeatedly add all its digits until the
result has only one digit.

For example:

Given num = 38, the process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only
one digit, return it.

Follow up:
Could you do it without any loop/recursion in O(1) runtime?
@author: K Li
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #result = 0
        while num>=10:
            num = sum([int(x) for x in str(num)])
        return num

    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        return num%9 if num%9!=0 else 9
         
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [0,1,2,38,238,2**31-1, 2**31]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Adding digits in %d is %d '%(test,a.addDigits(test)))
        print('Adding digits in %d is %d '%(test,a.addDigits1(test)))
