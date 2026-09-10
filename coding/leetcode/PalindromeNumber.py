# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 2017
LeetCode problem 9
Determine whether an integer is a palindrome. Do this without extra space.

The input is assumed to be a 32-bit signed integer. Your function should
return 0 when the reversed integer overflows.
@author: K Li
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if(x<0):
            return False
        if(x<10):
            return True
        
        maxScale = 10
        while x > (maxScale*10):
            maxScale *= 10

        retVal = True
        while x>0:
            MSB = x // maxScale
            LSB = x % 10
            if (MSB!= LSB):
                retVal = False
                break
            x = (x%maxScale) // 10
            maxScale /= 100

        return retVal

    def isPalindromeInt(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if(x<0):
            return False
        if(x<10):
            return True
        
        nDigits = 2
        MSBscale = 10
        while x>= MSBscale*10:
            nDigits += 1
            MSBscale *= 10
        print(x, nDigits, MSBscale)

        retVal = True
        nCompare = nDigits//2
        x_copy = x
        for _ in range(nCompare):
            MSB = x_copy // MSBscale
            LSB = x % 10
            if (MSB!= LSB):
                retVal = False
                break
            x = x//10
            x_copy = x_copy % MSBscale
            MSBscale = MSBscale // 10
        
        return retVal

    def isPalindromeStr(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if(x<0):
            return False
        if(x<10):
            return True
        
        s = str(x)
        N = len(s)
        retVal = True
        for i in range(N//2):
            if s[i]!=s[N-i-1]:
                retVal = False
                break

        return retVal

if __name__ == '__main__':
    a = Solution()
    testVector = [
            5,-5,10,22,10000,11111,12344321,12321,100021]
    for test in testVector:
        print('original=%d, Palindrome? %s' %(test, a.isPalindrome(test)))
        print('original=%d, Palindrome? %s' %(test, a.isPalindromeStr(test)))
    
