# -*- coding: utf-8 -*-
"""
Created on May 27, 2017
LeetCode problem 592
Given a string representing an expression of fraction addition and
subtraction, you need to return the calculation result in string format.
The final result should be irreducible fraction. If your final result is an
integer, say 2, you need to change it to the format of fraction that has
denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:
Input:"-1/2+1/2"
Output: "0/1"
Example 2:
Input:"-1/2+1/2+1/3"
Output: "1/3"
Example 3:
Input:"1/3-1/2"
Output: "-1/6"
Example 4:
Input:"5/3+1/3"
Output: "2/1"
@author: K Li
"""

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        Use functools.reduce
        """
        from functools import reduce
        if len(expression)==0:
            return "0/1"
        fracNumbers = self.parse(expression)
        return "{}/{}".format(*reduce(self.fracAdd, fracNumbers))

    def fractionAddition1(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        fracNumbers = self.parse(expression)
        
        result = [0, 1]
        for fNum in fracNumbers:
            result = self.fracAdd(result, fNum)
            #print("result=", result)
        return "{}/{}".format(*result)
    
    def parse(self, s):
        """
        Parse input string into fraction numbers, and '+','-' sign
        Iterator implement 
        """
        N = len(s)
        left = 0
        for n, ch in enumerate(s):
            if n<N-1:
                if ch.isdigit() and not s[n+1].isdigit() and s[n+1]!='/':
                    yield list(map(int,s[left:n+1].split('/')))
                    left = n+1
            if n==N-1:
                yield list(map(int,s[left:n+1].split('/')))
        return
    
    def parse1(self, s):
        """
        Parse input string into fraction numbers, and '+','-' sign
        """
        N = len(s)
        numbers = []
        left = 0
        for n, ch in enumerate(s):
            if n<N-1:
                if ch.isdigit() and not s[n+1].isdigit() and s[n+1]!='/':
                    numbers.append(list(map(int,s[left:n+1].split('/'))))
                    left = n+1
            if n==N-1:
                numbers.append(list(map(int,s[left:n+1].split('/'))))
        return numbers
    def fracAdd(self, n, m):
        """
        Add/Substract two fraction numbers
        Return a fraction tuple
        """
        num = (n[0]*m[1]+m[0]*n[1])
        den = n[1] * m[1]
        a, b = num, den
        # compute GCD of numerator and denominator
        if a==0:
            GCD = b
        else:
            while b:
                a, b = b, a%b
            GCD = a
        return (num//GCD, den//GCD)
        
if __name__ == '__main__':
    a = Solution()
    testVector = ["","-1/2+1/2",
                  "1/3-1/2","5/3+1/3",
                  "-1/2+1/2+1/3"]
    a = Solution()
    print("Fraction number addition/substraction")
    for test in testVector:
        #print(test)
        print("\'%s\' = \'%s\'"%(test, a.fractionAddition(test)))
        #print("\'%s\' = \'%s\'"%(test, a.reverseWordsI1(test)))
