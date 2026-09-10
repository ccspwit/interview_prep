# -*- coding: utf-8 -*-
"""
Created on June 11, 2019
LeetCode problem 647
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

Note:
The input string length won't exceed 1000.
@author: K Li
"""
class Solution:
    def countSubstrings1(self, S):
        # flavor of dynamic programming
        # center 2*N-1 position N position and N-1 mid point
        # if palindrome string, count++ and expand 1
        # else stop and move to the next center
        N = len(S)
        ans = 0
        for center in range(2*N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

    def countSubstrings(self, S):
        # flavor of dynamic programming
        # center start from 1, N
        # left/right odd even place
        # if palindrome string, count++ and expand 1
        # else stop and move to the next center
        N = len(S)
        if N == 0:
            return 0
        ans = N
        for pivot in range(1, N):
            left = pivot-1
            right = pivot
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1

            left = pivot-1
            right = pivot + 1
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1

        return ans
