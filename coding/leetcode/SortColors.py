# -*- coding: utf-8 -*-
"""
Created on June 5, 2017
LeetCode problem 75
Given an array with n objects colored red, white or blue, sort them so that
objects of the same color are adjacent, with the colors in the order red,
white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
@author: K Li
"""

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        One pass inplace solution.
        """
        red, white, blue = 0, 0, len(nums)-1
        
        while white <= blue:
            if nums[white] == 0:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] == 1:
                white += 1
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
        return
    
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Two pass solution is actually very effective. First pass count # of
        0/1/2. The second pass fill accordingly.
        """
        N = len(nums)
        Zeros, Ones, Twos = 0, 0, 0
        for n in nums:
            if n==0:
                Zeros += 1
            elif n==1:
                Ones += 1
            else:
                Twos += 1
        for n in range(Zeros):
            nums[n] = 0
        for n in range(Zeros, Zeros+Ones):
            nums[n] = 1
        for n in range(Zeros+Ones, N):
            nums[n] = 2
        return
    
if __name__ == '__main__':
    a = Solution()
    testVector = [[0],[1],[0,1,2,2,1,0],
                  [1,0,2,1,0,2,1,0]]
    a = Solution()
    for test in testVector:
        print(test)
        test1 = test[:]
        a.sortColors(test)
        a.sortColors1(test1)
        print("Sorted colors are ",(test))
        print("Sorted colors are ",(test1))
    
    #test = np.random.randint(0,20,20)