# -*- coding: utf-8 -*-
"""
Created on June 4, 2017
LeetCode problem 41
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

Your algorithm should run in O(n) time and uses constant space.
@author: K Li
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==0:
            return 1
        for n in range(N):
            ele = nums[n]
            while True:
                if ele <= 0 or ele > N or ele == nums[ele - 1]:
                    break
                # swap
                print(ele,N)
                nums[ele-1], ele = ele, nums[ele-1]
                #ele, nums[ele-1] = nums[ele-1], ele

        for n in range(N):
            if (nums[n]!=n+1):
                return n+1
        return N+1

    def firstMissingPositive1(self, A):
        n = len(A)
        for index in range(n):
            element = A[index]
            while True:
                if element <= 0 or element > n or element == A[element - 1]:
                    break
                A[element - 1], element = element, A[element - 1]
        for index in range(n):
            if A[index] != index + 1:
                return index + 1
        return n + 1
    
if __name__ == '__main__':
    a = Solution()
    testVector = [[1],[2],[1,0],[0,1],
                  [2,3,1,1,4],
                  [-1,4,2,1,9,10],
                  [0,1,2,3,4],
                  [3,2,0,3,2,1,0,1]]
    a = Solution()
    for test in testVector:
        print(test)
        test1=test[:]
        print("First missing positive number is",(a.firstMissingPositive(test)))
        #print("First missing positive number is",(a.firstMissingPositive1(test1)))
    
    #test = np.random.randint(0,20,20)