# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 2017
LeetCode problem 28
Returns the index of the first occurrence of needle in haystack
or -1 if needle is not part of haystack.

@author: K Li
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        matchIndex = -1
        N, M = len(haystack), len(needle)
        for n in range(N-(M-1)):
            match = 0
            for m in range(M):
                if(haystack[n+m] == needle[m]):
                    match += 1
                else:
                    break
            if match == M:
                matchIndex = n
                break
        return matchIndex

if __name__ == '__main__':
    a = Solution()
    testVector = [("abc", "abc"),
                  ("this is a test string", "str"),
                  ("this is a test string", "strings"),
                  ("this is a test string", "thisis"),
                  ("str", "string"), ("", "")]
    a = Solution()
    for test in testVector:
        print("haystack -- %s"%test[0])
        print("needle -- %s"%test[1])
        n = a.strStr(test[0],test[1])
        print("\tFirst match index is %d"%n)

