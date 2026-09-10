# -*- coding: utf-8 -*-
"""
Created on Sun May 21, 2017
LeetCode problem 500
Given a List of words, return the words that can be typed using letters of
alphabet on only one row's of American keyboard like the image below.


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.

@author: K Li
"""

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        Row1 = set("qwertyuiop")
        Row2 = set("asdfghjkl")
        Row3 = set("zxcvbnm")
        result = []
        if len(words)==0:
            return result
        for word in words:
            if word != "":
                curSet = set(word.lower())
                if (curSet<=Row1) | (curSet<=Row2) | (curSet<=Row3):
                    result.append(word)
        return result

if __name__ == '__main__':
    a = Solution()
    testVector = [["", "Hello", "Alaska", "Dad", "Peace","toquit","thank"]]
    a = Solution()
    for ind, test in enumerate(testVector):
        print('Test case #',ind+1)
        print(test)
        print(a.findWords(test))
        

