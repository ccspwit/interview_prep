# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 2017
LeetCode problem 53, 152 combined
---#53
Find the contiguous subarray within an array (containing at least one number)
which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

If you have figured out the O(n) solution, try coding another solution using
the divide and conquer approach, which is more subtle.

---#152
Find the contiguous subarray within an array (containing at least one number)
which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
@author: K Li
"""

class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N==0:
            return 0
        if N==1:
            return nums[0]
        maxProd = nums[0]
        minProd = nums[0]
        result = nums[0]
        for n in range(1,N):
            ni = nums[n]
            curMax = max(ni, maxProd*ni, minProd*ni)
            curMin = min(ni, maxProd*ni, minProd*ni)
            maxProd, minProd = curMax, curMin
            #print(ni, maxProd, minProd)
            result = max(maxProd, result)        
        return result
        
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if(N==0):
            return None
        if(N==1):
            return nums[0]

        cumsum = 0
        maxSum = nums[0]
        for i in range(N):
            ni = nums[i]
            if (cumsum<0):
                if (ni>cumsum):
                    cumsum = ni
            else:   #cumulated sum >= 0
                cumsum += ni
            if cumsum > maxSum:
                maxSum = cumsum

        return maxSum

    def maxSubArray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if(N==0):
            return None
        if(N==1):
            return nums[0]
        #maxL, maxR = 0, 0
        left, right = 0, 0
        cumsum = 0
        maxSum = nums[0]
        for i in range(N):
            ni = nums[i]
            if (cumsum<0):
                if (ni>=0):
                    left = i
                    right = i
                    cumsum = ni
                else:
                    if ni>cumsum:
                        left = i
                        right = i
                        cumsum = ni
            else:   #cumulated sum >= 0
                cumsum += ni
                right = i
            if cumsum > maxSum:
                maxSum = cumsum
                #maxL, maxR = left, right

        return maxSum

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[-1, 0, 1, 2, -1, -4],
                  [2,-1,2,-3,4],
                  [-1,2,-3,4,-5,6],
                  [-1,1,-1,1,2,2],
                  [-2,-4,6,0,8,-7,0,-5,2],
                  [-2,-4,6,0,8,-7,1,-5,2]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.maxSubArray(test)
        print(x)
        #x = a.maxSubArray1(test)
        x = a.maxProduct(test)
        print(x)
    #random.seed(0)
    #test = random.randint(-1000,1000,500)
    #x = a.threeSum(test)
