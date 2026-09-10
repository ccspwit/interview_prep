# -*- coding: utf-8 -*-
"""
Created on May 18, 2017
LeetCode problem 414
Given a non-empty array of integers, return the third maximum number in this
array. If it does not exist, return the maximum number. The time complexity
must be in O(n).

Example 1:
Input: [3, 2, 1]
Output: 1
Explanation: The third maximum is 1.

Example 2:
Input: [1, 2]
Output: 2
Explanation: The third maximum does not exist, so the maximum (2) is returned
instead.

Example 3:
Input: [2, 2, 3, 1]
Output: 1
Explanation: Note that the third maximum here means the third maximum distinct
number. Both numbers with value 2 are both considered as second maximum.
@author: K Li
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        a little more concise
        """
        N = len(nums)
        if N==1:
            return nums[0]
        if N==2:
            return max(nums)
        # save 3 largest number
        minusINF = float('-inf')
        store = [minusINF]*3
        for n in nums:
            if n> store[2]:
                # new largest
                store = [store[1], store[2], n]
            elif (n<store[2]) & (n>store[1]):
                # new second largest
                store = [store[1], n, store[2]]
            elif (n<store[1]) & (n>store[0]):
                store[0] = n
                
        if minusINF in store:
            return store[2]
        else:
            return store[0]

    def thirdMax1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==1:
            return nums[0]
        if N==2:
            return max(nums)
        # save 3 largest number
        minusINF = float('-inf')
        store = [minusINF]*3
        for n in nums:
            if n> store[2]:
                # new largest
                store[0], store[1] = store[1], store[2]
                store[2] = n
            elif (n<store[2]) & (n>store[1]):
                # new second largest
                store[0] = store[1]
                store[1] = n
            elif (n<store[1]) & (n>store[0]):
                store[0] = n
                
        if (store[0]==minusINF) | (store[1]==minusINF):
            return store[2]
        else:
            return store[0]
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[0],[1],[0,0,0],
                  [3,2,1],[2,2,3],
                  [1,2,3,4,3,1],
                  [0,1,2,3,4,5,6,0],
                  [1,2,3,4,5,6,7,8,9,0],
                  [0,1,2,3,4,5,6,6,6,4,4]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        
        print('3rd largest unique number is ... ',a.thirdMax(test))

