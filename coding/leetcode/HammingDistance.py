# -*- coding: utf-8 -*-
"""
Created on May 20, 2017
LeetCode problem 461
he Hamming distance between two integers is the number of positions at which
the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.
Note:
0 ≤ x, y < 2**31.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
@author: K Li
"""

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if (x<0) or (y<0):
            raise ValueError("x, y must be non-negative.")
        if (x>=2**31) or (y>=2**31):
            raise ValueError("x, y must be less than 2**31.")
        z = x^y     # get bits that are different
        dist = 0
        while z!= 0:
            dist += 1
            z = z&(z-1)
        return dist
    
if __name__ == '__main__':
    a = Solution()
    testVector = [(0,0), (2**30,2**20),
                  (1,4),(0x7ff, 0x700)]
    a = Solution()
    for test in testVector:
        print(test)
        print("Hamming distance is ", a.hammingDistance(test[0],test[1]))

