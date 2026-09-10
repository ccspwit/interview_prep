# -*- coding: utf-8 -*-
"""
Created on Fri May 5, 2017
LeetCode problem 167
Given an array of integers that is already sorted in ascending order,
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they
add up to the target, where index1 must be less than index2. Please note that
your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution and you may not
use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
@author: K Li
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        Use two pointer method, easy to understand.
        May employ two pointer combined with binary search. But the code will
        be much harder to read.
        """
        N = len(numbers)
        left, right = 0, N-1
        while left < right:
            curSum = numbers[left]+numbers[right]
            if curSum == target:
                return [left+1, right+1]
            elif curSum < target:
                left += 1
            else:
                right -= 1
        return []

if __name__ == '__main__':
    a = Solution()
    testVector = [([2,3,4],6),
                  ([2,7,11,15],9),
                  ([1,2,3,4,5],8)]
                  
    a = Solution()
    for test in testVector:
        print(test)
        print("The index of element with sum {} is {}".format(
                test[1], a.twoSum(test[0], test[1])))
    
    test = np.random.randint(0,20,20)