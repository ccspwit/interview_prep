# -*- coding: utf-8 -*-
"""
Created on June 11, 2019
LeetCode problem 1064
Given an array A of distinct integers sorted in ascending order, return the smallest index i that satisfies A[i] == i.  Return -1 if no such i exists.

Example 1:
Input: [-10,-5,0,3,7]
Output: 3
Explanation: 
For the given array, A[0] = -10, A[1] = -5, A[2] = 0, A[3] = 3, thus the output is 3.

Example 2:
Input: [0,2,5,8,17]
Output: 0
Explanation: 
A[0] = 0, thus the output is 0.

Example 3:
Input: [-10,-5,3,4,7,9]
Output: -1
Explanation: 
There is no such i that A[i] = i, thus the output is -1.

Note:
1 <= A.length < 10^4
-10^9 <= A[i] <= 10^9
@author: K Li
"""
class Solution:
    def fixedPoint1(self, A: List[int]) -> int:
        # binary search
        N = len(A)
        if N == 0:
            return -1
        low, high = 0, N-1
        ans = -1
        while low < high:
            mid = (low+high) // 2
            if A[mid] == mid:
                ans = mid
                high = mid - 1
            elif A[mid] > mid:
                high = mid - 1
            else:
                low = mid + 1
            print(low, mid, high, ans)

        if A[low] == low:
            ans = low
        return ans

    def fixedPoint(self, A: List[int]) -> int:
        # slight simpler binary search
        if not A:
            return -1
        lo, hi = 0, len(A) - 1
        while lo < hi:
            mid = (lo + hi) // 2 
            if A[mid] < mid:
                lo = mid + 1
            else:
                hi = mid
        return lo if A[lo] == lo else -1
