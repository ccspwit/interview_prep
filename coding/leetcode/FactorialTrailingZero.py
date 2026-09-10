# -*- coding: utf-8 -*-
"""
Created on Sat May 6, 2017
LeetCode problem 172
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.

For example:

@author: K Li
"""

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        10 can only be divided by 5, 2. So the problem will be boiled
        to count how many 10s and 5s below n. Actually count how many '5's
        below n
        """
        if n<5: return 0
        
        count5 = 0
        zeros = 0
        # count the number of 0s due to 10**n
        while n>=5:
            n = n // 5
            digit =  n % 5
            zeros = 5*zeros+1
            count5 += digit*zeros

        return count5

    def trailingZeroes1(self, n):
        """
        :type n: int
        :rtype: int
        10 can only be divided by 5, 2. So the problem will be boiled
        to count how many 10s and 5s below n. Actually count how many '5's
        below n
        """
        if n<5: return 0
        
        count5 = 0
        zeros = 0
        table5 = []
        # count the number of 0s due to 10**n
        while n>=5:
            n = n // 5
            digit =  n % 5
            zeros = 5*zeros+1
            table5.append((digit, zeros))
        #table5.append(())
        print(table5)
        count5 = sum( map(lambda x: x[0]*x[1], table5))
        return count5
        
if __name__ == '__main__':
    a = Solution()
    testVector = [1,5,10,20,30,100,1000]
                  
    a = Solution()
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        #print(test)
        print("Number of trailing zeros is %d"%a.trailingZeroes(test))
