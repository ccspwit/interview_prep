# -*- coding: utf-8 -*-
"""
Created on Sat May 6, 2017
LeetCode problem 169
Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.

@author: K Li
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Boyer-Moore Algorithm
        """
        count = 0
        #majority = nums[0]
        for x in nums:
            if count == 0:
                majority = x
            if majority == x:
                count += 1
            else:
                count -= 1
        return majority
        
if __name__ == '__main__':
    a = Solution()
    testVector = [[1],[1,1],[1,2,2],
                  [4,4,2,4,4,3,3,3,3,4,4],
                  [1,2,3,3,3,4,4,4,4,4,4]]
                  
    a = Solution()
    for test in testVector:
        print(test)
        print("Majority element is {}".format(a.majorityElement(test)))
