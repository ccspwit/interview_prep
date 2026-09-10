# -*- coding: utf-8 -*-
"""
Created on May 28, 2017
LeetCode problem 553
Given a list of positive integers, the adjacent integers will perform the
float division. For example, [2,3,4] -> 2 / 3 / 4.

However, you can add any number of parenthesis at any position to change
the priority of operations. You should find out how to add parenthesis to
get the maximum result, and return the corresponding expression in string
format. Your expression should NOT contain redundant parenthesis.

Example:
Input: [1000,100,10,2]
Output: "1000/(100/10/2)"
Explanation:
1000/(100/10/2) = 1000/((100/10)/2) = 200
However, the bold parenthesis in "1000/((100/10)/2)" are redundant, 
since they don't influence the operation priority. So you should return
"1000/(100/10/2)". 

Other cases:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2
Note:

The length of the input array is [1, 10].
Elements in the given array will be in range [2, 1000].
There is only one optimal division for each test case.
@author: K Li
"""

class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        N = len(nums)
        if N==0:
            return ""
        if N==1:
            return str(nums[0])
        strings = map(str, nums)
        if N<=2:
            return "/".join(strings)
        else:
            return "{}/({})".format(next(strings), "/".join(strings))
    
if __name__ == '__main__':
    a = Solution()
    testVector = [[],[1],[1,2],
                  [1000,100,10,2],[1,2,3,4,5,6]]
    for test in testVector:
        print(test)
        test1 = test[:]
        print("Optimal division is ", a.optimalDivision(test))

