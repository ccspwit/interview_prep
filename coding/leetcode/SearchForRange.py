# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 34
Given an array of integers sorted in ascending order, find the starting and
ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Hard to search simultaneously. Optimize a little
        """
        
        N = len(nums)
        if N==0:
            return [-1,-1]
        if N==1:
            return [0,0] if nums[0]==target else [-1,-1]
        l, r = 0, N-1
        # find left edge
        # Different loop solution 1
        left = -1
        while l<=r:
            mid = (l+r)//2
            if target< nums[mid]:
                r = mid-1
            elif target>nums[mid]:
                l = mid+1
            else:   #==
                left = mid
                r = mid-1
        if left==-1:
            return [-1,-1]

        # find to right edge
        # Different loop solution 2
        l, r = left, N-1
        while l<r:
            mid = (l+r+1)//2
            if target< nums[mid]:
                r = mid-1
            else:
                l = mid

        right = l

        return [left, right]
    
    def searchRange1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        Binary search left, then binary search right. The code is more clear.
        """
        def searchLeft(nums, target):
            N = len(nums)
            if N==0:
                return -1
            if N==1:
                return 0 if nums[0]==target else -1
            l, r = 0, N-1
            while l<r:
                mid = (l+r)//2
                if target< nums[mid]:
                    r = mid-1
                elif target>nums[mid]:
                    l = mid+1
                else:   #==
                    if (mid>0):
                        if (nums[mid-1]!=target):
                            return mid
                        else:
                            r = mid-1
                    else:
                        return mid
            # l>=r
            return l if nums[l]==target else -1
        
        def searchRight(nums, target):
            N = len(nums)
            if N==0:
                return -1
            if N==1:
                return 0 if nums[0]==target else -1
            l, r = 0, N-1
            while l<r:
                mid = (l+r)//2
                if target< nums[mid]:
                    r = mid-1
                elif target>nums[mid]:
                    l = mid+1
                else:   #==
                    if (mid<N-1):
                        if (nums[mid+1]!=target):
                            return mid
                        else:
                            l = mid+1
                    else:
                        return mid
            # l>=r
            return l if nums[l]==target else -1

        return [searchLeft(nums,target),searchRight(nums,target)]
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([],1),([1,1,1],1),([1,2,3,4],3),
                  ([1,1,2,3,3],1),([1,1,2,3,3],3),
                  ([1,2,3,3,3,4],3),([5,7,7,8,8,10],8)]
    for test in testVector:
        print(test)
        test1 = test[:]
        print("Possible 4 sum pairs are ", a.searchRange(test[0], test[1]))
        print("Possible 4 sum pairs are ", a.searchRange1(test[0], test[1]))

