# -*- coding: utf-8 -*-
"""
Created on Thu May 1st 2017
LeetCode problem 66
Given a non-negative integer represented as a non-empty array of digits,
plus one to the integer. You may assume the integer do not contain any
leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the
head of the list.

@author: K Li
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Use list[::-1] to reverse a list
        """
        
        result = []
        carry = 0
        digits[-1] += 1
        for digit in digits[::-1]:
            sumDigit = digit+carry
            if(sumDigit>=10):
                sumDigit -= 10
                carry = 1
            else:
                carry = 0
            result.append(sumDigit)
        if carry:
            result.append(carry)
        return result[::-1]


if __name__ == '__main__':
    a = Solution()
    testVector = [[0],[1,2,3,4],
                  [9,9,9],
                  [1,2]]
    a = Solution()
    for test in testVector:
        print(test)
        print(a.plusOne(test))
    
    test = np.random.randint(0,20,20)