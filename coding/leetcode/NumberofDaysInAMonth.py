# -*- coding: utf-8 -*-
"""
Created on Feb 22, 2020
LeetCode problem 1118
Given a year Y and a month M, return how many days there are in that month.

Example 1:
Input: Y = 1992, M = 7
Output: 31
Example 2:
Input: Y = 2000, M = 2
Output: 29
Example 3:
Input: Y = 1900, M = 2
Output: 28

Note:
1583 <= Y <= 2100
1 <= M <= 12
@author: K Li
"""
class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        # smart leap day calculation
        if M in {1,3,5,7,8,10,12}: return 31
        elif M != 2: return 30
        else: return 28 + (Y % 4 == 0 and Y % 100 != 0 or Y % 400 == 0)

    def numberOfDays1(self, Y: int, M: int) -> int:
        if M == 2:
            if Y % 4:
                return 28
            elif (Y % 400) and (Y%100)==0:
                return 28
            return 29
        elif M in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        else:
            return 30
