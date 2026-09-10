# -*- coding: utf-8 -*-
"""
Created on Oct 16th, 2022
LeetCode problem 1143
Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.
Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
@author: K Li
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # tabular dp soluton
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        previous = [0] * (len(text1) + 1)
        for col in reversed(range(len(text2))):
            current = [0] * (len(text1)+1)
            for row in reversed(range(len(text1))):
                if text1[row] == text2[col]:
                    current[row] = previous[row+1]+1
                else:
                    current[row] = max(
                        previous[row], current[row+1]
                    )
            previous = current
        return current[0]
    
    def longestCommonSubsequence2(self, text1: str, text2: str) -> int:
        # recursive dp optimized, divide into 2 sub problems
        # first letters same, first letters dfferent
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if (p1, p2) in cache:
                return cache[(p1, p2)]
            if text1[p1] == text2[p2]:
                result = 1 + dp(p1+1, p2+1)
            else:
                result = max(
                    dp(p1+1, p2), dp(p1, p2+1)
                )
            cache[(p1, p2)] = result
            return result
        
        cache = {}
        return dp(0, 0)        

    def longestCommonSubsequence1(self, text1: str, text2: str) -> int:
        # recursive dp, divide into 2 sub problems
        # text1[i] included and text1[i] not included
        def dp(p1, p2):
            if p1 == len(text1) or p2 == len(text2):
                return 0
            if (p1, p2) in cache:
                return cache[(p1, p2)]
            res1 = dp(p1+1, p2)
            
            first_occurence = text2.find(text1[p1], p2)
            if first_occurence != -1:
                res2 = 1 + dp(p1+1, first_occurence+1)
            else:
                res2 = 0
            result = max(res1, res2)
            cache[(p1, p2)] = result
            return result
        
        cache = {}
        return dp(0, 0)
