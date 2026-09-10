# -*- coding: utf-8 -*-
"""
Created on May 31, 2017
LeetCode problem 246, 247 combined, 248 is hard
---#246
A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is
represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

---#247
A strobogrammatic number is a number that looks the same when rotated 180
degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
@author: K Li
"""

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        Handle mid point of odd length string within the loop (last loop)
        """
        N = len(num)
        if N==0:
            return True
        snMap = {"0":"0","1":"1","6":"9","8":"8","9":"6"}
        
        for n in range((N+1)//2):
            ch1, ch2 = num[n], num[N-1-n]
            if (ch1 not in snMap) or (ch2!=snMap[ch1]):
                return False

        return True

    def isStrobogrammatic1(self, num):
        """
        :type num: str
        :rtype: bool
        """
        N = len(num)
        if N==0:
            return True
        snMap = {"0":"0","1":"1","8":"8","6":"9","9":"6"}
        for n in range(N//2):
            ch1, ch2 = num[n], num[N-1-n]
            if (ch1 not in snMap) or (ch2!=snMap[ch1]):
                return False
        if N&1:
            #odd number
            ch = num[N//2]
            return (ch in snMap) and (ch == snMap[ch])
        return True

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        

if __name__ == '__main__':
    a = Solution()
    testVector = ["1","2","11","18","69","96",
                  "1818","1881","6969","6996"]
    a = Solution()
    print("Palindrome permutation")
    for test in testVector:
        #print(test)
        print("%s is %s"%(test, a.isStrobogrammatic(test)))
        print("%s is %s"%(test, a.isStrobogrammatic1(test)))
