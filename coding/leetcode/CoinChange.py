# -*- coding: utf-8 -*-
"""
Created on June 12, 2017
LeetCode problem 200
You are given coins of different denominations and a total amount of money
amount. Write a function to compute the fewest number of coins that you need
to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

Example 1:
coins = [1, 2, 5], amount = 11
return 3 (11 = 5 + 5 + 1)

Example 2:
coins = [2], amount = 3
return -1.

Note:
You may assume that you have an infinite number of each kind of coin.
@author: K Li
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        BFS solution, faster than DP
        """
        if amount == 0:
            return 0
        N = len(coins)
        value = [0]
        #coins.sort()
        visited = [False for n in range(amount+1)]
        visited[0] = True
        nCoins = 0
        
        while value:
            nCoins += 1
            nextVal = []
            for val in value:
                for coin in coins:
                    newVal = val+coin
                    if newVal == amount:
                        return nCoins
                    elif newVal>amount:
                        continue
                    elif not visited[newVal]:
                        visited[newVal] = True
                        nextVal.append(newVal)
                value = nextVal
                
        return -1

    def coinChange1(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        Dynamic prorgamming
        """
        '''if amount == 0:
            return 0'''
        N = len(coins)
        #coins.sort()
        dp = [amount+1 for n in range(amount+1)]
        dp[0] = 0
        for i in range(amount+1):
            for j in range(N):
                if coins[j]<=i:
                    dp[i] = min(dp[i], dp[i-coins[j]]+1)

        return dp[amount] if dp[amount]<=amount else -1
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([1],0),([1],3),([1,2,5],11),
                  ([1,2,5,10],12345),([186,419,83,408],6249)]
    a = Solution()
    #testVector = [[10,3,4,11,12,13]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print("Number of coins is ",a.coinChange(test[0],test[1]))

