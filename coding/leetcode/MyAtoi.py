# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 2017
LeetCode problem 8
mplement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge,
please do not see below and ask yourself what are the possible input cases.
Notes: It is intended for this problem to be specified vaguely (ie, no given
input specs). You are responsible to gather all the input requirements up front.
@author: K Li
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """
        
        if not isinstance(s, str):
            raise TypeError('Input must be of string type')
        N = len(s)
        if N<=0:
            return 0
            #raise ValueError('Input can not be empty string')
        ind = 0
        intVal = 0
        negative = False
        # process any leading whitespace, +/- sign
        whiteSet = set((' ', '\t', '\n', '\r'))
        
        while (ind<N):
            if s[ind] in whiteSet:
                ind += 1
            else:
                break
        if s[ind] == '-':
            negative = True
            ind += 1
        elif s[ind] == '+':
            ind += 1
        
        # process digits
        numDict = {val: ind for ind, val in enumerate('0123456789')}
        while (ind<N):
            if (s[ind] in numDict):
                intVal *= 10
                intVal += numDict[s[ind]]
                ind += 1
            else:
                break
        
        #skip any trailing white space characters, othersise raise error
        while (ind<N):
            if (s[ind] in whiteSet):
                ind += 1
            else:
                break
        if ind<N:
            raise ValueError('input string %s contain invalid characters' %s)

        print(intVal)
        if negative:
            intVal *= -1
            intVal = max(intVal, -2**31)
        else:
            intVal = min(intVal, 2**31-1)

        return intVal
        
if __name__ == '__main__':
    a = Solution()
    testVector = [('123', 123), ('-123',-123), (' 0123', 123), (' -123', 123),
                  ('100', None), ('+12',-12), ('',0),
                  ('0',0), ('-0  ',0),('101',0), ('-0  ',0),
                  ('2147483648', 2147483647), ('-2147483649', -2147483648)]
    for test in testVector:
        print('String=\'%s\', Integer=%d' %(test[0], a.myAtoi(test[0])))
    
