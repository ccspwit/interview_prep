# -*- coding: utf-8 -*-
"""
Created on Sun May 7, 2017
LeetCode problem 33, 81 combined
---#33
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its
index, otherwise return -1.

You may assume no duplicate exists in the array.

---#81
Suppose an array sorted in ascending order is rotated at some pivot unknown
to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.
@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def searchI(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        bi-section method, the logic of this implementation is more clear
        First check whether left side is sorted or right side is sorted.
        """
        N = len(nums)
        """if(N==0):
            return -1
        if N==1:
            return 0 if nums[0]==target else -1"""
        start, end = 0, N-1
        
        while start<=end:
            # note mid point could be smaller than left point
            # or larger than right point
            mid = (start+end)//2
            
            #print(start,mid,end)
            if target == nums[mid]:
                return mid
            """if target == nums[end]:
                return end
            if target == nums[start]:
                return start"""
            # target != nums[mid]
            if (nums[mid]<nums[end]):
                #right side sorted, have to check right side, because
                #for 2-array case, start,mid,end = 0,0,1
                if (target<=nums[end]) and (target>nums[mid]):
                    start = mid+1
                else:
                    end = mid-1
            else:
                # left side sorted
                if (target<nums[mid]) and (target>=nums[start]):
                    end = mid-1
                else:
                    start = mid+1
        return -1

    def searchI1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        bi-section method
        """
        N = len(nums)
        if(N==0):
            return -1
        if N==1:
            return 0 if nums[0]==target else -1
        start, end = 0, N-1
        index = -1
        
        while start<end:
            # note mid point could be smaller than left point
            # or larger than right point
            mid = (start+end)//2
            
            #print(start,mid,end)
            if target == nums[mid]:
                return mid
            if target == nums[end]:
                return end
            if target == nums[start]:
                return start
            # target != nums[mid]
            if (target<nums[mid]):
                if (nums[mid]<nums[end]):
                    end = mid
                elif(target>nums[start]):
                    end = mid
                else:
                    start = (start+end+1)//2
            else:   #target<nums[mid]
                if (nums[mid]>nums[start]):
                    start = (start+end+1)//2
                elif(target>nums[start]):
                    end = mid
                else:
                    start = (start+end+1)//2
        return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        bi-section method, the logic of this implementation is more clear
        First check whether left side is sorted or right side is sorted.
        """
        N = len(nums)
        """if(N==0):
            return -1
        if N==1:
            return 0 if nums[0]==target else -1"""
        start, end = 0, N-1
        
        while start<=end:
            # note mid point could be smaller than left point
            # or larger than right point
            mid = (start+end)//2
            
            #print(start,mid,end)
            if target == nums[mid]:
                return True
            """if target == nums[end]:
                return end
            if target == nums[start]:
                return start"""
            # target != nums[mid]
            if (nums[mid]<nums[end]):
                #right side sorted, have to check right side, because
                #for 2-array case, start,mid,end = 0,0,1
                if (target<=nums[end]) and (target>nums[mid]):
                    start = mid+1
                else:
                    end = mid-1
            elif (nums[mid]>nums[end]):
                # left side sorted
                if (target<nums[mid]) and (target>=nums[start]):
                    end = mid-1
                else:
                    start = mid+1
            else:
                end -= 1
        return False

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    a = Solution()
    testVector = [([],1),([1],1),([1],2),([3,1],1),
                  ([4,5,7,0,1,2],4),([4,5,7,0,1,2],2),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],55),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],1),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],33),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],6),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],30),
                  ([],3)]
    print("Search in rotated sorted array")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        n = a.searchI(test[0], test[1])
        print(n)
        #n = a.searchI1(test[0], test[1])
        #print(n)

    testVector = [([],1),([1],1),([1],2),
                  ([3,3,1],1),([3,1,2,2,2],1),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],55),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],1),
                  ([11,22,33,44,55,1,2,3,4,5,6,7,8,9,10],30)]
    print("Search in rotated sorted array II")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        n = a.search(test[0], test[1])
        print(n)
