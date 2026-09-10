# -*- coding: utf-8 -*-
"""
Created on Sun May 7, 2017
LeetCode problem 204
Description:

Count the number of prime numbers less than a non-negative number, n.
@author: K Li
"""

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        A computation efficient, but memory inefficient method
        sieve of Eratosthenes 
        """
        if (n<=2):
            return 0
        primeTable = [True]*n
        primeTable[0] = False
        primeTable[1] = False
        for i in range(2,int(n**0.5)+1):
            if primeTable[i]:
                primeTable[i*i::i] = [False]*(((n-1)//i)-(i-1))
                #print(len(primeTable[i*i::i]), ((n-1)//i)-(i-1))
        return sum(primeTable)

if __name__ == '__main__':
    a = Solution()
    testVector = [1,5,10,20,30,100,255,1000]
                  
    a = Solution()
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        #print(test)
        print("%d, has %d prime number"%(test, a.countPrimes(test)))

