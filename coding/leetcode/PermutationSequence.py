# -*- coding: utf-8 -*-
"""
Created on May 30 2019
LeetCode problem 60
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order,
we get the following sequence for n = 3:
"123"
"132"
"213"
"231"
"312"
"321"

Given n and k, return the kth permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
@author: K Li
"""
class Solution(object):
    # comupte result numerically
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def getDigits(curr_string, factorial, k):
            N = len(curr_string)
            if N == 1:
                return curr_string

            ind = k // factorial
            rem = k % factorial
            # print(curr_string, k, factorial, ind, rem)
            next_string = curr_string[:ind] + curr_string[ind+1:]
            next_factorial = factorial//(N-1)
            return curr_string[ind]+getDigits(next_string, next_factorial, rem)
        
        # compute [(n-1)!, (n-2)!, ..., 1]
        factorial = 1
        for m in range(1, n):
            factorial *= m
        string = "".join([str(m) for m in range(1, n+1)])
        return getDigits(string, factorial, k-1)

    # recursively generate sequence, time out
    def getPermutationR(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        def permuteString(nums, n, k):
            N = len(nums)
            if N<=1:
                return [nums]
            
            results = []
            count = 0
            for n in range(N):
                ele = nums[n]
                remString = nums[:n] + nums[n+1:N]
                temp = permuteString(remString, n, k)
                for seq in temp:
                    results.append(ele+seq)
                    if N==n:
                        count += 1
                        if count == k:
                            return results
            return results
        
        L = permuteString("".join([str(n) for n in range(1, n+1)]), n, k)
        
        return L[k-1]
