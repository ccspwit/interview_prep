# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 2017
LeetCode problem 20
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid
but "(]" and "([)]" are not.

@author: K Li
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        Use stack to match opening and closing parenthesis
        Return when deteced mismatch
        """
        
        valid = True
        matchDict = {")":"(","]":"[","}":"{"}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            if char in ")]}":
                if stack:   # not empty
                    last = stack.pop()
                    if last != matchDict[char]:
                        # poped opening parenthesis does matched the closing one
                        return False
                else:       # nothing to pop, unmatch closing parenthesis
                    return False
        if stack: # there are unmatched opening parenthesis left
            return False
        return valid

    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        Use stack to match opening and closing parenthesis
        """
        
        valid = True
        matchDict = {")":"(","]":"[","}":"{"}
        stack = []
        for char in s:
            if char in "([{":
                stack.append(char)
            if char in ")]}":
                if stack:   # not empty
                    last = stack.pop()
                    if last != matchDict[char]:
                        # poped opening parenthesis does matched the closing one
                        valid = False
                else:       # nothing to pop, unmatch closing parenthesis
                    valid = False
        if stack: # there are unmatched opening parenthesis left
            valid = False
        return valid

if __name__ == '__main__':
    a = Solution()
    testVector = ["()","{}","[]","[",
                  "abd(def(g[]))",
                  "abcd","(()([({)}]))"]
    for test in testVector:
        print('{} parenthesis validity is {}'.format(test, a.isValid(test)))

