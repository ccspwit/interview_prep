# -*- coding: utf-8 -*-
"""
Created on May 24, 2017
LeetCode problem 521, 522 combined
---#521
Given a group of two strings, you need to find the longest uncommon
subsequence of this group of two strings. The longest uncommon subsequence
is defined as the longest subsequence of one of these strings and this
subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting
some characters without changing the order of the remaining elements.
Trivially, any string is a subsequence of itself and an empty string is a
subsequence of any string.

The input will be two strings, and the output needs to be the length of the
longest uncommon subsequence. If the longest uncommon subsequence doesn't
exist, return -1.

Example 1:
Input: "aba", "cdc"
Output: 3
Explanation: The longest uncommon subsequence is "aba" (or "cdc"), 
because "aba" is a subsequence of "aba", 
but not a subsequence of any other strings in the group of two strings. 
Note:

Both strings' lengths will not exceed 100.
Only letters from a ~ z will appear in input strings.

---#522
Given a list of strings, you need to find the longest uncommon subsequence
among them. The longest uncommon subsequence is defined as the longest
subsequence of one of these strings and this subsequence should not be any
subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting
some characters without changing the order of the remaining elements.
Trivially, any string is a subsequence of itself and an empty string is a
subsequence of any string.

The input will be a list of strings, and the output needs to be the length
of the longest uncommon subsequence. If the longest uncommon subsequence
doesn't exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3
Note:

All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
@author: K Li
"""

class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        
        """
        def subseq(w1, w2):
            """
            Check if w1 is subsequence of w2
            """
            i, N = 0, len(w1)
            for c in w2:
                if (i<N) and (w1[i]==c):
                    i += 1
            return i==N
            
        N = len(strs)
        if N==0:
            return -1
        descent = sorted(strs, key=len, reverse=True)
        length = [len(s) for s in descent]
        
        for i, w1 in enumerate(descent):
            isSubseq = [not subseq(w1,w2)
            for j, w2 in enumerate(descent) if (i!=j)]
            if all(isSubseq):
                return len(w1)
                    
        return -1

    def findLUSlength1(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        Assume duplicate string of same length will be contiguous.
        Not working for case like ["a","b","a""b"]
        """
        def subseq(w1, w2):
            """
            Check if w1 is subsequence of w2
            """
            i, N = 0, len(w1)
            for c in w2:
                if (i<N) and (w1[i]==c):
                    i += 1
            return i==N
            
        N = len(strs)
        if N==0:
            return -1
        sortedStrs = sorted(strs, key=len, reverse=True)
        length = [len(s) for s in sortedStrs]
        
        duplicate = 0
        curLen = length[0]
        curWord = sortedStrs[0]
        for n in range(1,N):
            if length[n]!=curLen:
                if duplicate:
                    if subseq(sortedStrs[n], curWord):
                        curLen = -1
                        curWord = sortedStrs[n]
                        duplicate = 1
                    else:
                        curLen = length[n]
                        curWord = sortedStrs[n]
                        duplicate = 0
                else:
                    return curLen
            else:
                if sortedStrs[n]!=curWord:
                    return curLen
                else:
                    duplicate = 1
                    
        return -1 if duplicate else curLen
    
    def findLUSlengthI(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        What a stupid problem it is.
        """
        if a==b:
            return -1
        else:
            return max(len(a),len(b))

    def findLUSlengthI1(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        What a stupid problem it is.
        """
        N, M = len(a), len(b)
        if N==M:
            return -1 if a==b else N
        else:
            return max(N,M)

if __name__ == '__main__':
    a = Solution()
    testVector = [("", ""), ("a","a"),("a", "b"),
                  ("abc", "abc"),
                  ("abcabcabc", "abc"),
                  ("babacd", "abc"),
                  ("cbaebabacd", "abc"),
                  ("ana gram", "nagaram")]
    for test in testVector:
        print(test[0], test[1])
        print(a.findLUSlengthI(test[0],test[1]))
        print(a.findLUSlengthI1(test[0],test[1]))

    testVector = [[],["","",""],["a"],
                  ["a","b","a","b"],
                  ["aaa","aaa","aa"],
                  ["aaa","aaa","ab"],
                  ["aaa","aaa","ab","ab","a"],
                  ["aabbcc", "aabbcc","abc"],
                  ["aba","cdc","eae"]]
    for test in testVector:
        print(test)
        print(a.findLUSlength(test))
        #print(a.findLUSlengthI1(test[0],test[1]))
