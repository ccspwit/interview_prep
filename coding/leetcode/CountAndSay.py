# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 2017
LeetCode problem 38

The count-and-say sequence is the sequence of integers beginning as follows:
given a nonnegative number n, output sequence of string as follows
1, 11, 21, 1211, 111221, ...

0: "1"
1: "1"
2: "11", count number in the previous sequence
3: "21"
4, "1211"
Note: The sequence of integers will be represented as a string.

@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def countRegex(self, n):
        """
        :type n: int
        :rtype: str
        Amazing trick using regular expression
        """

        s = '1'
        for _ in range(n - 1):
            s = re.sub(r'(.)\1*', lambda m: str(len(m.group(0))) + m.group(1), s)
        return s

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        resStr = "1"
        if n<=1:
            return resStr
        for i in range(1,n):
            lastStr = resStr
            resStr = ""
            occurance = 0
            for ch in lastStr:
                if occurance==0:
                    lastChar = ch
                    occurance += 1
                elif ch==lastChar:
                    occurance += 1
                else:
                    resStr += str(occurance)+lastChar
                    lastChar = ch
                    occurance = 1
            #process last char
            resStr += str(occurance)+ch
            #print(i, resStr)
        
        return resStr
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [6]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        string = a.countAndSay(test)
        print(string)
        string = a.countRegex(test)
        print(string)
