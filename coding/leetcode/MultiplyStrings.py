# -*- coding: utf-8 -*-
"""
Created on May 30, 2017
LeetCode problem 43
Given two non-negative integers num1 and num2 represented as strings, return
the product of num1 and num2.

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to
integer directly.
@author: K Li
"""

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        Convert str to list[int] first, also keep intermediate result in
        reverse order. More efficient
        """
        def mulOne(num1, num2):
            """
            num1: list in reverse order
            num2: int
            rtype: list in reverse order
            """
            ans = []
            carry = 0
            n2 = num2
            for n1 in num1:
                mul2 = n1*n2 + carry
                digit = mul2%10
                carry = mul2//10
                ans += [digit]
            if carry:
                ans += [carry]
            return ans
            #end of function add2

        def add2(num1, num2):
            """
            :type num1: list in reverse order
            :type num2: list in reverse order
            :rtype: list in reverse order
            """
            N, M = len(num1), len(num2)
            # make sure len(num1)>=len(num2)
            if N<M:
                N, M = M, N
                num1, num2 = num2, num1
            result = []
            carry = 0
            for ind, n2 in enumerate(num2):
                add2 = n2 + num1[ind] + carry
                digit = add2%10
                carry = add2//10
                result += [digit]
            for ind in range(M,N):
                add2 = num1[ind] + carry
                digit = add2%10
                carry = add2//10
                result += [digit]
            if carry:
                result += [1]
            
            return result
            #end of function add2
        
        if not num1 or not num2:
            return "0"
        if (num1=="0") or (num2=="0"):
            return "0"

        #N1, N2 = len(num1), len(num2)
        # reverse order of input
        num1 = [int(n) for n in num1[::-1]]
        num2 = [int(n) for n in num2[::-1]]
        result = [0]
        temp = 0
        for n2 in num2:
            temp = mulOne(num1, n2)
            result = add2(temp, result)
            num1  = [0]+num1
        return "".join([str(_) for _ in result[::-1]])

    def multiply0(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        Keep intermediate result in str format. A bit too complicated
        """
        
        N1, N2 = len(num1), len(num2)
        if (N1==0) or (N2==0):
            return "0"
        if (num1=="0") or (num2=="0"):
            return "0"
        
        result = "0"
        carry = 0
        temp = ""
        for n2 in num2[::-1]:
            temp = self.multiply1(num1, n2)
            result = self.addition(temp, result)
            num1 += "0"
        return result

    def multiply1(self, num1, num2):
        """
        num1: string
        num2: string of length 1
        rtype: string
        """
        num1 = num1[::-1]
        ans = ""
        carry = 0
        n2 = int(num2)
        for n1 in num1:
            mul2 = int(n1)*n2 + carry
            digit = mul2%10
            carry = mul2//10
            ans += str(digit)
        if carry:
            ans += str(carry)
        return ans[::-1]
            
    def addition(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        N, M = len(num1), len(num2)
        # make sure len(num1)>=len(num2)
        if N<M:
            N, M = M, N
            num1, num2 = num2, num1
        result = ""
        carry = 0
        num1, num2 = num1[::-1], num2[::-1]
        for ind, n2 in enumerate(num2):
            add2 = int(n2) + int(num1[ind]) + carry
            digit = add2%10
            carry = add2//10
            result += str(digit)
        for ind in range(M,N):
            add2 = int(num1[ind]) + carry
            digit = add2%10
            carry = add2//10
            result += str(digit)
        if carry:
            result += "1"
        
        return result[::-1]
            
if __name__ == '__main__':
    a = Solution()
    testVector = [("0","0"),("2","3"),("123","3"),
                  ("1234567890","987654321")]
    a = Solution()
    print("Multiply strings...")
    for test in testVector:
        print(test)
        print(a.multiply(test[0],test[1]))
        print(a.multiply0(test[0],test[1]))
