# -*- coding: utf-8 -*-
"""
Created on June 11, 2019
LeetCode problem 1051
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)

Example 1:
Input: [1,1,4,2,1,3]
Output: 3
Explanation: 
Students with heights 4, 3 and the last 1 are not standing in the right positions.

Note:
1 <= heights.length <= 100
1 <= heights[i] <= 100
@author: K Li
"""
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        hs = sorted(heights)
        diff = 0
        for n in range(len(heights)):
            if hs[n] != heights[n]:
                diff += 1
        return diff
