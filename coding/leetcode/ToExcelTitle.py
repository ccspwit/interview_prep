# -*- coding: utf-8 -*-
"""
Created on Sat May 6, 2017
LeetCode problem 168, 171 combined
---#168
Given a positive integer, return its corresponding column title as appear
in an Excel sheet.

For example:
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

---#171
Given a column title as appear in an Excel sheet, return its corresponding
column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
@author: K Li
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N<=0:
            return 0
        s = s.upper()
        Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        alphaDict = {val:ind for ind, val in enumerate(Alphabet)}
        result = alphaDict[s[0]]+1
        #print(result)
        for n in range(1,N):
            ch = s[n]
            result *= 26
            result += alphaDict[ch]+1
            #print(result)
        return result
        
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = n-1
        if (n<0):
            return ""
        base = 26
        Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ''
        while n>=26:
            rem = n % 26
            n = n//26 -1
            #print(chr(A_int+rem))
            result = result+Alphabet[rem]
        #print(chr(A_int+ (n%26)))
        result = result+Alphabet[n]
        return result[::-1]

    def convertToTitle1(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = n-1
        if (n<0):
            return ""
        base = 26
        A_int = ord('A')
        result = ''
        while n>=26:
            rem = n % 26
            n = n//26 -1
            #print(chr(A_int+rem))
            result = result+(chr(A_int+rem))
        #print(chr(A_int+ (n%26)))
        result = result+(chr(A_int+(n%26)))
        return result[::-1]
        
if __name__ == '__main__':
    a = Solution()
    testVector = [1,27,1*26,2*26+1,27*26+1,2*27*26, 26*26*26+26]
                  
    a = Solution()
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        #print(test)
        num = a.convertToTitle(test)
        print("Excel title of {} --> number {}".format(test, num))
        title = a.titleToNumber(num)
        print("number {} --> Excel title is {}".format(num, title))
