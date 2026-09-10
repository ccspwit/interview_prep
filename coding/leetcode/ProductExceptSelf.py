# -*- coding: utf-8 -*-
"""
Created on Mon May 8, 2017
LeetCode problem 238

Given an array of n integers where n > 1, nums, return an array output such
that output[i] is equal to the product of all the elements of nums except
nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].

@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        A computational more efficient way do not need to perform division.
        """
        # compute forward and backward cumulative product
        N = len(nums)
        prod = nums[:]
        # forward cumprod
        cumProd = 1
        for n in range(N):
            if(n>0):
                cumProd *= nums[n-1]
            prod[n] = cumProd
        # backward cumprod
        cumProd = 1
        for n in range(N-1,-1,-1):
            if n<N-1:
                cumProd *= nums[n+1]
            prod[n] *= cumProd
        
        return prod
    
    def productExceptSelf1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        First calculate the product of the whole array.
        Then for each element, divide the full product by nums[i]
        Need to be careful when there is one or more '0's.
        """
        fullProduct = 1
        nZeros = 0
        zeroPos = 0
        result = nums[:]
        
        for n in range(len(nums)):
            if nums[n]!=0:
                fullProduct *= nums[n]
            else:
                nZeros += 1
                zeroPos = n
        
        for n in range(len(nums)):
            if nZeros==0:
                result[n] = fullProduct//nums[n]
            if nZeros==1:
                if(n==zeroPos):
                    result[n] = fullProduct
                else:
                    result[n] = 0
            if nZeros>1:
                result[n] = 0
        
        return result
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[1,2,3,4],
                  [1,0,2,3,4],
                  [1,2,0,0,5,6]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.productExceptSelf(test)
        print(x)
    test = sorted(random.randint(0,100,1000))
