# -*- coding: utf-8 -*-
"""
Created on Feb 22, 2020
LeetCode problem 1133
Given an array of integers A, return the largest integer that only occurs once.
If no integer occurs once, return -1.

Example 1:
Input: [5,7,3,9,4,9,8,3,1]
Output: 8
Explanation: 
The maximum integer in the array is 9 but it is repeated. The number 8 occurs only once, so it's the answer.

Example 2:
Input: [9,9,8,8]
Output: -1
Explanation: 
There is no number that occurs only once.

Note:
1 <= A.length <= 2000
0 <= A[i] <= 1000
@author: K Li
"""
class Solution:
    def largestUniqueNumber(self, A: List[int]) -> int:
        val_count = {}
        for n in A:
            val_count[n] = val_count.get(n, 0) + 1
        unique_vals = [val for val, cnt in val_count.items() if cnt==1]
        return max(unique_vals) if unique_vals else -1
