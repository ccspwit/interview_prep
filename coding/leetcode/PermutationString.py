# -*- coding: utf-8 -*-
"""
Created on May 27, 2017
LeetCode problem 567
Given two strings s1 and s2, write a function to return true if s2 contains
the permutation of s1. In other words, one of the first string's permutations
is the substring of the second string.

Example 1:
Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False
Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
@author: K Li
"""

class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        N, M = len(s1), len(s2)
        if N==0:
            return True
        if (M==0) or (N>M):
            return False

        counter = {}
        for ch in s1:
            counter[ch] = counter.get(ch,0)+1

        nCount = 0
        left, right = 0, N-1
        for n in range(left, right+1):
            ch = s2[n]
            if ch in counter:
                counter[ch] = counter[ch] - 1
                if counter[ch]>=0:
                    nCount += 1
                else:
                    nCount -= 1
                if nCount == N:
                    #print(counter)
                    return True
        
        right = N
        while right < M:
            l = s2[left]
            r = s2[right]
            if l in counter:
                counter[l] = counter[l]+1
                if counter[l]>0:
                    nCount -= 1
                else:
                    nCount += 1
            if r in counter:
                counter[r] = counter[r]-1
                if counter[r]>=0:
                    nCount += 1
                else:
                    nCount -= 1
            if nCount ==N:
                #print(counter)
                return True
            left += 1
            right += 1
            
        return False

if __name__ == '__main__':
    a = Solution()
    testVector = [("","a"),("a",""),("abc","aaaccbac"),
                  ("sea","aet"),("aabcc","aabbacac"),
                  ("heart","earth")]
    a = Solution()
    print("Reverse words in string I")
    for test in testVector:
        #print(test)
        print("\'%s\' = \'%s\'"%(test, a.checkInclusion(test[0], test[1])))
        #print("\'%s\' = \'%s\'"%(test, a.reverseWordsI1(test)))
