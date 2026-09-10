# -*- coding: utf-8 -*-
"""
Created on Sun May 17, 2017
LeetCode problem 409
Given a string which consists of lowercase or uppercase letters, find the
length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

@author: K Li
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        REALLY REALLY CONCISE
        """
        from collections import Counter
        odds = sum(v & 1 for v in Counter(s).values())
        return len(s) - odds + bool(odds)

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N<=1:
            return N
        charCount = {}
        for ch in s:
            charCount[ch] = charCount.get(ch,0)+1
        oddFlag = 0
        result = 0
        for cnt in charCount.values():
            if cnt>=2:
                result += (cnt//2)*2
            if cnt&1:
                oddFlag = 1
        return result+oddFlag
    
if __name__ == '__main__':
    a = Solution()
    testVector = ["","aa","aAa","leetcode","abccccdd"]
    a = Solution()
    for test in testVector:
        print(test)
        print("%s -- %s"%(test, a.longestPalindrome(test)))
        print("%s -- %s"%(test, a.longestPalindrome1(test)))

