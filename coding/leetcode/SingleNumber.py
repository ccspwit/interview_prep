# -*- coding: utf-8 -*-
"""
Created on Thu May 4 2017
Leetcode 136, 137 combined
---#136
Given an array of integers, every element appears twice except for one.
Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?

---#137
Given an array of integers, every element appears three times except for one,
which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement
it without using extra memory?
@author: K Li
"""

class Solution(object):
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Assume input has every element appears exactly twice except for one.
        """
        # One line solution #1
        # return sum(set(nums))*2-sum(nums)
        # One line solution #2
        #from functools import reduce
        #return reduce(lambda a,b: a^b, nums)
        ini = 0
        for n in nums:
            ini = ini^n
        return ini

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Assume input has every element appears three times except for one.
        Assume elements of nums array are nonnegative.
        The basic idea is that we build the result bit by bit.
        If we sum each bit[i] across the input, we will get 
        3 * (x1 + x2 + x3 + ...+xn-1) + xn where x1 to xn-1 are unqiue
        numbers with frequency 3. Take a mod with 3 to get final answer.
        """
        
        result = 0
        for nShift in range(32):
            bitSum = 0
            for n in nums:
                bitSum += (n>>nShift)&1
            result += (bitSum%3)<<nShift
        if result>=(2**31):
            result -= 2**32
        return result
        """
        If we see one number the counter should be 1, if we see two numbers
        the counter should be 2, and if we see 3 numbers the counter should
        loop back to 0. In order to have these 3 states we need 2 bits,
        hence a and b. Below is the transition table, and the code follows
        from it.
        a = b = 0
        for n in nums:
            b = (b^n)&~a
            a = (a^n)&~b
        return b
        """
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[1,1,1,-2],[1,2,3,3,2,1,1,2,3,4],[-2,-2,1,1,-3,1,-3,-3,4,-2]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print(a.singleNumber(test))
    test = list(random.randint(0,10000,1000))
    