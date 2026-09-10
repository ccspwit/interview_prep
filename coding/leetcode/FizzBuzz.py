# -*- coding: utf-8 -*-
"""
Created on May 17, 2017
LeetCode problem 412
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and
for the multiples of five output “Buzz”. For numbers which are multiples of
both three and five output “FizzBuzz”.

Example:
n = 15,
Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
@author: K Li
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n<=0:
            return []
        result = []
        for i in range(1,n+1):
            if (i%15)==0:
                result.append('FizzBuzz')
            elif (i%5)==0:
                result.append('Buzz')
            elif (i%3)==0:
                result.append('Fizz')
            else:
                result.append(str(i))
        return result

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [0,1,15,30]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test, a.fizzBuzz(test))
        

