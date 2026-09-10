# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 2017
LeetCode problem 35

Given a sorted array and a target value, return the index if the target
is found. If not, return the index where it would be if it were inserted
in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0

@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        bi-section method
        """
        N = len(nums)
        if(N==0):
            return 0
        start, end = 0, N-1
        while start<end:
            mid = (start+end)//2
            #print(start,mid,end)
            if(nums[mid]>target):
                end = mid
            elif(nums[mid]<target):
                start = (start+end+1)//2
            else:
                return mid

        if(nums[start] > target):
            return start
        elif(nums[start] < target):
            return start+1
        else:
            return start
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([1,2,3,4,5],3),
                  ([1,2,3,4,5],0),
                  ([1,2,3,4,5],6),
                  ([0,2,4,6,8,10],5),
                  ([],3)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        n = a.searchInsert(test[0], test[1])
        print(n)
    test = sorted(random.randint(0,100,1000))
