# -*- coding: utf-8 -*-
"""
Created on Thu May 1st 2017
LeetCode problem 70
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can
you climb to the top?

Note: Given n will be a positive integer.
@author: K Li
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        It turns out the result is Fibonacci2 sequence
        X(n) = X(n-1) + X(n-2)
        """
        
        if n <= 0:
            return 0
        if n <= 2:
            return n
        X_2, X_1 = 1, 2
        for i in range(3, n+1):
            X = X_1 + X_2
            X_2, X_1 = X_1, X
        return X

    def climbStairs1(self, n):
        """
        :type n: int
        :rtype: int
        Sum of combination of position for all possible number of '2's.
        """
        
        if n <= 0:
            return 0
        if n == 1:
            return 1
        
        maxTwos = n//2
        nWays = 0
        for nTwos in range(maxTwos+1):
            nOnes = n - 2* nTwos
            N = nOnes + nTwos
            numerator, denominator = 1, 1
            for k in range(N+1-nTwos,N+1):
                numerator *= k
                denominator *= (N+1-k)
            combination  = numerator // denominator
            nWays += combination
            #print(nTwos, combination)
        return nWays

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [2,4,6,8,9]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.climbStairs(test)
        print(x)
        x = a.climbStairs1(test)
        print(x)
    random.seed(0)
    test = random.randint(-1000,1000,500)
    #x = a.threeSum(test)
