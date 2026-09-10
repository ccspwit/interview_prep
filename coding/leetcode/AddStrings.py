# -*- coding: utf-8 -*-
"""
Created on Sun May 18, 2017
LeetCode problem 415
Given two non-negative integers num1 and num2 represented as string, return
the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to
integer directly.
@author: K Li
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        N1, N2 = len(num1), len(num2)
        if N1>N2:
            N1, N2 = N2, N1
            num1, num2 = num2, num1
        n1, n2 = num1[::-1], num2[::-1]
        carry = 0
        sumStr = ""
        for n in range(N1):
            theSum = int(n1[n])+int(n2[n])+carry
            if theSum>=10:
                theSum -= 10
                carry = 1
            else:
                carry = 0
            sumStr += str(theSum)

        for n in range(N1,N2):
            theSum = int(n2[n])+carry
            if theSum>=10:
                theSum -= 10
                carry = 1
            else:
                carry = 0
            sumStr += str(theSum)
        if carry:
            sumStr += '1'
        return sumStr[::-1]
            
if __name__ == '__main__':
    a = Solution()
    testVector = [("", ""), ("0", "0"),
                  ("12345", "54321"),("11", "223344"),
                  ("999","2"),
                  ("98765432123456789","55555555555555555")]
    a = Solution()
    for test in testVector:
        print(test[0], test[1])
        print(a.addStrings(test[0],test[1]))
