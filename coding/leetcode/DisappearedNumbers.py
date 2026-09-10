# -*- coding: utf-8 -*-
"""
Created on May 19, 2017
LeetCode problem 448
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some
elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the
returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
@author: K Li
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Negative indexing method
        For each number i in nums, we mark the number that i points as negative.
        Then we filter the list, get all the indexes who points to a positive number.
        Since those indexes are not visited.
        """
        N = len(nums)
        if N <= 1:
            return []
        result = []
        for n in range(N):
            val1 = nums[n]
            ind = val1-1 if val1>0 else -1-val1
            val2 = nums[ind]
            nums[ind] = -val2 if val2>0 else val2

        for n in range(N):
            if nums[n]>0:
                result.append(n+1)
        return result

    def findDisappearedNumbers1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Swapping method        
        """
        N = len(nums)
        if N <= 1:
            return []
        result = []
        for n in range(N):
            while nums[n] != n+1:
                nums[nums[n]-1], nums[n] = nums[n], nums[nums[n]-1]
                if nums[nums[n]-1] == nums[n]:
                    break

        for n in range(N):
            if nums[n] != n+1:
                result.append(n+1)
        return result
    
    def findDisappearedNumbers2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Negative indexing method
        For each number i in nums, we mark the number that i points as negative.
        Then we filter the list, get all the indexes who points to a positive number.
        Since those indexes are not visited.
        """
        N = len(nums)
        if N <= 1:
            return []
        result = []
        for n in range(N):
            ind = abs(nums[n])-1
            nums[ind] = -abs(nums[ind])
        return [i+1 for i in range(N) if nums[i]>0]

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[],[1],[1,1,],[2,2],
                  [4,3,2,7,8,2,3,1],
                  [1,1,2,2]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        test1 = test[:]
        print('The missing numbers are: ',a.findDisappearedNumbers(test))
        print('The missing numbers are: ',a.findDisappearedNumbers1(test1))

    t = list(range(1,1000))
    t[100] = 999