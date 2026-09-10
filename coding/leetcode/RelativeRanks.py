# -*- coding: utf-8 -*-
"""
Created on May 23, 2017
LeetCode problem 506
Given scores of N athletes, find their relative ranks and the people with the
top three highest scores, who will be awarded medals: "Gold Medal",
"Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so
they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks
according to their scores.

Note:
N is a positive integer and won't exceed 10,000.
All the scores of athletes are guaranteed to be unique.
@author: K Li
"""

class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #sort and get index
        N = len(nums)
        if N==0:
            return []
        if N==1:
            return ["Gold Medal"]
        #The following statement get oriignal indices of the sorted array
        #ind = [i[0]+1 for i in sorted(enumerate(nums), key=lambda x:x[1], reverse=True)]
        #ind = sorted(range(len(nums)),key=lambda x:nums[x])
        sortArray = sorted(nums, reverse=True)
        mapping = {}
        medal = {0: 'Gold Medal', 1: 'Silver Medal', 2: 'Bronze Medal'}
        for i, n in enumerate(sortArray):
            if i in medal:
                mapping[n] = medal[i]
            else:
                mapping[n] = str(i+1)
                
        result = nums[:]
        for n in range(len(nums)):
            result[n] = mapping[nums[n]]

        return result

    def findRelativeRanks1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        #sort and get index
        N = len(nums)
        if N==0:
            return []
        if N==1:
            return ["Gold Medal"]
        #The following statement get oriignal indices of the sorted array
        #ind = [i[0]+1 for i in sorted(enumerate(nums), key=lambda x:x[1], reverse=True)]
        #ind = sorted(range(len(nums)),key=lambda x:nums[x])
        sortArray = sorted(nums, reverse=True)
        mapping = {val: str(ind+1) for ind, val in enumerate(sortArray)}
        result = nums[:]
        for n in range(len(nums)):
            pos = mapping[nums[n]]
            if pos== '1':
                result[n] = "Gold Medal"
            elif pos == '2':
                result[n] = "Silver Medal"
            elif pos == '3':
                result[n] = "Bronze Medal"
            else:
                result[n] = pos
        return result
    
if __name__ == '__main__':
    import numpy as np
	# test case to generate ListNode and run test function
    testVector = [[],[1],[1,2],[3,2,1],
                  [5,6,1,2,3,4],
                  [10,3,8,9,4],
                  [8,9,10,1,2,3,-1,0]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        test1 = test[:]
        print('Relative ranking is ',a.findRelativeRanks(test))
        print('Relative ranking is ',a.findRelativeRanks1(test))

    tc = np.random.randint(1,1000,100)