# -*- coding: utf-8 -*-
"""
Created on June 4, 2017
LeetCode problem 464
n the "100 game," two players take turns adding, to a running total, any
integer from 1..10. The player who first causes the running total to reach
or exceed 100 wins.

What if we change the game so that players cannot re-use integers?
For example, two players might take turns drawing from a common pool of
numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal,
determine if the first player to move can force a win, assuming both players
play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and
desiredTotal will not be larger than 300.

Example
Input:
maxChoosableInteger = 10
desiredTotal = 11
Output:
false
Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from
2 up to 10. The second player will win by choosing 10 and get a total = 11,
which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will
always win.

@author: K Li
"""

class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        DFS search and bitmap mask, almost like a hard problem
        """
        def searchPlay(nums, target, choosableState):
            """DFS
            True represent win
            """
            # stop recursion
            if nums[-1]>=target:
                return True
            '''if sum(nums)<target:
                return False'''
            if choosableState in self.cache:
                return self.cache[choosableState]
            for n in range(len(nums)):
                val = nums[n]
                nextState = choosableState^(1<<(val-1))
                #print(bin(choosableState))
                nextPlay = searchPlay(nums[:n]+nums[n+1:], target-val, nextState)
                if not nextPlay:
                    self.cache[choosableState] = True
                    return True

            self.cache[choosableState] = False
            return False
        
        numbers = list(range(1,maxChoosableInteger+1))
        if sum(numbers) < desiredTotal:
            return False
        self.cache = {}
        return searchPlay(numbers, desiredTotal, 2**(maxChoosableInteger+1)-1)
    
if __name__ == '__main__':
    a = Solution()
    testVector = [(10,11),(15,115),
                  (20,200)]
    a = Solution()
    #testVector=[(10,11)]
    for test in testVector:
        print(test)
        print("Can you win?",(a.canIWin(test[0],test[1])))
    
    #test = np.random.randint(0,20,20)