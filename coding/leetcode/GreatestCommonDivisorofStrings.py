# -*- coding: utf-8 -*-
"""
Created on June 10, 2019
LeetCode problem 1071
For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Note:
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
@author: K Li
"""
class Solution:
    def gcdOfStrings1(self, str1: str, str2: str) -> str:
        # brute-force method
        minStr = (str1 if len(str1) < len(str2) else str2)
        maxStr = (str1 if len(str1) >= len(str2) else str2)
        n_min, n_max = len(minStr), len(maxStr)
        for k in range(n_min,0,-1):
            if n_max%k == 0 and n_min%k == 0:
                if ((n_min//k) * minStr[:k] == minStr) and ((n_max//k) * minStr[:k] == maxStr):
                    return minStr[:k]
        return ""

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # this seem a nicer solution
        # imilar to Euclidian algorithm
        def gcd(x, y):
            # x>0, y>0
            while y:
                x, y = y, x%y
            return y

        while True:
            if str2 in str1:
                str1 = str1.replace(str2, '')
            elif str1 in str2:
                str2 = str2.replace(str1, '')
            else:
                return ""
            if str1 == '':
                return str2
            if str2 == '':
                return str1
        return ""
