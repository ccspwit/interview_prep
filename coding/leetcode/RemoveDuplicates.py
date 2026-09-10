# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 2017
LeetCode problem 26
Given a sorted array, remove the duplicates in place such that each element
appear only once and return the new length. Do not allocate extra space for
another array, you must do this in place with constant memory.

For example, Given input array nums = [1,1,2],
Your function should return length = 2, with the first two elements of nums
being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Scan the array, maintain two pointers
        rightp, scan through the whole array
        leftp, index of current non duplicate elements
        """
        
        if not nums:
            return 0
        N = len(nums)
        
        left = 0
        right = 1

        for right in range(1,N):
            if nums[left] == nums[right]:
                right += 1
            else:
                left += 1
                nums[left] = nums[right]
                right += 1
        return left+1

    def removeDuplicates2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Scan the array, skip duplicated elements, copy new non-duplicate
        element to the end of result array in-place
        """
        
        if not nums:
            return 0
        N = len(nums)
        
        left = 0
        right = 1
        curTail = 1

        while right < N:
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[curTail] = nums[right]
                left = right
                right += 1
                curTail += 1
        return curTail

    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Scan the array, delete duplicate items when detected.
        Length of array changes duing runtime.
        """
        
        if not nums:
            return 0
        N = len(nums)
        curInd = 1
        curLen = N
        curVal = nums[0]
        while curInd < curLen:
            if curVal == nums[curInd]:
                nums.pop(curInd)
                curLen -= 1
            else:
                curVal = nums[curInd]
                curInd += 1
        
        return curLen

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,1],[1,2],
                  [-1, 0, 1, 1, 2, 4],
                  [1,1,2,2,2,3,4,1],
                  [-1,-1,-1,1,2,2]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        n = a.removeDuplicates(test)
        print(test[:n])
    test = sorted(random.randint(-1000,1000,400))
    #x = a.threeSum(test)