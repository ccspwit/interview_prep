# -*- coding: utf-8 -*-
"""
Created on May 28, 2017
LeetCode problem 565
A zero-indexed array A consisting of N different integers is given. The array
contains all integers in the range [0, N - 1].

Sets S[K] for 0 <= K < N are defined as follows:

S[K] = { A[K], A[A[K]], A[A[A[K]]], ... }.

Sets S[K] are finite for each K and should NOT contain duplicates.

Write a function that given an array A consisting of N integers, return the
size of the largest set S[K] for this array.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
Note:
N is an integer within the range [1, 20,000].
The elements of A are all distinct.
Each element of array A is an integer within the range [0, N-1].
@author: K Li
"""

class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n) time, O(1) space
        """
        N = len(nums)
        if N<=1:
            return N
        #visited = [0 for _ in nums]
        MAX_INT = 1000000000
        result = 0
        for n in range(N):
            count = 0
            if (nums[n]<MAX_INT):   # not been visited
                pointer = nums[n]
                count = 0
                while nums[pointer]<MAX_INT:
                    tmp = pointer
                    pointer = nums[pointer]
                    nums[tmp] = MAX_INT
                    count += 1
            result = max(count, result)
        return result
    
    def arrayNesting1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n) time, O(n) space
        """
        N = len(nums)
        if N<=1:
            return N
        visited = [0 for _ in nums]
        result = 0
        for n in range(N):
            count = 0
            if (visited[nums[n]]==0):
                pointer = nums[n]
                count = 1
                while nums[n]!=nums[pointer]:
                    count += 1
                    visited[pointer] = 1
                    pointer = nums[pointer]
            result = max(count, result)
        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = [[],[1],[5,4,0,3,1,6,2],
                  [0,1,2,3,4,5],[5,4,3,2,1,0]]
    for test in testVector:
        print(test)
        test1 = test[:]
        print("Longest nested array ", a.arrayNesting(test))
        print("Longest nested array ", a.arrayNesting1(test1))

