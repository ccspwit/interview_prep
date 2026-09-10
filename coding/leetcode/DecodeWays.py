# -*- coding: utf-8 -*-
"""
Created on June 1 2019
LeetCode problem 91
A message containing letters from A-Z is being encoded to
numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine
the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6),
or "BBF" (2 2 6).
@author: K Li
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        TLE error
        """
        # dynamic programming much faster
        single_alphabet=set(['1','2','3','4','5','6','7','8','9'])
        double_alphabet = set(['10','11','12','13','14','15','16','17','18','19',
                 '20','21','22','23','24','25','26'])
        N = len(s)
        if N == 0:
            return 0
        if N == 1:
            if s[0] in single_alphabet:
                return 1
            else:
                return 0
        dp = [0 for e in s]

        # forward compute 
        dp[0] = 1 if s[0] in single_alphabet else 0
        dp[1] = (1 if s[:2] in double_alphabet else 0) + (dp[0] if s[1] in single_alphabet else 0)

        for n in range(2, N):
            dp[n] = dp[n-1] if s[n] in single_alphabet else 0
            dp[n] += dp[n-2] if s[n-1:n+1] in double_alphabet else 0

        return dp[-1]

    def numDecodingsR(self, s):
        """
        :type s: str
        :rtype: int
        TLE error
        """
        def newCombinations(s):
            single_alphabet=set(['1','2','3','4','5','6','7','8','9'])
            double_alphabet = set(['10','11','12','13','14','15','16','17','18','19',
                     '20','21','22','23','24','25','26'])
            N = len(s)
            if N == 0:
                return 1
            if N == 1:
                if s[0] in single_alphabet:
                    return 1
                else:
                    return 0

            n_comb = 0
            if s[0] in single_alphabet:
                n_comb += newCombinations(s[1:])
            if s[:2] in double_alphabet:
                n_comb += newCombinations(s[2:])
            return n_comb                

        return newCombinations(s)