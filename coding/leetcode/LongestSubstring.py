# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 2017
LeetCode problem 3
Given a string, find the length of the longest substring without repeating characters.

Examples:
Given "abcabcbb", the answer is "abc", which the length is 3.
Given "bbbbb", the answer is "b", with the length of 1.
Given "pwwkew", the answer is "wke", with the length of 3.

@author: K Li
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        Implement using dictionary
        """

        # scan string from left to right
        start, end = 0, 1
        N = len(s)
        if N==0:
            return 0
        
        # initialize variables
        alphabet = {}
        alphabet[s[0]]=0
        curlen, maxlen = 1, 1
        
        for end in range(1,N):
            matchIndex = alphabet.get(s[end],-1)
            if(matchIndex >= start):
                # repeated character found after startindex

                # update maxlen/maxstr if needed
                if(curlen>maxlen):
                    maxlen = curlen
                
                # reset start index and current string len
                start = matchIndex+1
                curlen = end-start+1
            else:
                # if no repeated character found
                # increase length of substr
                curlen += 1

            alphabet[s[end]]=end
                
        if(curlen>maxlen):
            maxlen = curlen
        
        return maxlen

    def lengthOfLongestSubstring2(self, s):
        """
        :type s: str
        :rtype: int
        Implement using dictionary
        """

        # scan string from left to right
        start = 0
        end = start+1
        N = len(s)
        if N==0:
            return 0
        
        # initialize variables
        alphabet = {}
        alphabet[s[0]]=0
        curlen = 1
        maxlen = 1
        
        for end in range(1,N):
            matchIndex = alphabet.get(s[end])
            if(matchIndex is not None):
                # repeated character found

                # update maxlen/maxstr if needed
                if(curlen>maxlen):
                    maxlen = curlen
                
                # remove substring before the match index from alphabet
                #print(start,matchIndex,end)
                substr = s[start:matchIndex]
                #print(alphabet)
                #print(substr)
                for key in substr:
                    alphabet.pop(key)
                #[alphabet.pop(key) for key in substr]
                alphabet[s[end]]=end
                
                # reset substr index to after the first occurance of repetition
                start = matchIndex+1
                curlen = end-start+1
            else:
                # if no repeated character found
                # update character set, end index, length of substr
                alphabet[s[end]] = end
                curlen += 1
                
        if(curlen>maxlen):
            maxlen = curlen
        
        return maxlen

    def lengthOfLongestSubstring1(self, s):
        """
        :type s: str
        :rtype: int
        Implement using set
        """

        # scan string from left to right
        start = 0
        end = start+1
        N = len(s)
        if N==0:
            return 0
        
        # initialize variables
        alphabet = {s[0]}
        curlen = 1
        maxlen = 1
        maxstr = s[0]
        
        for end in range(1,N):
            if(s[end] in alphabet):
                # repeated character found

                # update maxlen/maxstr if needed
                if(curlen>maxlen):
                    maxlen = curlen

                # reset substr index to after the first occurance of repetition
                start = s.find(s[end], start, end)+1
                
                newsubstr = s[start:end+1]
                curlen = end-start+1
                #curlen = len(newsubstr)
                alphabet = set(newsubstr)   # reset alphabet set with newsubstr
            else:
                # if no repeated character found
                # update character set, end index, length of substr
                alphabet.add(s[end])
                curlen += 1
                
        if(curlen>maxlen):
            maxlen = curlen
        
        return maxlen

    def lengthOfLongestSubstring0(self, s):
        """
        :type s: str
        :rtype: int
        """

        # scan string from left to right
        start = 0
        end = start+1
        N = len(s)
        if N==0:
            return 0
        
        # initialize variables
        alphabet = {s[0]}
        curlen = 1
        maxlen = 1
        maxstr = s[0]
        
        while(end<N):
            if(s[end] in alphabet):
                # repeated character found
                # record substr with no repeated character
                curstr = s[start:end]

                # update maxlen/maxstr if needed
                if(curlen>maxlen):
                    maxlen = curlen
                    maxstr = curstr
                    #print('maxstr is ',maxstr)

                # reset substr index to after the first occurance of repetition
                repIndex = curstr.find(s[end])
                start += repIndex+1
                end += 1
                
                newsubstr = s[start:end]
                #curlen = end-start
                curlen = len(newsubstr)
                #print('newsubstr is ',newsubstr)
                #print(start, end)
                alphabet = set(newsubstr)   # reset alphabet set with newsubstr
            else:
                # if no repeated character found
                # update character set, end index, length of substr
                alphabet.add(s[end])
                end += 1
                curlen += 1
                
        if(curlen>maxlen):
            maxlen = curlen
            maxstr = s[start:end]
            #print('maxstr is ',maxstr)
        
        return maxlen