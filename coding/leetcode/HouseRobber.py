# -*- coding: utf-8 -*-
"""
Created on Sat May 6, 2017
LeetCode problem 198, 213 combined
---#213
You are a professional robber planning to rob houses along a street. Each
house has a certain amount of money stashed, the only constraint stopping
you from robbing each of them is that adjacent houses have security system
connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight without
alerting the police.
---#213
After robbing those houses on that street, the thief has found himself a new
place for his thievery so that he will not get too much attention. This time,
all houses at this place are arranged in a circle. That means the first house
is the neighbor of the last one. Meanwhile, the security system for these
houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of
each house, determine the maximum amount of money you can rob tonight without
alerting the police.
@author: K Li
"""

class Solution(object):
    def rob(self, nums):
        #return self.robI(nums)
        return self.robII(nums)
    
    def robII(self, nums):
        """
        :type nums: List[int]
        :rtype: int        
        """
        N = len(nums)
        if N == 0:
            return 0
        if N == 1:
            return nums[0]
        if N==2:
            return max(nums[:2])
        # convert into robI problem.
        # if rob the first home, then robbers can't rob second and last home
        r1 = nums[0] + self.robI(nums[2:N-1])
        # if do not rob the first home, can rob all other homes
        r2 = self.robI(nums[1:])
        return max(r1,r2)

    def robI(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        at first house, robber can choose to rob it or not
        Therefore R(n) = max(r0+R(n-2), R(1))
        Forward iteration, more effective
        """
        N = len(nums)
        if N==0:
            return 0
        if N==1:
            return nums[0]
        if N==2:
            return max(nums[:2])
        f_n2 = nums[0]
        f_n1 = max(nums[:2])
        for i in range(2,N):
            result = max(f_n1, f_n2+nums[i])
            f_n1, f_n2 = result, f_n1
        return result

    def robI1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Extremely compact way of computing
        R(n) = max(r0+R(n-2), R(1))
        """
        last, now = 0, 0
        
        for i in nums:
            last, now = now, max(last + i, now)
                
        return now
    
if __name__ == '__main__':
    a = Solution()
    testVector = [[],[1],[2,1],
                  [5,2,3,6],
                  [5, 13, 11,  7,  2,  2,  5, 13, 15, 19]]
                  
    a = Solution()
    for test in testVector:
        print(test)
        print(a.robI(test))
        print(a.robII(test))
    
    test = np.random.randint(1,20,200)