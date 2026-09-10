# -*- coding: utf-8 -*-
"""
Created on Thu May 4 2017
Leetcode 121, 122 combined
---#121
Say you have an array for which the ith element is the price of a given stock
on day i. If you were only permitted to complete at most one transaction
(ie, buy one and sell one share of the stock), design an algorithm to find
the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5

max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger
than buying price)
Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0

In this case, no transaction is done, i.e. max profit = 0.

---#122
Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (ie, buy one and sell one share of the stock multiple
times). However, you may not engage in multiple transactions at the same time
(ie, you must sell the stock before you buy again).
@author: K Li
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return self.maxProfit1(prices)
        return self.maxProfitN(prices)

    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        You are only allowed to make at most one trade
        """
        N = len(prices)
        if N<=1:
            return 0
        result = 0
        low, high = prices[0], prices[0]
        index = 1
        
        while index<N:
            num = prices[index]
            if num < low:
                low, high = num, num
            if num > high:
                high  = num
            if low < high:
                profit = high - low
                if profit > result:
                    result = profit
                
            index += 1
        return result
                
    def maxProfitN(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        You are only allowed to make as many trades possible. But need to
        sell before you buy.
        """
        N = len(prices)
        if N<=1:
            return 0
        result, curProfit = 0, 0
        low, high = prices[0], prices[0]
        index = 1
        
        while index<N:
            num = prices[index]
            if num < low:
                low, high = num, num
            if num > high:
                high  = num
                curProfit = high - low
            else:
                result += curProfit
                curProfit = 0
                low, high = num, num                
            index += 1
        result += curProfit
        return result
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[1],[1,2,3,4,5],
                  [7, 6, 4, 3, 1],
                  [3,6,4,7,2,1,5],
                  [7, 1, 5, 3, 6, 4]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Maximum profit with at most one trade')
        print(a.maxProfit1(test))
        print('Maximum profit with as many trades possible')
        print(a.maxProfitN(test))
