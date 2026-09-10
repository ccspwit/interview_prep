# -*- coding: utf-8 -*-
"""
Created on May 27, 2017
LeetCode problem 560
Given an array of integers and an integer k, you need to find the total
number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the
integer k is [-1e7, 1e7].
@author: K Li
"""

class Solution(object):
    def subarraySum(self, A, K):
        """
        hashmap method, code is more concise but more difficult to understand
        A little more efficient.
        """
        count = {0:1}
        ans = su = 0
        for x in A:
            su += x
            ans += count.get(su-K,0)
            count[su] = count.get(su,0)+1
        return ans

    def subarraySum3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Use hashmap to store cumsum and occurance
        O(n) time, O(n) space
        TLE?
        """
        N = len(nums)
        if N==0:
            return 0
        
        csMap = {}
        cumsum = 0
        count = 0
        for n in range(N):
            cumsum += nums[n]
            count += csMap.get(cumsum-k,0)
            csMap[cumsum] = csMap.get(cumsum, 0)+1
            #print(csMap)
            if cumsum==k:
                count += 1
            #print(cumsum, count)
                    
        return count

    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Compute cumsum fisrt from different start positions. Use less memory
        O(n^2) time, O(1) space
        TLE?
        """
        N = len(nums)
        if N==0:
            return 0

        count = 0
        # compute cumsum with shifting (to the right) start position
        for start in range(N):
            cumsum = 0
            for end in range(start, N):
                cumsum += nums[end]
                if cumsum==k:
                    count += 1
                    
        return count

    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Compute cumsum fisrt, then check for cumsum from i, i=0,....,N-1
        O(n^2) time, O(n) space
        TLE?
        """
        N = len(nums)
        if N==0:
            return 0
        # compute cumsum of the array
        csum = nums[:]
        csum[0] = 0
        for n in range(N-1):
            csum[n+1] = csum[n]+nums[n]
        csum.append(csum[N-1]+nums[N-1])

        #count # of subarray with sum k using sliding window methods
        count = 0
        for left in range(N):
            for right in range(left+1, N+1):
                if (csum[right]-csum[left])==k:
                    count += 1
                    
        return count

if __name__ == '__main__':
    import numpy as np
	# test case to generate ListNode and run test function
    testVector = [([2],2),([0,1,-1,1,0],0),
                  ([1,3,2,2,5,2,3,7],4),
                  ([1,2,3,3,2,1,4,3,2,0],5)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('# of continuous subarray: ',a.subarraySum(test[0], test[1]))
        print('# of continuous subarray: ',a.subarraySum3(test[0], test[1]))

    tc = np.random.randint(1,100,100)
    print(a.subarraySum(tc,100), a.subarraySum3(tc,100))