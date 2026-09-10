# -*- coding: utf-8 -*-
"""
Created on May 17th, 2017
LeetCode problem 400
Find the nth digit of the infinite integer sequence
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n<2**31).

Example 1:
Input:
3
Output:
3

Example 2:
Input:
11
Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
which is part of the number 10.
@author: K Li
"""

class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        Rules are
        1~9         --- 9 one digit
        10~99       --- 90 two digits
        100~999     --- 900 three digits
        More concise
        """
        
        nRange = 9
        digits = 1
        lowBound = 1
        total = 0
        while n > (digits*nRange):
            # go to the next range
            n -= digits*nRange
            digits += 1
            nRange *= 10
            lowBound *= 10

        #decide which number and which digit
        num = lowBound+(n-1)//digits
        bitPos = (n-1) % digits
        return int(str(num)[bitPos])

    def findNthDigit1(self, n):
        """
        :type n: int
        :rtype: int
        Rules are
        1~9         --- 9 one digit
        10~99       --- 90 two digits
        100~999     --- 900 three digits
        """
        
        nRange = 9
        digits = 1
        low, high = 1, 10
        total = 0
        while n > 0:
            if n > (digits*nRange):
                # go to the next range
                n -= digits*nRange
                digits += 1
                nRange *= 10
                low, high = low*10, high*10
            else:
                #decide which number and which digit
                num = low+(n-1)//digits
                bitPos = (n-1) % digits
                return int(str(num)[bitPos])
        return -1
            
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [1,5,6,10,11,13,189,190,191,192,193,
                  2147483647]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test, a.findNthDigit(test))
        print(test, a.findNthDigit1(test))

