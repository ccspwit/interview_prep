# -*- coding: utf-8 -*-
"""
Created on May 26, 2017
LeetCode problem 575
Given an integer array with even length, where different numbers in this
array represent different kinds of candies. Each number means one candy of
the corresponding kind. You need to distribute these candies equally in
number to brother and sister. Return the maximum number of kinds of candies
the sister could gain.

Example 1:
Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for
each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has
candies [1,2,3], too. 
The sister has three different kinds of candies. 

Example 2:
Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has
candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind
of candies. 
Note:

The length of the given array is in range [2, 10,000], and will be even.
The number in given array is in range [-100,000, 100,000].
@author: K Li
"""

class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        min(len(candies)//2, len(set(candies)))
        More concise code
        """
        return min(len(candies)//2, len(set(candies)))
        
    def distributeCandies1(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        min(len(candies)//2, len(set(candies)))
        """
        N = len(candies)
        if N&1!=0:
            raise ValueError("The length of array must be even number")
        n = len(set(candies))
        if (n>=N//2):
            return N//2
        else:
            return n

if __name__ == '__main__':
    import numpy as np
	# test case to generate ListNode and run test function
    testVector = [[1,1],[2,1],
                  [1,1,2,3],[1,1,2,2,3,3],
                  [1,1,2,2,3,3,4,5,6,7],
                  [1,1,1,1,1,2,2,3]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Types of candies is ',a.distributeCandies(test))
        print('Types of candies is ',a.distributeCandies1(test))

    tc = np.random.randint(1,1000,100)