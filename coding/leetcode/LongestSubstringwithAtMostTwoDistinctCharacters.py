# -*- coding: utf-8 -*-
"""
Created on Feb 23, 2020
LeetCode problem 159
Given a string s , find the length of the longest substring t that
contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.
Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
@author: K Li
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # two pointers and counter
        # if not s: return 0
        counter = {}
        max_len = 0
        left = 0
        for ind, c in enumerate(s):
            # add count for c
            counter[c] = counter.get(c, 0) + 1
            if len(counter) > 2:
                cur_len = ind - left
                if cur_len > max_len:
                    max_len = cur_len
                # move left point to two distinct characters
                while len(counter) > 2:
                    left_ch = s[left]
                    counter[left_ch] = counter[left_ch] - 1
                    if counter[left_ch] == 0:
                        counter.pop(left_ch)
                    left += 1
        # check counter last time
        if len(counter) <= 2:
            cur_len = len(s) - left
            if cur_len > max_len:
                max_len = cur_len
        
        return max_len
