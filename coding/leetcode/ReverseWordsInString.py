# -*- coding: utf-8 -*-
"""
Created on May 25, 2017
LeetCode problem 151, 186, 557 combined
-- #151
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

-- #557
Given a string, you need to reverse the order of characters in each word
within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will
not be any extra space in the string.

-- # 186, Feb 23, 2020
Given an input string , reverse the string word by word. 

Example:
Input:  ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
Output: ["b","l","u","e"," ","i","s"," ","s","k","y"," ","t","h","e"]

Note:
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
@author: K Li
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join([w[::-1] for w in s.split()])

    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return ""
        words = s.split()

        N = len(words)
        r = ""
        if N==0:
            return ""
        for w in words[:-1]:
            r += w[::-1]+" "
        r += words[-1][::-1]
        return r
    
    def reverseWordsI(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)==0:
            return s
        wList = s.split()
        N = len(wList)
        if N==0:
            return ""
        r = ""
        for n in range(N-1,0,-1):
            r += wList[n]+" "
        r += wList[0]
        return r

    def reverseWordsI1(self, s):
        """
        :type s: str
        :rtype: str
        """
        return " ".join(s.split()[::-1])
    def reverseWordsII(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # first reverse the whole list
        N = len(s)
        mid = N // 2
        for n in range(mid):
            s[n], s[-1-n] = s[-1-n], s[n]

        # then reverse each word
        left = 0
        # use index(' ', n) to get index of ' ' after n
        while True:
            try:
                ind = s.index(' ', left)
                # flip word
                right = ind - 1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                left = ind + 1
            except ValueError:
                break

        if left < N-1:
            right = N-1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
                
    def reverseWordsII1(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # first reverse the whole list
        N = len(s)
        mid = N // 2
        for n in range(mid):
            s[n], s[-1-n] = s[-1-n], s[n]
        # then reverse each word
        left = 0
        for n in range(N):
            if s[n] == ' ':
                # flip word
                right = n-1
                while left < right:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                    right -= 1
                left = n + 1
        if left < N-1:
            right = N-1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1

if __name__ == '__main__':
    a = Solution()
    testVector = [""," ", "a", " a ", " the sky is blue",
                  "Let's take LeetCode contest"]
    a = Solution()
    print("Reverse words in string I")
    for test in testVector:
        #print(test)
        print("\'%s\' -- \'%s\'"%(test, a.reverseWordsI(test)))
        print("\'%s\' -- \'%s\'"%(test, a.reverseWordsI1(test)))

    print("Reverse words in string III")

    for test in testVector:
        #print(test)
        print("\'%s\' -- \'%s\'"%(test, a.reverseWords(test)))
        print("\'%s\' -- \'%s\'"%(test, a.reverseWords1(test)))
