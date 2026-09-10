# -*- coding: utf-8 -*-
"""
Created on June 4, 2017
LeetCode problem 55
Given an array of non-negative integers, you are initially positioned at the
first index of the array. Each element in the array represents your maximum
jump length at that position.

Determine if you are able to reach the last index.
For example:
A = [2,3,1,1,4], return true.
A = [3,2,1,0,4], return false.

@author: K Li
"""

class Solution(object):
    def canJump(self, nums):

        if len(nums) < 2: return True
        i = mx = 0
        while i <= mx:
            mx, i = max(mx, i+nums[i]), i + 1
            if mx >= len(nums)-1: return True
        return False

    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        From last index, scan for "0", check whether any previous element
        can jump over. 
        """
        N = len(nums)
        if N<=1:
            return True
        pos = N-2
        jumpOver = True
        while pos>=0:
            if nums[pos]>0:
                pos -= 1
            else:
                #check if any previous element can jump over
                jumpOver = False
                n = pos-1
                while n>=0:
                    #print(n, nums[n], pos, jumpOver)
                    nextPos = n+nums[n]
                    n -= 1
                    if (nextPos)>pos:
                        jumpOver = True
                        break
                pos = n
        return jumpOver

if __name__ == '__main__':
    a = Solution()
    testVector = [[1,0],[0,1],
                  [2,3,1,1,4],
                  [3,2,1,0,4],
                  [0,1,2,3,4],
                  [3,2,0,3,2,1,0,1]]
    a = Solution()
    for test in testVector:
        print(test)
        print("Can jump to the last element",(a.canJump(test)))
        print("Can jump to the last element",(a.canJump1(test)))
    
    #test = np.random.randint(0,20,20)