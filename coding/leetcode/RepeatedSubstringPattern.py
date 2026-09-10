# -*- coding: utf-8 -*-
"""
Created on Sun May 20, 2017
LeetCode problem 459
Given a non-empty string check if it can be constructed by taking a substring
of it and appending multiple copies of the substring together. You may assume
the given string consists of lowercase English letters only and its length
will not exceed 10000.

Example 1:
Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc"
twice.)

@author: K Li
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        Solution with a trick, if s is multiple repeated pattern P.
        Form a new string S1 = s+s, S2=s1[1:-1].
        if s in contained in S2, then s is a repetition of some pattern P
        Note the complexity of string match with KMP algorithm is O(2n)
        for two strings of length n and 2n
        """
        N = len(s)
        if N==0:
            return False
        newS = (s+s)[1:-1]
        return s in newS

    def repeatedSubstringPattern1(self, s):
        """
        :type s: str
        :rtype: bool
        Solution with a trick, if s is multiple repeated pattern P.
        Form a new string S1 = s+s, S2=s1[1:-1].
        if s in contained in S2, then s is a repetition of some pattern P
        Note the complexity of string match with KMP algorithm is O(2n)
        for two strings of length n and 2n
        """
        N = len(s)
        if N==0:
            return False
        n = max(1, N//3)
        newS = (s+s)[n:-n]
        return s in newS
    
if __name__ == '__main__':
    a = Solution()
    testVector = ["","a","aa","ab","abab","abba",
                  "abccbaabc","aabbcaabbc","abcabcabcabc"]
    a = Solution()
    for ind, test in enumerate(testVector):
        print('Test case #',ind+1)
        print(test)
        print(a.repeatedSubstringPattern(test))
        print(a.repeatedSubstringPattern1(test))
        

