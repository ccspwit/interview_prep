# -*- coding: utf-8 -*-
"""
Created on May 19, 2017
LeetCode problem 215
Find the kth largest element in an unsorted array. Note that it is the kth
largest element in the sorted order, not the kth distinct element.

For example,
Given [3,2,1,5,6,4] and k = 2, return 5.

Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
@author: K Li
"""

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        heap sort, O(n+klog(n)). More efficient if k<<n
        """
        import heapq
        N = len(nums)
        if N==0:
            raise ValueError("array is empty")
        if N<k:
            raise ValueError("K is larger than array size")
        
        return heapq.nlargest(k, nums)[k-1]

    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        Sort then index, O(nlog(n))
        """
        N = len(nums)
        if N==0:
            raise ValueError("array is empty")
        if N<k:
            raise ValueError("K is larger than array size")
        
        nums.sort()
        return nums[-k]
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [([1],1),([1,1],2),
                  ([2,2],1),([1,9,9,9],2),
                  ([3,2,1,5,6,4],2)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('The %dth largest element is : ',
              a.findKthLargest(test[0],test[1]))

    tc = np.random.randint(1,10000,1000)