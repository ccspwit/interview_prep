# -*- coding: utf-8 -*-
"""
Created on June 8, 2019
LeetCode problem 852
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].

Example 1:

Input: [0,1,0]
Output: 1
Example 2:

Input: [0,2,1,0]
Output: 1
Note:

3 <= A.length <= 10000
0 <= A[i] <= 10^6
A is a mountain, as defined above.
@author: K Li
"""
class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        # binary search
        N = len(A)
        if N <= 2:
            return 0
        low, mid, high = 0, (N-1)//2, N-1
        while low < high:
            '''if A[mid-1] < A[mid]:
                low = mid
            else:
                high = mid - 1'''
            if A[mid] < A[mid+1]:
                low = mid + 1
            else:
                high = mid
            mid = (low+high)//2

        return mid

    def peakIndexInMountainArrayLinear(self, A: List[int]) -> int:
        N = len(A)
        if N <= 2:
            return 0
        left, right = 0, N-1
        while left<N-1 and A[left] <= A[left+1]:
            left += 1
        left_peak = left

        return left_peak
