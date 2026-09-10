# -*- coding: utf-8 -*-
"""
Created on Sun May 7, 2017
LeetCode problem 205
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character
while preserving the order of characters. No two characters may map to the
same character but a character may map to itself.

For example,
Given "egg", "add", return true.
Given "foo", "bar", return false.
Given "paper", "title", return true.

@author: K Li
"""

class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Use one dictionary, use zip
        """
        N, M = len(s), len(t)
        if N != M:
            return False
        if N==0:
            return True
        iso_map = {}
        
        for si, ti in zip(s,t):
            if (si in iso_map):
                # match s[n-k]:t[n-k] to t[n]
                if ti != iso_map[si]:
                    return False
            else:
                # si is new element, ti could be new or old
                # new is True, old (meaning duplicate) is False
                iso_map[si] = ti

        return len(set(iso_map.values())) == len(iso_map.values())
    
    def isIsomorphic1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Use two dictionary
        """
        N, M = len(s), len(t)
        if N != M:
            return False
        if N==0:
            return True
        dictST = {s[0]:t[0]}
        dictTS = {t[0]:s[0]}
        
        for n in range(N):
            if (s[n] in dictST):
                # match s[n-k]:t[n-k] to t[n]
                if t[n] != dictST[s[n]]:
                    return False
                else:
                    continue
            elif t[n] not in dictTS:
                # both are new element, add to dictionary
                dictST[s[n]] = t[n]
                dictTS[t[n]] = s[n]
            else:
                # s[n] new, but t[n] old, False
                return False
        return True

if __name__ == '__main__':
    a = Solution()
    testVector = [("egg", "add"),
                  ("foo", "bar"),
                  ("paper", "title"),
                  ("abab", "aabb"),
                  ("abbac", "addab"), ("", "")]
    a = Solution()
    for test in testVector:
        print(test[0], test[1])
        flag = a.isIsomorphic(test[0],test[1])
        print("\tIs %s isomorphic."%('' if flag else 'NOT'))

