# -*- coding: utf-8 -*-
"""
Created on May 16th, 2017
LeetCode problem 374, 375
---#374
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number is higher or lower.
You call a pre-defined API guess(int num) which returns 3 possible results
(-1, 1, or 0):

-1 : My number is lower
 1 : My number is higher
 0 : Congrats! You got it!
Example:
n = 10, I pick 6.
Return 6.

---#375
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I'll tell you whether the number I picked is
higher or lower.
However, when you guess a particular number x, and you guess wrong, you pay
$x. You win the game when you guess the number I picked.

Example:
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.
Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to
guarantee a win.
@author: K Li
"""
def guess(num):
    """
    """
    global pick
    if num<pick:    # pick is larger
        return 1
    if num>pick:    # pick is lower
        return -1
    if num==pick:
        return 0

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=1:
            return 1
        left, right = 1, n
        while left<right:
            mid = (left+right)//2
            if guess(mid)==1:
                left = mid+1
            elif guess(mid)==-1:
                right = mid-1
            else:
                return mid
        return left

    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        Need to devise guessing strategy. 
        one number, penalty is 0 since we always guess right
        two numbers, guess small number first, lower penalty
        three numbers, guess middle number first, if wrong, from feedback
        from guess, will know the answer. Penalty is mid-number
        more than 3 numbers, need to iterate all possible seperating point k
        DP(lo, hi) = k + max(DP(lo, k-1),DP(k+1,hi)) to find argmin_k
        Iterative solution
        """
        """   INCOMPLETE CODE   """
        cost = [[float('inf')]*(n+1) for _ in range(n+1)]
        for i in range(1,n):
            for j in range(1, n-i+1):
                for mid in range(j, i+j):
                    #print(j, i+j,mid)
                    cost[j][i+j] = min(
                            cost[j][i+j], max(cost[j][mid-1], cost[mid+1][i+j])+mid)
        
        return cost

    def getMoneyAmountR(self, n):
        """
        :type n: int
        :rtype: int
        Need to devise guessing strategy. 
        one number, penalty is 0 since we always guess right
        two numbers, guess small number first, lower penalty
        three numbers, guess middle number first, if wrong, from feedback
        from guess, will know the answer. Penalty is mid-number
        more than 3 numbers, need to iterate all possible seperating point k
        DP(lo, hi) = k + max(DP(lo, k-1),DP(k+1,hi)) to find argmin_k
        Recursive solution
        """
        def cost(lo, hi, cache):
            if hi <= lo:
                return 0
            if cache[lo][hi] != float('inf'):
                return cache[lo][hi]
            for k in range(lo, hi+1):
                temp = k+max(cost(lo,k-1,cache), cost(k+1,hi,cache))
                cache[lo][hi] = min(temp, cache[lo][hi])
            return cache[lo][hi]

        min_money = [[float('inf')]*(n+1) for _ in range(n+1)]
        return cost(1, n, min_money)

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    N = 10
    testVector = [1,2,3,4,5,6,7,8,9,99,100]
    a = Solution()
    print('Contains duplicate I')
    for pick in range(1,N+1):
        #print('Test case %d-----------'%i)
        print(N, pick)
        print(a.guessNumber(N))
    
    #print("Need $%d to win."%a.getMoneyAmount(N))

