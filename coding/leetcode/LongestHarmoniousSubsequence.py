# -*- coding: utf-8 -*-
"""
Created on May 26, 2017
LeetCode problem 594
We define a harmonious array is an array where the difference between its
maximum value and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest
harmonious subsequence among all its possible subsequences.

Example 1:
Input: [1,3,2,2,5,2,3,7]
Output: 5
Explanation: The longest harmonious subsequence is [3,2,2,2,3].
Note: The length of the input array will not exceed 20,000.
@author: K Li
"""

class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        N = len(nums)
        if N<=1:
            return 0
        posMap = {}
        for ind, val in enumerate(nums):
            posMap[val] = posMap.get(val, 0)+1
        
        maxLen = 0
        for val in sorted(posMap):
            if val+1 in posMap:
                maxLen = max(maxLen, posMap[val]+posMap[val+1])
        return maxLen

if __name__ == '__main__':
    import numpy as np
	# test case to generate ListNode and run test function
    testVector = [[1],[1,1],[1,2,2,1],[1,2,3,4,5,6],
                  [1,3,2,2,5,2,3,7],
                  [1,2,3,3,2,1,4,3,2,0]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Shortest Unsorted Continous Subarray: ',a.findLHS(test))

    tc = np.random.randint(1,10000,1000)