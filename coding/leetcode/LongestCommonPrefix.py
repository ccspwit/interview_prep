# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 2017
LeetCode problem 14
Write a function to find the longest common prefix string amongst an array of strings.

@author: K Li
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        N = len(strs)
        if N<=0:
            return ""
        if N==1:
            return strs[0]
        strs.sort()
        LCP = strs[0]
        for i in range(1,N):
            j = 0
            si = strs[i]
            while (j< min(len(LCP),len(si))):
                if LCP[j] == si[j]:
                    j += 1
                else:
                    break
            if(j==0):
                return ""
            else:
                LCP = LCP[:j]
            
        return LCP

    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        N = len(strs)
        if N<=0:
            return ''
        if N==1:
            return strs[0]
        LCP = strs[0]
        for i in range(1,N):
            j = 0
            while (j< min(len(LCP),len(strs[i]))):
                if LCP[j] == strs[i][j]:
                    j += 1
                else:
                    break
            LCP = LCP[:j]
            
        return LCP

if __name__ == '__main__':
    a = Solution()
    testVector = [["this is voa","this is not voa", "the voice of america"],
                  ["why not","why not to study", "why no to study coding"],
                  ["abc","def","ghi","zzz"],
                  ["a","abcde","acc","ass"],
                  ["abcd"],[""],[]]
    for test in testVector:
        print('Input is {}\n. Longest common prefix is {}'.format(
                test, a.longestCommonPrefix(test)))

data1 = ["why not to do this",
        "why not to study",
        "why not to study coding",
        "why not to studing coding in leetcode",
        "why not to studing coding in leetcode?"]
data2 = ["why not to studing coding in leetcode?",
        "why not to studing coding in leetcode",
        "why not to study coding",
        "why not to study",
        "why not to do this"]