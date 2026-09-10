# -*- coding: utf-8 -*-
"""
Created on June 6, 2017
LeetCode problem 605
Suppose you have a long flowerbed in which some of the plots are planted and
some are not. However, flowers cannot be planted in adjacent plots - they
would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means
empty and 1 means not empty), and a number n, return if n new flowers can be
planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
@author: K Li
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        count number of 0s between two 1s. for m '0's, can place (m-1)//2
        flowers. Need to consider cases start with 0 or end with 0, can
        place m//2 flowers
        """
        ans = 0
        fb, N = flowerbed, len(flowerbed)
        
        last = -2
        for ind in range(N):
            if fb[ind]==1:
                #faster than the original code
                #ans+=max((ind-last-2)//2,0)
                diff = ind-last
                if diff>3:
                    ans += (diff-2)>>1
                last = ind
        if fb[N-1]==0:
            ans += max((N-1-last)//2,0)
        return ans>=n
        
if __name__ == '__main__':
    a = Solution()
    testVector = [([1,0,0,0,1],1),([1,0,0,0,1],2),
                  ([0,0,0,0,0],3),([0,0,1,0,0,0,0,1,0,0],3)]
    a = Solution()
    #testVector=[(10,11)]
    for test in testVector:
        print(test)
        print("Can place flower?",(a.canPlaceFlowers(test[0],test[1])))
    
    #test = np.random.randint(0,20,20)