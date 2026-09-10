# -*- coding: utf-8 -*-
"""
Created on Sun May 17, 2017
LeetCode problem 383
Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
@author: K Li
"""

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        set & count
        """
        for ch in set(ransomNote):
            if ransomNote.count(ch) > magazine.count(ch):
                return False
        return True

    def canConstruct1(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        Dictionary & counter
        """
        chCounter = {}
        # Count occurance of all characters in the magazine
        for ch in magazine:
            chCounter[ch] = chCounter.get(ch, 0)+1
        #
        for ch in ransomNote:
            if ch in chCounter:
                chCounter[ch] = chCounter[ch]-1
                if chCounter[ch]<0:
                    return False
            else:
                return False
        return True

    def canConstruct2(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        Dictionary & counter
        """
        chCounter = {}
        # Count occurance of all characters in the magazine
        for ch in magazine:
            chCounter[ch] = chCounter.get(ch, 0)+1
        #
        for ch in ransomNote:
            chCounter[ch] = chCounter.get(ch, 0)-1
            if chCounter[ch]<0:
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    testVector = [("", ""), (" ", " "),("a", ""),("a", "b"),
                  ("aa", "ab"),("aa", "aab"),
                  ("godttf","dog cat cat fish"),
                  ("godtttf","dog cat cat fish"),
                  ("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj")]
    a = Solution()
    for test in testVector:
        print(test[0], test[1])
        flag = a.canConstruct(test[0],test[1])
        print("Can %s construct ransom note."%('' if flag else 'NOT'))
        flag = a.canConstruct1(test[0],test[1])
        print("Can %s construct ransom note."%('' if flag else 'NOT'))
