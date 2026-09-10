# -*- coding: utf-8 -*-
"""
Created on Thu May 1st 2017
LeetCode problem 67
Given two binary strings, return their sum (also a binary string).

For example,
a = "11"
b = "1"
Return "100".

@author: K Li
"""
class Solution(object):
    def addBinary(self, a, b):
        return bin(int(a,2)+int(b,2))[2:]
    
    def addBinary1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        nA, nB = len(a), len(b)
        if(nA<nB):
            a, b = b,a
            nA, nB = nB, nA

        result = 0
        carry = 0
        scale = 1
        
        for n in range(-1, -nA-1,-1):
            if n>=-nB:
                binSum = int(a[n])+int(b[n])+carry
            else:
                binSum = int(a[n])+carry
            if binSum >= 2:
                binSum -= 2
                carry = 1
            else:
                carry = 0
            result += binSum*scale
            scale *= 10
        
        result += carry*scale
        return str(result)

if __name__ == '__main__':
    a = Solution()
    testVector = [["11","11"],["1","0"],
                  ["101","101"]]
    a = Solution()
    for test in testVector:
        print(test)
        print(a.addBinary(test[0], test[1]))
    
    test = np.random.randint(0,20,20)