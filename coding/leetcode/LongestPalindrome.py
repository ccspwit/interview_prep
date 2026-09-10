# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 2017
LeetCode problem 5
Given a string s, find the longest palindromic substring in s.
You may assume that the maximum length of s is 1000.

Examples:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"
@author: K Li
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        Iterate potential mid-point from 0, N, check for palindrome pattern
        from neighboring points, stop immediately when does not match.
        Appears to be more efficient.
        Optimize further
        """
        
        N = len(s)
        if N<=1:
            return s
        
        retVal = s[0]
        maxLen = 1
        maxLeft = 0
        
        for midPoint in range(1,N):
            if(N-midPoint)<((maxLen+1)//2):
                break;
            #odd case 'aba'
            left = midPoint-1
            right = midPoint+1
            curLen = 1
            while (left>=0) and (right<N) and s[left]==s[right]:
                curLen += 2
                left -= 1
                right += 1
            if(curLen>maxLen):
                maxLen = curLen
                maxLeft = left+1

            #even case 'abba'
            left = midPoint-1
            right = midPoint
            curLen = 0
            while (left>=0) and (right<N) and s[left]==s[right]:
                curLen += 2
                left -= 1
                right += 1
            if(curLen>maxLen):
                maxLen = curLen
                maxLeft = left+1
        
        retVal = s[maxLeft:(maxLeft+maxLen)]
        return retVal

    def longestPalindrome2(self, s):
        """
        :type s: str
        :rtype: str
        Iterate potential mid-point from 0, N, check for palindrome pattern
        from neighboring points, stop immediately when does not match.
        Appears to be more efficient.
        """
        
        N = len(s)
        if N<=1:
            return s
        
        retVal = s[0]
        maxLen = 1
        maxLeft = 0
        
        for midPoint in range(1,N):
            #odd case 'aba'
            left = midPoint-1
            right = midPoint+1
            curLen = 1
            while (left>=0) and (right<N) and s[left]==s[right]:
                curLen += 2
                left -= 1
                right += 1
            if(curLen>maxLen):
                maxLen = curLen
                maxLeft = left+1

            #even case 'abba'
            left = midPoint-1
            right = midPoint
            curLen = 0
            while (left>=0) and (right<N) and s[left]==s[right]:
                curLen += 2
                left -= 1
                right += 1
            if(curLen>maxLen):
                maxLen = curLen
                maxLeft = left+1
        
        retVal = s[maxLeft:(maxLeft+maxLen)]
        return retVal

    def longestPalindrome1(self, s):
        """
        :type s: str
        :rtype: str
        Use string operation: slicing and reverse slicing, compare for equality
        May be time consuming
        """
        
        N = len(s)
        if N<=1:
            return s
        sRev = s[::-1]
        
        retVal = s[0]
        curPos = 0
        curLen = 1
        maxLen = 1
        
        while (curPos+curLen)<N:
            curLen = (N-curPos)
            while(curLen>maxLen):
                s1 = s[curPos:(curPos+curLen)]
                s2 = sRev[(N-curPos-curLen):N-curPos]
                #print(curPos, curLen)
                #print(s1)
                #print(s2)
                if(s1 == s2):
                    maxLen = curLen
                    retVal = s1
                    #print('current maxLen is ',maxLen)
                    break
                curLen -= 1
            curPos += 1
        
        return retVal

if __name__ == "__main__":
    a = Solution()
    testVector = ['','a','bb','babad','radarisraddar',
                  'radarisraddarabcdcba']
    for test in testVector:
        print(test)
        print('Longest Palindrome string is ',a.longestPalindrome(test))
