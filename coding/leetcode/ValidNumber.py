# -*- coding: utf-8 -*-
"""
Created on May 10, 2017
LeetCode problem 65
Return True if the input string is a number and false otherwise
@author: K Li
"""

class Solution(object):
    def isNumber(self, s):
        """
        :type s: string
        :rtype: bool
        Use DFA or FSM to process state transition
        Check the number is a valid number, integer or float
        Use the following regex as a guide for code
        pattern1 = r"\s*[+-]?\d*[\.]?\d+([eE]\d+)?\s*"
        pattern2 = r"\s*[+-]?\d+[\.]?\d*([eE]\d+)?\s*"
        """
        # remove all preceding and trailing white spaces
        s = s.strip()
        N = len(s)
        if N==0:
            return False
        digitFound = False
        eFound = False
        
        ind = 0
        
        # if there is +/-, skip
        if (s[ind] == '+') | (s[ind]=='-'):
            ind += 1
        
        if ind==N:  # check if reach end of the string
            return False

        # check for digits
        while ind<N and s[ind].isnumeric():
            ind += 1
            # have to see at least 1 digit
            digitFound = True

        if ind==N:  # check if reach end of the string
            return digitFound

        # check for '.' character
        if ind < N and s[ind] == '.':
            ind += 1
            while ind < N and s[ind].isnumeric():
                digitFound = True
                ind += 1
        if ind==N:  # check if reach end of the string
            return digitFound
        
        #check for 'e'/'E' character
        if ind <N and s[ind].lower() == 'e':
            ind += 1
            eFound = True
            if digitFound is False:
                return False
        
        #check for +/- sign after e/E
        if eFound and ind<N and ((s[ind]=='+') or (s[ind]=='-')):
            ind += 1
        if ind == N:    # check if reach end of the string
            return False
        #check for digit after e and/or sign
        while ind<N and s[ind].isnumeric():
            ind += 1
        
        if ind==N:  # check if reach end of the string
            return True
        else:
            return False
        
    def isNumber1(self, s):
        """
        :type root: TreeNode
        :rtype: bool
        Employ FSM or DFA
        """
        #define a DFA
        state = [{},
                 {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
                 {'digit':3, '.':4},
                 {'digit':3, '.':5, 'e':6, 'blank':9},
                 {'digit':5},
                 {'digit':5, 'e':6, 'blank':9},
                 {'sign':7, 'digit':8},
                 {'digit':8},
                 {'digit':8, 'blank':9},
                 {'blank':9}]
        currentState = 1
        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'
            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]
        if currentState not in [3,5,8,9]:
            return False
        return True
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = ["   ", " +12", " -12345 ", " 12a",
                  "-.12", "+0.00"," -123.","-1.23.3",
                  "-.1E11","1.23e","1.234E+e"]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        status = 'IS' if a.isNumber1(test) else 'IS NOT'
        print('\"%s\" %s an number'%(test, status))
