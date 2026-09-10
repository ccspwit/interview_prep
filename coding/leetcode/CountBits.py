# -*- coding: utf-8 -*-
"""
Created on Sep 26, 2022
LeetCode problem 338
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1:
Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10

Example 2:
Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

Constraints:
0 <= n <= 105
Follow up:
It is very easy to come up with a solution with a runtime of O(n log n). Can you do it in linear time O(n) and possibly in a single pass?
Can you do it without using any built-in function (i.e., like __builtin_popcount in C++)?
@author: K Li
"""
class Solution(object):
    def __init__(self):
        self.table=[
            0, 1, 1, 2,
            1, 2, 2, 3,
            1, 2, 2, 3,
            2, 3, 3, 4
        ]

    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        for n in range(n+1):
            temp = n
            count = 0
            while n>=16:
                count += self.table[n & 15]
                n = n>>4
            count += self.table[n]
            res.append(count)
        return res
