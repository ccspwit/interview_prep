# -*- coding: utf-8 -*-
"""
Created on Thu May 1st 2017
LeetCode problem 69
Implement int sqrt(int x). Compute and return the square root of x.
@author: K Li
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        Apply Newton's method
        r*r - x = 0
        x_{n+1} = x_n - f(x_n)/f'(x_n)
        """
       
        r = x
        while (r*r) > x:
            r = (r+x//r)//2
            #print(r)
        return r

    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        Binary search
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        lower, upper = 1, (x+2)//2
        while lower < upper:
            mid = (lower+upper)>>1
            if (mid*mid) > x:
                upper = mid
            elif (mid*mid) < x:
                if lower == mid:
                    lower = mid+1
                else:
                    lower = mid
            else:
                break
        return mid

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [0,1,2,4,6,8,9,10,15,16,17]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.mySqrt(test)
        print(x)
        x = a.mySqrt1(test)
        print(x)
    random.seed(0)
    test = random.randint(-1000,1000,500)
    #x = a.threeSum(test)
