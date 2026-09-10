# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 17
Given a digit string, return all possible letter combinations that the number
could represent.

A mapping of digit to letters (just like on the telephone buttons) is given
below.
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:
Although the above answer is in lexicographical order, your answer could be
in any order you want.
@author: K Li
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        _keyMap = {'0':" ",
                  '1':"*",
                  '2':"abc",
                  '3':"def",
                  '4':"ghi",
                  '5':"jkl",
                  '6':"mno",
                  '7':"pqrs",
                  '8':"tuv",
                  '9':"wxyz"}
        N = len(digits)
        if N==0:
            return []
        
        result = [""]
        for d in digits:
            _keys = _keyMap[d]
            temp = []
            for comb in result:
                for ch in _keys:
                    temp.append(comb+ch)
            result = temp    
        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = ["","2","22","23"]
    for test in testVector:
        print(test)
        print("Letter combination is ", a.letterCombinations(test))

