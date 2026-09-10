# -*- coding: utf-8 -*-
"""
Created on May 28, 2017
LeetCode problem 31
Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its
corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
@author: K Li
"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if N<=1:
            return

        pseFound = False
        for n in range(N-2,-1,-1):
            if nums[n]<nums[n+1]:
                pseFound = True
                break

        if pseFound:
            left = n
            minPos, minVal = n+1, nums[n+1]
            for n in range(left+2,N):
                if (nums[n]>nums[left])&(nums[n]<minVal):
                    minVal = nums[n]
                    minPos = n

            #print(left, minPos)
            nums[left], nums[minPos] = nums[minPos], nums[left]
            nums[left+1:] = sorted(nums[left+1:])
            return
        else:
            # if no PSE found, meaning in reverse order
            # no need to sort, just reverse
            nums.reverse()
            return

    def nextPermutation1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        This method is a little hard to understand
        """
        # Use two-pointers: two pointers start from back
        # first pointer j stop at descending point
        # second pointer i stop at value > nums[j]
        # swap and sort rest
        if not nums: return None
        i = len(nums)-1
        j = -1 # j is set to -1 for case `4321`, so need to reverse all in following step
        while i > 0:
            if nums[i-1] < nums[i]: # first one violates the trend
              j = i-1
              break
            i-=1
        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[j]: # 
                nums[i], nums[j] = nums[j], nums[i] # swap position
                nums[j+1:] = sorted(nums[j+1:]) # sort rest
                return
            
if __name__ == '__main__':
    a = Solution()
    testVector = [[],[1],[1,2,3],[3,2,1],
                  [1,4,5,3,2,1],[1,6,5,3,5,4,1]]
    for test in testVector:
        print(test)
        test1 = test[:]
        a.nextPermutation(test)
        print("Next permutation is ", test)
        a.nextPermutation1(test1)
        print("Next permutation is ", test1)

