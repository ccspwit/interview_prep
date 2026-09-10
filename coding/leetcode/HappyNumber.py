# -*- coding: utf-8 -*-
"""
Created on Sat May 6, 2017
LeetCode problem 202
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process,
Starting with any positive integer, replace the number by the sum of the
squares of its digits, and repeat the process until the number equals 1
(where it will stay), or it loops endlessly in a cycle which does not
include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
@author: K Li
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        Determin if n is a Happy number
        """
        def sumSquare(num):
            """
            Helper function to compute sum of digit square
            """
            result = 0
            while num > 0:
                LSB = num % 10
                num = num//10
                result += LSB**2
            return result
        
        nLoops = 0
        history = {n}
        nextNum = sumSquare(n)
        while nextNum!=1:
            if nextNum in history:
                return False
            else:
                history.add(nextNum)
            nextNum = sumSquare(nextNum)
            nLoops += 1
            if nLoops>100:
                break

        if nextNum == 1:
            return True
        else:
            print('Maximum number of loops %d reached. Not a happy number'%nLoops)
            return False

if __name__ == '__main__':
    a = Solution()
    testVector = [1,5,10,20,30,100,255,1000]
                  
    a = Solution()
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        #print(test)
        print("%d, is %s a happy number"%(test, '' if a.isHappy(test) else 'NOT'))

