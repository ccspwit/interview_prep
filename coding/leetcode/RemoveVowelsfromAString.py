# -*- coding: utf-8 -*-
"""
Created on Feb 22, 2020
LeetCode problem 1119
Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and return the new string.

Example 1:
Input: "leetcodeisacommunityforcoders"
Output: "ltcdscmmntyfrcdrs"

Example 2:
Input: "aeiou"
Output: ""

Note:
S consists of lowercase English letters only.
1 <= S.length <= 1000
@author: K Li
"""
class Solution:
    def removeVowels(self, S: str) -> str:
        # string translate function
        mapping = {ord(vowel): None for vowel in 'aeiou'}
        return S.translate(mapping)

    def removeVowels1(self, S: str) -> str:
        # filter list then join
        vowels = ['a', 'e', 'i', 'o', 'u']
        return "".join(filter(lambda a: a not in vowels, list(S)))
