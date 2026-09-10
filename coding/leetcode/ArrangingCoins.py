# -*- coding: utf-8 -*-
"""
Created on May 18, 2017
LeetCode problem 441
You have a total of n coins that you want to form in a staircase shape,
where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.

@author: K Li
"""

class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=1
        #if n==1:return 1
        while(n>=i):
            n=n-i
            i+=1
        return (i-1)

    def arrangeCoins1(self, n):
        """
        :type n: int
        :rtype: int
        Math solution: Sum from 1 to m is m(m+1)/2
        Solve equation m(m+1)=2n, m^2+m-2n=0
        ax^2+bx+c=0 have roots (-b$\pm$sqrt(b^2-4ac))/2a
        Therefore we have ((8n+1)**0.5-1)/2
        """
        return int(((8*n+1)**0.5-1)/2)
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [0,1,5,8,55,250,1000]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test, a.arrangeCoins(test))
        print(test, a.arrangeCoins1(test))
        

