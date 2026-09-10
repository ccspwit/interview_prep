# -*- coding: utf-8 -*-
"""
Created on Thu May 4 2017
Leetcode 125
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
@author: K Li
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        Sliding windows method.
        Check to see whether a character is alphanumeric or not. Use .isalnum()
        If not, skip.
        """
        N = len(s)
        if N<=1:
            return True
        left, right = 0, N-1
        s = s.lower()
        result = True
        
        while left<right:
            lChar, rChar = s[left], s[right]
            if lChar.isalnum() and rChar.isalnum():
                if lChar == rChar:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if not lChar.isalnum():
                    left += 1
                if not rChar.isalnum():
                    right -= 1
                
        return result

    def isPalindrome1(self, s):
        """
        :type s: str
        :rtype: bool
        Sliding windows method.
        Check to see whether a character is alphanumeric or not. Use set
        If not, skip.
        """
        N = len(s)
        if N<=1:
            return True
        left, right = 0, N-1
        s = s.lower()
        result = True
        
        alphanumericSet = set('abcdefghijklmnopqrstuvwxyz0123456789')
        while left<right:
            lChar, rChar = s[left], s[right]
            if (lChar in alphanumericSet) and (rChar in alphanumericSet):
                if lChar == rChar:
                    left += 1
                    right -= 1
                else:
                    return False
            else:
                if lChar not in alphanumericSet:
                    left += 1
                if rChar not in alphanumericSet:
                    right -= 1
                
        return result

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = ["", ".", "1", "aa  ","...",
                  "radar","r a---dar",
                  "A man, a plan, a canal: Panama",
                  "race a car"]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Is it palindrome? ', 'YES' if a.isPalindrome(test) else 'NO')
        print('Is it palindrome? ', 'YES' if a.isPalindrome1(test) else 'NO')
