# -*- coding: utf-8 -*-
"""
Created on June 8, 2017
LeetCode problem 153, 154 combined
---#153
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
Find the minimum element.
You may assume no duplicate exists in the array.

---#154
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.
The array may contain duplicates.
@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def findMinI(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        bi-section method, the logic of this implementation is more clear
        First check whether left side is sorted or right side is sorted.
        """
        
        start, end = 0, len(nums)-1
        while start<end:
            # note mid point could be smaller than left point
            # or larger than right point
            mid = (start+end)//2
            
            if (nums[mid]<nums[end]):
                #right side sorted, have to check right side, because
                #for 2-array case, start,mid,end = 0,0,1
                end = mid
                """if minVal > nums[mid]:
                    minVal = nums[mid]"""
            else:
                # left side sorted, minimum on the right
                start = mid+1
                """if minVal>nums[end]:
                    minVal = nums[end]"""
        return nums[start]

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if(N==0):
            return None
        start, end = 0, N-1
        while start<end:
            # note mid point could be smaller than left point
            # or larger than right point
            mid = (start+end)//2
            _midVal, _endVal = nums[mid], nums[end]
            if _midVal < _endVal:
                #right side sorted, have to check right side, because
                #for 2-array case, start,mid,end = 0,0,1
                end = mid
                """if minVal > nums[mid]:
                    minVal = nums[mid]"""
            elif _midVal > _endVal:
                # left side sorted, minimum on the right
                start = mid+1
                """if minVal>nums[end]:
                    minVal = nums[end]"""
            else:
                #equal, can't decide which side
                end -= 1
        return nums[start]
        

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    a = Solution()
    testVector = [[1],[3,1],[1,2,4,5,7,0],
                  [11,22,33,44,55,1,2,3,4,5,6,7,8,9,10]]
    print("Find minimum in rotated sorted array")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print("mimimum is :",a.findMinI(test))
        
    testVector = [[1],[3,3,1],[3,1,2,2,2],[3,1,1,1,2],[3,4,5,1,2],
                  [11,22,33,44,55,1,2,3,4,5,6,7,8,9,10]]
    print("Find minimum in rotated sorted array II")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print("mimimum is :",a.findMin(test))
        #print(n)
