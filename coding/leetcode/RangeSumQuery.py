# -*- coding: utf-8 -*-
"""
Created on May 15th, 2017
LeetCode problem 303
Given an integer array nums, find the sum of the elements between indices
i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:
You may assume that the array does not change.
There are many calls to sumRange function.
@author: K Li
"""

class NumArray(object):
    """
    Precompute cumulative sum of the array. Then range sum i, j will be
    cumsum(j+1)-cumsum(i), cumsum(0) = 0
    Complexity: O(1) time and O(n) space
    """
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cumsum = [0]+nums[:]
        N = len(nums)
        for n in range(1,N+1):
            self.cumsum[n] = self.cumsum[n-1]+nums[n-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i>j:
            return 0
        else:
            return self.cumsum[j+1]-self.cumsum[i]

        
# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[0,0],[1,1],[0,2],
                  [3,2],[2,5],[0,5]]
    a = NumArray([0,1,2,3,4,5,6,7])
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Range sum is ', a.sumRange(test[0],test[1]))

