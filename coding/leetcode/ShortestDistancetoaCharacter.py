# -*- coding: utf-8 -*-
"""
Created on Nov 8, 2020
LeetCode problem 821
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:
Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 
Note:
S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
@author: K Li
"""

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        if not S:
            return []

        N = len(S)
        res = []

        # compute forward distance
        dist = N - 1
        for ind, ch in enumerate(S):
            if ch == C:
                dist = 0
            res.append(dist)
            dist += 1
        
        # compute backward distance
        dist = N - 1
        for n in range(N-1, -1, -1):
            ch = S[n]
            if ch == C:
                dist = 0
            res[n] = min(dist, res[n])
            dist += 1
        
        return res

    def shortestToChar1(self, S, C):
        prev = float('-inf')
        ans = []
        for i, x in enumerate(S):
            if x == C: prev = i
            ans.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C: prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
