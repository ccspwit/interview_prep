# -*- coding: utf-8 -*-
"""
Created on Jan 13, 2020
LeetCode problem 696
Give a string s, count the number of non-empty (contiguous) substrings that have the same number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

Substrings that occur multiple times are counted the number of times they occur.

Example 1:
Input: "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
Notice that some of these substrings repeat and are counted the number of times they occur.
Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

Example 2:
Input: "10101"
Output: 4
Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.

Note:
s.length will be between 1 and 50,000.
s will only consist of "0" or "1" characters.
@author: K Li
"""
class Solution:
    def countBinarySubstrings1(self, s: str) -> int:
        # linear scan
        N = len(s)
        if N <= 1:
            return 0
        prev_pos, prev_val = 0, s[0]
        pivot_pos, pivot_val = 0, s[0]
        cur_pos = 0
        count = 0
        while cur_pos < N:
            cur_val = s[cur_pos]
            if cur_val != pivot_val:
                # update prev_pos, pivot_pos
                count += min(cur_pos-pivot_pos, pivot_pos-prev_pos)
                prev_pos, prev_val = pivot_pos, pivot_val
                pivot_pos, pivot_val = cur_pos, cur_val
            cur_pos += 1

        # post processing
        count += min(cur_pos-pivot_pos, pivot_pos-prev_pos)
        return count

    def countBinarySubstrings(self, s: str) -> int:
        # group into contiguous 0, 1
        N = len(s)
        if N <= 1:
            return 0
        arr = []
        prev_pos, prev_val = 0, s[0]
        for n in range(1, N):
            if s[n] != prev_val:
                arr.append(n-prev_pos)
                prev_pos, prev_val = n, s[n]
        arr.append(N-prev_pos)
        
        count = 0
        for n in range(1, len(arr)):
            count += min(arr[n-1], arr[n])
        return count
