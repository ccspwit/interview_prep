# -*- coding: utf-8 -*-
"""
Created on Feb 24, 2020
LeetCode problem 161
Given two strings s and t, determine if they are both one edit distance apart.

Note: 
There are 3 possiblities to satisify one edit distance apart:
Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t

Example 1:
Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.

Example 2:
Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.

Example 3:
Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
@author: K Li
"""
class Solution:
    def isOneEditDistance1(self, s: str, t: str) -> bool:
        # my solution
        def eq_diff1(s1, s2):
            count = 0
            for x, y in zip(s1, s2):
                if x != y:
                    count += 1
                    if count > 1:
                        return False
            return count == 1

        def neq_diff1(s1, s2):
            # len(s1) = len(s2)+1
            del1 = False
            p1, p2 = 0, 0
            while p1<len(s1) and p2<len(s2):
                if del1:
                    if s1[p1] != s2[p2]:
                        return False
                    p1 += 1
                    p2 += 1
                else:
                    if s1[p1] != s2[p2]:
                        p1 += 1
                        del1 = True
                    else:
                        p1 += 1
                        p2 += 1
            # print(del1, p1, p2)
            return del1 or (p1==p2)
        
        if len(s) == len(t):
            return eq_diff1(s, t)
        if len(s) == len(t)+1:
            return neq_diff1(s, t)
        if len(s) == len(t)-1:
            return neq_diff1(t, s)
        return False
    
    def isOneEditDistance(self, s: 'str', t: 'str') -> 'bool':
        # cleaner code
        ns, nt = len(s), len(t)

        # Ensure that s is shorter than t.
        if ns > nt:
            return self.isOneEditDistance(t, s)

        # The strings are NOT one edit away distance  
        # if the length diff is more than 1.
        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                # if strings have the same length
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                # if strings have different lengths
                else:
                    return s[i:] == t[i + 1:]
        
        # If there is no diffs on ns distance
        # the strings are one edit away only if
        # t has one more character. 
        return ns + 1 == nt
