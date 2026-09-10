# -*- coding: utf-8 -*-
"""
Created on Mon May 8, 2017
LeetCode problem 367
Given a positive integer num, write a function which returns True
if num is a perfect square else False.
@author: K Li
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=0:
            return False
        if num==1:
            return True
        low, high = 0, num//2+1
        while low<high:
            mid = (low+high)//2
            if low == mid:
                return low*low==num
            #print(low,mid,high)
            square = mid*mid
            if square==num:
                return True
            elif square>num:
                high = mid
            else:
                low = mid
        return False
        
if __name__ == '__main__':
    a = Solution()
    testVector = list(range(1000))
                  
    a = Solution()
    for test in testVector:
        if a.isPerfectSquare(test):
            print(np.sqrt(test))
    
    test = np.random.randint(1,20,200)