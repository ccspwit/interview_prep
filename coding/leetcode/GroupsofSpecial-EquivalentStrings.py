# -*- coding: utf-8 -*-
"""
Created on June 8, 2019
LeetCode problem 893
You are given an array A of strings.
Two strings S and T are special-equivalent if after any number of moves, S == T.
A move consists of choosing two indices i and j with i % 2 == j % 2, and swapping S[i] with S[j].
Now, a group of special-equivalent strings from A is a non-empty subset S of A such that any string not in S is not special-equivalent with any string in S.
Return the number of groups of special-equivalent strings from A.

Example 1:
Input: ["a","b","c","a","c","c"]
Output: 3
Explanation: 3 groups ["a","a"], ["b"], ["c","c","c"]

Example 2:
Input: ["aa","bb","ab","ba"]
Output: 4
Explanation: 4 groups ["aa"], ["bb"], ["ab"], ["ba"]

Example 3:
Input: ["abc","acb","bac","bca","cab","cba"]
Output: 3
Explanation: 3 groups ["abc","cba"], ["acb","bca"], ["bac","cab"]

Example 4:
Input: ["abcd","cdab","adcb","cbad"]
Output: 1
Explanation: 1 group ["abcd","cdab","adcb","cbad"]

Note:
1 <= A.length <= 1000
1 <= A[i].length <= 20
All A[i] have the same length.
All A[i] consist of only lowercase letters.
@author: K Li
"""
class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        def specialEquivalent(s):
            # normalize SE string into sorted odd part + sorted even part
            # then use set to count unique groups
            if len(s) == 0:
                return s
            even_str = ''.join(sorted(s[::2]))
            odd_str = ''.join(sorted(s[1::2]))
            return even_str+odd_str
        se_str = [specialEquivalent(ele) for ele in A]
        # print(se_str)
        return len(set(se_str))
