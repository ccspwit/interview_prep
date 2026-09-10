# -*- coding: utf-8 -*-
"""
Created on June 4, 2017
LeetCode problem 150
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another
expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
Show Company Tags
Show Tags
Show Similar Problems
@author: K Li
"""

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        result = 0
        for t in tokens:
            if t.lstrip("-+").isdigit():
                stack.append(int(t))
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                if t == "+":
                    res = o1+o2
                if t == "-":
                    res = o1-o2
                if t == "*":
                    res = o1*o2
                if t == "/":
                    res = int(float(o1)/o2)
                
                stack.append(res)
   
        return int(stack[-1])

    def evalRPN1(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        Use eval, code is very clean, but there is one case may be incorrect
        for 2.x version. int(eval("-1/10")) give -1, while result is 0
        in 3.x version
        """
        stack = []
        result = 0
        for t in tokens:
            if t.lstrip("-+").isdigit():
                stack.append(t)
            else:
                o2 = stack.pop()
                o1 = stack.pop()
                res = int(eval(o1+t+o2))
                stack.append(str(res))
            #print(stack)
        # after for loop
        #print(stack)
        return int(stack[-1])

if __name__ == '__main__':
    a = Solution()
    testVector = [["18"],["3","-4","+"],
                  ["1","2","*","3"],
                  ["1","2","*","3","+"],
                  ["2", "1", "+", "3", "*"],    #9
                  ["4", "13", "5", "/", "+"],
                  ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]]
    a = Solution()
    for test in testVector:
        print(test)
        print("Can jump to the last element",(a.evalRPN(test)))
    
    #test = np.random.randint(0,20,20)