# -*- coding: utf-8 -*-
"""
Created on Sun May 15, 2017
LeetCode problem 290
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains
lowercase letters separated by a single space.
@author: K Li
"""

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        n1 = len(pattern)
        wordList = s.split()
        n2 = len(wordList)
        if n1==0:
            return False
        if n1!=n2:
            return False
        mapping = {}
        for n, p in enumerate(pattern):
            if p not in mapping:
                mapping[p] = wordList[n]
            else:
                if mapping[p]!= wordList[n]:
                    return False
                else:
                    continue
        v = list(mapping.values())
        return len(v)==len(set(v))

    def wordPattern1(self, pattern, str):
        s = pattern
        t = str.split()
        if len(s)==0:
            return False
        if len(s) != len(t):
            return False
        if len(set(s)) != len(set(t)):
            return False
        return len(set(zip(s, t))) == len(set(s))

if __name__ == '__main__':
    a = Solution()
    testVector = [("", ""), (" ", " "),("a", ""),
                  ("abba","dog cat cat dog"),
                  ("abba","dog cat cat fish"),
                  ("abbac","dog cat cat dog alpha"),
                  ("abba","dog dog dog dog")]
    a = Solution()
    for test in testVector:
        print(test[0], test[1])
        flag = a.wordPattern(test[0],test[1])
        #print("Pattern %s is %s matched."%(test[0].upper(),'' if flag else 'NOT'))
        print(a.wordPattern(test[0], test[1]),a.wordPattern1(test[0],test[1]))
