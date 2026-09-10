# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 2017
LeetCode problem 16
Given an array S of n integers, find three integers in S such that the sum
is closest to a given number, target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

For example, given array S = {-1 2 1 -4}, and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Sort nums first, pick first numbers
        Then scan through the list from left and right.
        Optimize on iteration/loop parameters, better performance
        """
        
        N = len(nums)
        if N<3:
            return 0

        result = sum(nums[:3])
        minDiff = abs(target-result)
        nums.sort()     # O(nlogn)
        
        for i in range(N-2):
            left, right = i+1, N-1
            while left < right:
                threeSum = nums[i]+nums[left]+nums[right]
                diff = threeSum - target
                '''if(abs(diff)<minDiff):
                    minDiff = abs(diff)
                    result = threeSum'''
                if(diff>0): # decrease value
                    right -= 1
                    if(diff<minDiff):
                        minDiff = diff
                        result = threeSum
                elif(diff<0):
                    left += 1
                    if((-diff)<minDiff):
                        minDiff = -diff
                        result = threeSum
                else:
                    return target
        #print(test)
        return result

    def threeSumClosest1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Sort nums first, pick first numbers
        Then scan through the list from left and right.
        """
        
        N = len(nums)
        if N<3:
            return 0
        if N==3:
            return sum(nums)

        minDiff = abs(target-sum(nums[:3]))+1
        nums.sort()     # O(nlogn)
        
        for i in range(N):
            left, right = 0, N-1
            while left < right:
                if (left==i):
                    left += 1
                    continue
                if (right==i):
                    right -= 1
                    continue
                threeSum = nums[i]+nums[left]+nums[right]
                diff = threeSum - target
                if(abs(diff)<minDiff):
                    minDiff = abs(diff)
                    threeTuple = (nums[i],nums[left], nums[right])
                if(diff>0): # decrease value
                    right -= 1
                elif(diff<0):
                    left += 1
                else:
                    return target
        #print(test)
        return sum(threeTuple)

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([-1, 0, 1, 2, -1, -4],0),
                  ([-1,2,-3,4,-5,6],10),
                  ([-1,1,-1,1,2,2],-2)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.threeSumClosest(test[0], test[1])
        print(x)
    random.seed(0)
    test = random.randint(-1000,1000,400)
    #x = a.threeSumClosest(test)