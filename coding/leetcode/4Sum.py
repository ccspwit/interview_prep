# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 18
Given an array S of n integers, are there elements a, b, c, and d in S such
that a + b + c + d = target? Find all unique quadruplets in the array which
gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

For example, given array S = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[ [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]]
@author: K Li
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        First create hashtable for target-twoSum, then check other twoSum.
        O(n^2) time, O(n^2) space
        """
        N = len(nums)
        if N<4:
            return []
        diffMap = {}
        for i in range(N-1):
            for j in range(i+1,N):
                diff = target-(nums[i]+nums[j])
                if diff not in diffMap:
                    
                    diffMap[diff] = [(i,j)]
                else:
                    diffMap[diff].append([i,j])
        #print(diffMap)
        result = []
        fourSet = set()
        for i in range(N-1):
            for j in range(i+1,N):
                twoSum = nums[i]+nums[j]
                if twoSum in diffMap:
                    indices = diffMap[twoSum]
                    for n_m in indices:
                        if (i not in n_m) and (j not in n_m):
                            n, m = n_m
                            values = tuple(sorted((nums[i],nums[j],nums[n], nums[m])))
                            if values not in fourSet:
                                fourSet.add(values)
                                result.append(list(values))

        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([],1),([1,2,3,4],10),
                  ([1,0,-1,0,-2,2],0)]
    for test in testVector:
        print(test)
        test1 = test[:]
        print("Possible 4 sum pairs are ", a.fourSum(test[0], test[1]))
        #print("Longest nested array ", a.arrayNesting1(test1))

