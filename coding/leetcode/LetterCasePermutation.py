# -*- coding: utf-8 -*-
"""
Created on June 6, 2019
LeetCode problem 784
Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
@author: K Li
"""
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return ['']
        result = ['']
        for ch in S:
            temp = result
            if ch.isdigit():
                result = [ele+ch for ele in temp]
            elif ch.isalpha():
                result = [ele+ch.lower() for ele in temp] + [ele+ch.upper() for ele in temp]

        return result
