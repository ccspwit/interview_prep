# -*- coding: utf-8 -*-
"""
Created on May 24, 2017
LeetCode problem 532
Given an array of integers and an integer k, you need to find the number of
unique k-diff pairs in the array. Here a k-diff pair is defined as an integer
pair (i, j), where i and j are both numbers in the array and their absolute
difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of
unique pairs.
Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4)
and (4, 5).
Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).
Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
@author: K Li
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        hashmap, 2sum method
        O(n) time, O(n) space
        """
        N = len(nums)
        if N<2:
            return 0
        count = 0
        if k>0:
            diffSet = set()
            for n in nums:
                diffSet.add(n-k)
            for n in set(nums):
                if n in diffSet:
                    count += 1
            return count
        elif k==0:
            hashMap = {}
            for n in nums:
                hashMap[n] = hashMap.get(n,0)+1
            return len([i for i in hashMap.values() if i>=2])
        
        return 0

    def findPairs1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Sort & count
        O(nlogn) time, O(1) space
        """
        N = len(nums)
        if N<2:
            return 0
        nums.sort()
        left, right = 0, 1
        nPairs = 0
        while right < N:
            diff = nums[right] - nums[left]
            if (diff==k):
                nPairs += 1
                while (left<N-1) and (nums[left]==nums[left+1]):
                    left += 1
                left += 1
                right = max(left+1, right+1)
            elif diff<k:
                right += 1
            else:
                left += 1
                right = max(left+1, right)
            #print(left,right)
        return nPairs
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([],1),([1,2,3],1),([1,1,1,1,1],0),
                  ([1,2,3,4,5],-1),
                  ([1,1,2,2,3],1),([1,1,2,2,3],0),
                  ([6,1,2,3,4],2),([6,1,2,3,4],0),([6,1,2,3,4],6)]
    a = Solution()
    for test in testVector:
        print(test[0])
        print("%d pairs differed by %d"%(a.findPairs(test[0],test[1]),test[1]))
        print("%d pairs differed by %d"%(a.findPairs1(test[0],test[1]),test[1]))
