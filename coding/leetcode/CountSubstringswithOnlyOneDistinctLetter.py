# -*- coding: utf-8 -*-
"""
Created on Feb 21, 2020
LeetCode problem 1180
Given a string S, return the number of substrings that have only one distinct letter.

Example 1:
Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

Example 2:
Input: S = "aaaaaaaaaa"
Output: 55

Constraints:
1 <= S.length <= 1000
S[i] consists of only lowercase English letters.
@author: K Li
"""
class Solution:
    def countLetters(self, S: str) -> int:
        # directly add cumsum, no division needed
        same = S[0]
        streak = 1
        res = 1
        for i in range(1, len(S)):
            if S[i] == same:
                streak += 1
            else:
                same = S[i]
                streak = 1
            res += streak
        return res

    def countLetters1(self, S: str) -> int:
        # count consecutive ch, use n*(n+1)/2
        total = 0
        pre, n = '', 0
        for c in S:
            if c != pre:
                total += (n+1)*n//2
                pre = c
                n = 1
            else:
                n += 1
        total += (n+1)*n//2
        return total
