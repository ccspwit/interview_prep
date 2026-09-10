# -*- coding: utf-8 -*-
"""
Created on May 13, 2017
LeetCode problem 217, 219, 220 combined
---#217
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in
the array, and it should return false if every element is distinct.

---#219
Given an array of integers and an integer k, find out whether there are
two distinct indices i and j in the array such that nums[i] = nums[j] and
the absolute difference between i and j is at most k.

---#220
Given an array of integers, find out whether there are two distinct
indices i and j in the array such that the absolute difference between
nums[i] and nums[j] is at most t and the absolute difference between i and j
is at most k.
@author: K Li
"""

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        Bucket sort method, amazing! very efficient
        For the last k elements, map to a bucket of size t+1, nums[i]//(t+1)
        For a match, meaning abs(nums[i]-nums[j])<=t, two values are
        1. fall within the same bucket
        2. belong to neightbor bucket i/i+1, or i-1/i
        3. we can therefore use dictionary/hashmap to match bucket id O(1)
        """
        N = len(nums)
        if N<=1:
            return False
        if (k<=0):
            return False
        if t<0:
            return False
        bucket = {}
        
        for n in range(N):
            #left = max(n-k,0)
            bucketID = nums[n]//(t+1)
            if bucketID in bucket:
                return True
            if bucketID-1 in bucket:
                if abs(bucket[bucketID-1]-nums[n])<=t:
                    return True
            if bucketID+1 in bucket:
                if abs(bucket[bucketID+1]-nums[n])<=t:
                    return True

            # no match, add nums[n] with key=bucketID
            bucket[bucketID] = nums[n]
            # remove (n-k)th element
            if n-k>=0:
                del bucket[nums[n-k]//(t+1)]
        return False
                
    def containsNearbyAlmostDuplicate1(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        Brute force solution, time limit exceeded
        """
        N = len(nums)
        if N<=1:
            return False
        if (k<=0):
            return False
        if t<0:
            return False
        
        for n in range(1,N):
            left = max(n-k,0)
            for m in range(left, n):
                #check if abs(nums[i]-nums[j])<=t
                if abs(nums[n]-nums[m])<=t:
                    return True
        return False
       
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        N = len(nums)
        if N<=1:
            return False
        if (k<=0):
            return False

        dictCache = {}
        for ind, val in enumerate(nums):
            if val in dictCache:
                if (ind-dictCache[val])<=k:
                    return True
            
            dictCache[val] = ind
        return False
        
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]N
        :rtype: bool
        """
        N = len(nums)
        if N<=1:
            return False
        s = set()
        for e in nums:
            if e in s:
                return True
            else:
                s.add(e)
        return False

    def containsDuplicate1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set(nums)
        if len(s)==len(nums):
            return False
        else:
            return True
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[],[123],[1,2,3],
                  [1,1,1],[1,1,2]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Contain Duplicate? ', a.containsDuplicate(test))

    testVector = [([],1),([123],0),([1,2,3],1),
                  ([1,1,1],2),([1,2,3,1],1),([1,2,3,1],3)]
    print('Contains duplicate II')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Contain Duplicate? ', a.containsNearbyDuplicate(test[0], test[1]))

    testVector = [([],0,0),([123],1,1),([1,1],1,0),
                  ([1,2,3,1],1,1),([1,2,3,1],1,0),([1,2,3,1],2,2)]
    print('Contains duplicate III')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Contain Duplicate? ',
              a.containsNearbyAlmostDuplicate(test[0], test[1], test[2]),
              a.containsNearbyAlmostDuplicate1(test[0], test[1], test[2]))

    import numpy as np
    tc = np.random.randint(0,10000,100)
    a.containsNearbyAlmostDuplicate(tc, 100, 1)
    a.containsNearbyAlmostDuplicate1(tc, 100, 1)