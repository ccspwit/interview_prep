# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 2017
LeetCode problem 50
Implement pow(x, n). x is floating number, n is integer
Try optimize complexity
@author: K Li
"""

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        This is a more concise and efficient solution.
        1. handling of negative n
        2. Scan from LSB to MSB
        more efficient and more concise.
        """
        
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = -n

        result = 1
        nResidue = n
        power2 = x

        while nResidue > 0:
            if(nResidue & 1):   # check LSB of nResidue
                result *= power2
            power2 = power2*power2
            nResidue = nResidue>>1

        return result

    def myPow1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        Save power2 sequence of x upto 2^MSB, then scan n from MSB to LSB.
        Perform multiplication if '1'. It turns out scan from LSB to MSB is
        more efficient and more concise.
        """
        
        if n < 0:
            return 1/self.myPow(x, -1*n)
        if n == 0:
            return 1

        power2Dict = {}
        two2n = 1
        power2 = x

        while two2n <= n:
            power2Dict[two2n] = power2
            two2n *= 2
            power2 = power2*power2

        #print(power2Dict)
        result = 1
        nResidue = n

        while nResidue > 0:
            if(two2n<=nResidue):
                result *= power2Dict[two2n]
                nResidue -= two2n
            two2n  = two2n // 2

        return result

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [(2.0,0),(2.0,1),(2.0,-1),
                  (2.0,11),(2.0,-11),(2.0,60),
                  (2.0,-60)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.myPow(test[0], test[1])
        y = a.myPow1(test[0], test[1])
        print(x, y)
