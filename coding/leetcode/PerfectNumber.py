# -*- coding: utf-8 -*-
"""
Created on May 23rd, 2017
LeetCode problem 507
We define the Perfect Number is a positive integer that is equal to the sum
of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a
perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
@author: K Li
"""

class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=3:
            return False
        selfSum = 0
        for n in range(1,int(num**0.5)+1):
            if (num%n) == 0:
                selfSum += n
                m = num//n
                if (m!=num)&(m!=n):
                    selfSum += m
        return selfSum == num
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [1,6,28,496,500,8128, 33550336, 8589869056]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        #print('Test case %d-----------'%i)
        flag = a.checkPerfectNumber(test)
        print(test, "is %s a perfect number"%("" if flag else "NOT"))
        

