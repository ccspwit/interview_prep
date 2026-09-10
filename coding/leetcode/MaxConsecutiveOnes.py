# -*- coding: utf-8 -*-
"""
Created on May 20, 2017
LeetCode problem 485
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
@author: K Li
"""

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        The code is more clear and concise.
        """
        N = len(nums)
        if N==0:
            return 0
        maxN = 0
        count = 0
        for n in nums:
            if n==1:
                count += 1
                if count > maxN:
                    maxN = count
            else:
                count = 0
        return maxN

    def findMaxConsecutiveOnes1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        The code is a bit too complicated
        """
        N = len(nums)
        if N==0:
            return 0
        maxN = 0
        start, end = -1, -1
        for ind, val in enumerate(nums):
            if val==0:
                if end>start:
                    maxN = max(maxN, end-start)
                start = ind
            else:
                end = ind

        if end>start:
            maxN = max(maxN, end-start)
        
        return maxN
    
if __name__ == '__main__':
    import numpy as np
	# test case to generate ListNode and run test function
    testVector = [[],[1],[1,1],[0,0],
                  [1,1,0,1,1,1,0],
                  [1,1,1,0,0,1,1,0,1,1,1,1]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        test1 = test[:]
        print('Max consecutive \'1\' is ',a.findMaxConsecutiveOnes(test))
        print('Max consecutive \'1\' is ',a.findMaxConsecutiveOnes1(test))

    tc = np.random.randint(1,100,20)