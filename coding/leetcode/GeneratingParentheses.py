# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 22
Given n pairs of parentheses, write a function to generate all combinations
of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
@author: K Li
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        ")" can only be placed at 1 or more "(". So we could first find out
        all possible positions of ")", adjust position of "(" accordingly.
        Then we find all possible parentheses.
        """
        if n<=0:
            return [""]

        result=["("*n]
        pos = [1]
        for i in range(n):
            # place one ")" at a time
            temp = []
            tempPos=[]
            for comb, start in zip(result,pos):
                #start = i*2+1
                end = n+i+1
                for j in range(start,end):
                    temp.append(comb[:j]+")"+comb[j:])
                    tempPos.append(max(j+1,2*i+3))
            result = temp
            pos = tempPos
        
        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = [3]
    for test in testVector:
        print(test)
        print("Possible combination of parentheses are ", a.generateParenthesis(test))

