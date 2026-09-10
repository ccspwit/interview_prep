# -*- coding: utf-8 -*-
"""
Created on June 9, 2019
LeetCode problem 977
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

Example 1:
Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:
Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A is sorted in non-decreasing order.
@author: K Li
"""
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)
        if N == 0:
            return A

        ans = [None for _ in A]
        # find position of first non negative element
        pos = 0
        while pos<N and A[pos] < 0:
            pos += 1
        left, right = pos-1, pos
        curr = 0

        while left >= 0 and right < N:
            lval = A[left]**2
            rval = A[right]**2
            if lval >= rval:
                ans[curr] = rval
                right += 1
            else:
                ans[curr] = lval
                left -= 1
            curr += 1

        # left remain
        while left >= 0:
            ans[curr] = A[left]**2
            left -= 1
            curr += 1
        # right remain
        while right < N:
            ans[curr] = A[right]**2
            right += 1
            curr += 1
        return ans
