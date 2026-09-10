# -*- coding: utf-8 -*-
"""
Created on Thu May 1st 2017
LeetCode problem 88
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as
one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to
m + n) to hold additional elements from nums2. The number of elements
initialized in nums1 and nums2 are m and n respectively.
@author: K Li
"""

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        Start filling data from the end of array from largest of two arrays.
        If nums1 array is exhausted, fill remaining nums2 into unfilled nums1
        positions.
        """
        if (len(nums1)<m+n):
            raise ValueError("size of nums1 must be >= m+n.")
        '''if (m==0) | (n==0):
            return'''
        mr = m-1
        nr = n-1
        #left, right = 0, m+n-1
        for i in range(m+n-1,-1,-1):
            if (mr < 0) | (nr < 0):
                break
            if nums1[mr] >= nums2[nr]:
                nums1[i] = nums1[mr]
                mr -= 1
            else:
                nums1[i] = nums2[nr]
                nr -= 1
            
        while nr>=0:
            nums1[i] = nums2[nr]
            nr -= 1
            i -= 1

        return
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([-1],0,[1],1),([2,0],1,[1],1),
                  ([1,2,3,4,0,0,0,0],4,[5,6,7,8],4),
                  ([5,6,7,8,0,0,0,0],4,[1,2,3,4],4),
                  ([2,4,6,8,0,0,0,0],4,[1,3,5],3),
                  ([2,4,6,8,0,0,0,0],4,[1,1,3,5],4)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        arr1, arr2 = test[0], test[2]
        a.merge(arr1,test[1],arr2,test[3])
        print(arr1)
    random.seed(0)
    test = random.randint(-1000,1000,500)
    #x = a.threeSum(test)
