# -*- coding: utf-8 -*-
"""
Created on May 23rd, 2017
LeetCode problem 504
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"
Note: The input will be in range of [-1e7, 1e7].
@author: K Li
"""

class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num>10**7)|(num<-1e7):
            raise ValueError("Value %d is out of range"%num)
        if num == 0:
            return '0'
        save = num
        if num<0:
            num = -1*num
        result = ""
        while num>0:
            result = str(num%7)+result
            num = num//7
        
        return result if save>0 else '-'+result

    def convertToBase71(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num>10**7)|(num<-1e7):
            raise ValueError("Value %d is out of range"%num)
        if num == 0:
            return '0'
        sign = 1
        if num<0:
            sign = -1
            num = -1*num
        result = ""
        while num>0:
            result += str(num%7)
            num = num//7
        result = result[::-1]
        if sign == -1:
            result = '-'+result
        return result
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [0,1,6,7,10,15,10000000,
                  -1,-2,-6,-7,-10000000]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test, a.convertToBase7(test))
        

