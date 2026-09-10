# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 2017
LeetCode problem 29
Divide two integers without using multiplication, division and mod operator.
If it is overflow, return MAX_INT.
Result is of integer type
For example,
100/3 = 33
3/100 = 0
@author: K Li
"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if(divisor==0):
            return -1
        sign = 1
        if(dividend<0):
            sign *= -1
            dividend = -dividend
        if(divisor<0):
            sign *= -1
            divisor = -divisor

        scale = 1
        divisorScaled = divisor
        while dividend>=divisorScaled:
            divisorScaled = divisorScaled<<1
            scale = scale << 1
        #print(scale, divisorScaled)
        
        nRemain = dividend
        result = 0
        while (nRemain>0) & (divisorScaled>0):
            if nRemain>=divisorScaled:
                nRemain -= divisorScaled
                result += scale
            scale = scale>>1
            divisorScaled = divisorScaled>>1
        if (sign==-1)&(result == 2**32):
            result = 2**32-1
        return sign*result

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [(0,1),(1,0),(20,-3),(-3,-10),
                  (-100,-3)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.divide(test[0], test[1])
        y = a.divide(test[0], test[1])
        print(x, y)
