# -*- coding: utf-8 -*-
"""
Created on May 26, 2017
LeetCode problem 581
Given an integer array, you need to find one continuous subarray that if you
only sort this subarray in ascending order, then the whole array will be
sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make
the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
@author: K Li
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Two pointer approach:
            1. From left, when encounter first descending record index, then
            find min value on the right, scan from start to left, compare with
            minRight, find position when num[i]>minRight, record as new left edge.
            2. Perform similar operation to find right edge, do it reversely.
        O(n) time, O(1) space
        """
        N = len(nums)
        if N==0:
            return 0
        
        minRight = float('inf')
        maxLeft = float('-inf')

        left = N-1      
        wrongOrder = False
        for i in range(N-1):
            if wrongOrder:
                minRight = min(minRight,nums[i+1])
            else:
                if nums[i]>nums[i+1]:
                    wrongOrder = True
                    minRight = nums[i+1]
                    left = i

        wrongOrder = False
        right = left
        for j in range(N-1,left,-1):
            if wrongOrder:
                maxLeft = max(maxLeft,nums[j-1])
            else:
                if nums[j]<nums[j-1]:
                    wrongOrder = True
                    maxLeft = nums[j-1]
                    right = j
                    
        #print(left,right)
        #print('minRight=',minRight, 'maxLeft=',maxLeft)
        
        left = N-1
        for i in range(left):
            if nums[i] > minRight:
                left = i
                break
        right = left
        for j in range(N-1, left,-1):
            if nums[j] < maxLeft:
                right = j
                break

        #print(left, right)
        if left==right:
            return 0
        else:
            return right-left+1
    
    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        First sort, then compared with original series to find left/right
        boundary of mismatch
        O(nlogn) time, O(n) space
        """
        N = len(nums)
        if N==0:
            return 0
        sortedArray = sorted(nums)
        i, j = 0, N-1
        for i in range(N):
            if nums[i]!=sortedArray[i]:
                break
        for j in range(N-1,i,-1):
            if nums[j]!=sortedArray[j]:
                break
        if i==j:
            return 0
        else:
            return j-i+1

if __name__ == '__main__':
    import numpy as np
	# test case to generate ListNode and run test function
    testVector = [[1],[1,1],[1,2,2,1],[1,2,3,4,5,6],
                  [2, 6, 4, 8, 10, 9, 15],
                  [1,5,6,10,4,9,7,11,2],
                  [1,3,5,4,2],
                  [1,5,3,2,4],
                  [1,2,3,7,4,5,6,8]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Shortest Unsorted Continous Subarray: ',a.findUnsortedSubarray(test))
        print('Shortest Unsorted Continous Subarray: ',a.findUnsortedSubarray1(test))

    tc = np.random.randint(1,10000,1000)
    print(a.findUnsortedSubarray(tc))
    print(a.findUnsortedSubarray1(tc))