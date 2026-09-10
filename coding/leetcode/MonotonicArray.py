# -*- coding: utf-8 -*-
"""
Created on June 8, 2019
LeetCode problem 896
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].
Return true if and only if the given array A is monotonic.

Example 1:
Input: [1,2,2,3]
Output: true

Example 2:
Input: [6,5,4,4]
Output: true

Example 3:
Input: [1,3,2]
Output: false

Example 4:
Input: [1,2,4,5]
Output: true

Example 5:
Input: [1,1,1]
Output: true

Note:
1 <= A.length <= 50000
-100000 <= A[i] <= 100000
@author: K Li
"""
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        # checking for increasing or decreasing
        # early stop if both False
        valid = True
        mi, md = True, True
        for n in range(1, len(A)):
            if mi:
                if A[n-1] > A[n]:
                    mi = False
            if md:
                if A[n-1] < A[n]:
                    md = False
            if not mi and not md:
                break
        return mi or md
