# -*- coding: utf-8 -*-
"""
Created on Feb 22, 2020
LeetCode problem 758
Given a set of keywords words and a string S, make all appearances of all keywords in S bold. Any letters between <b> and </b> tags become bold.
The returned string should use the least number of tags possible, and of course the tags should form a valid combination.

For example, given that words = ["ab", "bc"] and S = "aabcd", we should return "a<b>abc</b>d". Note that returning "a<b>a<b>b</b>c</b>d" would use more tags, so it is incorrect.

Note:
words has length in range [0, 50].
words[i] has length in range [1, 10].
S has length in range [0, 500].
All characters in words[i] and S are lowercase letters.
@author: K Li
"""
class Solution:
    def boldWords1(self, words: List[str], S: str) -> str:
        # brute force solution
        bold =[False for i in range(len(S))]
        
        # for each word, search for matched substr in S, marked as True
        for i in range(len(S)):
             for l in words:
                    if i+len(l)<=len(S) and S[i:i+len(l)]==l:
                        for j in range(len(l)):
                            bold[i+j]=True
        res = ''
        # find beginning and end of True block, insert <b></b>
        for i in range(len(bold)):
            if bold[i]:
                if i==0 or not bold[i-1]:
                    res+='<b>'
                res+=S[i]
                if i==len(bold)-1 or not bold[i+1]:
                    res+='</b>'
            else:
                res+=S[i]
                
        return res

    def boldWords(self, words: List[str], S: str) -> str:
        # again brute force, use string.find(word, start_index)
        mark = [False]*len(S) #true for bold char
        for word in words:
            i = -1
            while True: 
                i = S.find(word, i+1)
                if i == -1: break 
                for j in range(i, i+len(word)): mark[j] = True
        #insert tags      
        ans = []     
        for i in range(len(S)): 
            if mark[i] and (i == 0 or not mark[i-1]): ans.append("<b>")
            ans.append(S[i])
            if mark[i] and (i == len(S) - 1 or not mark[i+1]): ans.append("</b>")
        return "".join(ans)
