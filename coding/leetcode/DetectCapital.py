# -*- coding: utf-8 -*-
"""
Created on Sun May 23, 2017
LeetCode problem 520
Given a word, you need to judge whether the usage of capitals in it is right
or not. We define the usage of capitals in a word to be right when one of the
following cases holds:

1. All letters in this word are capitals, like "USA".
2. All letters in this word are not capitals, like "leetcode".
3.Only the first letter in this word is capital if it has more than one
letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.

Example 1:
Input: "USA"
Output: True
Example 2:
Input: "FlaG"
Output: False
Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.

@author: K Li
"""

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.islower() | word.isupper() | word.istitle()

    def detectCapitalUse2(self, word):
        """
        :type word: str
        :rtype: bool
        """
        N = len(word)
        if N>0:
            nCapital, firstCapital = 0,0
            for n in range(N):
                if word[n].isupper():
                    if (n==0):
                        firstCapital = 1
                    nCapital += 1
            cond1 = (nCapital==N)
            cond2 = (nCapital==0)
            cond3 = (nCapital==1)&(firstCapital==1)
            return cond1|cond2|cond3
        else:
            raise ValueError("Input can not be empty string")

    def detectCapitalUse1(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if word:
            cond1 = word.upper()==word
            cond2 = word.lower()==word
            cond3 = word.capitalize()==word
            return cond1|cond2|cond3
        else:
            raise ValueError("Input can not be empty string")

if __name__ == '__main__':
    a = Solution()
    testVector = ["USA", "Alaska", "Dad", "Peace","toQuit","thanK"]
    a = Solution()
    for ind, test in enumerate(testVector):
        print('Test case #',ind+1)
        print(test)
        print(test,"is valid capital?",a.detectCapitalUse(test))
        print(test,"is valid capital?",a.detectCapitalUse1(test))
        

