# -*- coding: utf-8 -*-
"""
Created on June 3rd, 2017
LeetCode problem 408
Given a non-empty string s and an abbreviation abbr, return whether the
string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
"w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the
string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase
letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.
Example 2:
Given s = "apple", abbr = "a2e":

Return false.
@author: K Li
"""

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        N, M = len(word), len(abbr)
        if M>N:
            return False
        posW, p1 = 0, 0     #position pointer for word
        while p1<M:
            ch = abbr[p1]
            if ch.isalpha():
                if ch==word[posW]:
                    posW += 1
                    p1 += 1
                else:
                    return False
            elif ch.isdigit() and ch!="0":
                p2 = p1+1
                while (p2 < M) and (abbr[p2].isdigit()):
                    p2 += 1
                num = int(abbr[p1:p2])
                posW += num
                p1 = p2
                if posW>=N:
                    break
            else:
                # not alphanumeric characters
                return False
        return (posW==N) and (p1==M)
        """if (posW==N) and (p1==M):
            return True
        else:
            return False"""

if __name__ == '__main__':
    a = Solution()
    testVector = [("",""),("hi","2i"),("hi","02")
                  ("word","w1rd"),("word","2r1"),
                  ("xxx","3"),("xxx","2"),("xxx","1x"),
                  ("internationalization","i12iz4n"),
                  ("internationalization","i5a11o1"),
                  ("apple","a2e"), ("justifi","justifi")]
    a = Solution()
    print("Palindrome permutation")
    for test in testVector:
        print(test)
        print("Valid abbrevation? ", a.validWordAbbreviation(test[0],test[1]))
