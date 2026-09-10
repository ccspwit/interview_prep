# -*- coding: utf-8 -*-
"""
Created on Sat May 6, 2017
LeetCode problem 189
Rotate an array of n elements to the right by k steps.

For example, with n = 7 and k = 3, the array [1,2,3,4,5,6,7] is rotated to
[5,6,7,1,2,3,4].

Note:
Try to come up as many solutions as you can, there are at least 3 different
ways to solve this problem.
@author: K Li
"""

class Solution(object):
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        Use O(k) memory to save the first k elements
        """
        N = len(nums)
        if N==0:
            return
        # make sure k is between 0, N-1
        k = k%N
        # save the last k samples
        tmpArray = nums[N-k:]
        # copy the first N-k samples to the right by k, from N-k-1 to 0
        for n in range(N-k-1,-1,-1):
            nums[n+k] = nums[n]

        # copy last k samples to the begining
        for n in range(k):
            m = (n+k) %N
            nums[n] = tmpArray[n]
        return

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        Multiple in place reversing, complexity O(kN), memory O(1)
        """
        def inverseIP(nums, left, right):
            N = right - left + 1
            if N<=1:
                return
            while left<right:
                tmp = nums[right]
                nums[right] = nums[left]
                nums[left] = tmp
                right -= 1
                left += 1
            return
        
        N = len(nums)
        if N==0:
            return
        # make sure k is between 0, N-1
        k = k%N
        inverseIP(nums, 0, N-1)
        inverseIP(nums, 0, k-1)
        inverseIP(nums, k, N-1)
        return
            
if __name__ == '__main__':
    a = Solution()
    testVector = [([],2),
                  ([1,2],1),
                  ([2,3,4],6),
                  ([1,2,3,4,5,6,7],3),
                  ([1,2,3,4,5],-1)]
                  
    a = Solution()
    for test in testVector:
        print("Original array is: ", test[0])
        print("List shift to right by %d is -----"%test[1])
        a.rotate(test[0], test[1])
        print(test[0])
    
    #test = np.random.randint(0,20,20)