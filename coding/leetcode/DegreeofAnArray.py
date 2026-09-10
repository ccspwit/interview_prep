# -*- coding: utf-8 -*-
"""
Created on Jan 8, 2020
LeetCode problem 697
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

Example 1:
Input: [1, 2, 2, 3, 1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.

Example 2:
Input: [1,2,2,3,1,4,2]
Output: 6

Note:
nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.
@author: K Li
"""
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        # go through list to find count and length of unique values
        degree_pos = {}
        maxdegree_minlen = [0, len(nums)]
        
        for ind, val in enumerate(nums):
            # update degree, start, and length for each unique values
            if val not in degree_pos:
                degree_pos[val] = (1, ind, 1)
            else:
                degree, start, end = degree_pos[val]
                degree_pos[val] = (degree+1, start, ind-start+1)
            # update max degree and min length
            if degree_pos[val][0] > maxdegree_minlen[0]:
                maxdegree_minlen = [degree_pos[val][0], degree_pos[val][2]]
            elif degree_pos[val][0] == maxdegree_minlen[0]:
                if degree_pos[val][2] < maxdegree_minlen[1]:
                    maxdegree_minlen[1] = degree_pos[val][2]
        # print(maxdegree_minlen)
        return maxdegree_minlen[1]

    def findShortestSubArray_lc(self, nums):
        left, right, count = {}, {}, {}
        for i, x in enumerate(nums):
            if x not in left: left[x] = i
            right[x] = i
            count[x] = count.get(x, 0) + 1

        ans = len(nums)
        degree = max(count.values())
        for x in count:
            if count[x] == degree:
                ans = min(ans, right[x] - left[x] + 1)

        return ans
