# -*- coding: utf-8 -*-
"""
Created on June 7, 2017
LeetCode problem 139
Given a non-empty string s and a dictionary wordDict containing a list of
non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
@author: K Li
"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        Dynamic programming solution
        O(n2) time, O(n) space
        """
        N = len(s)
        dp = [False for _ in range(N)]
        
        for i in range(N):
            for w in wordDict:
                M = len(w)
                if w == s[i-M+1:i+1] and (dp[i-M] or i-M == -1):
                    dp[i] = True
        return dp[-1]

    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        Dynamic programming solution. Not sliding windows interpretation
        O(n2) time, O(n) space
        """
        N = len(s)
        wordSet = set(wordDict)
        dp = [False for _ in range(N+1)]
        dp[0] = True
        
        for i in range(1,N+1):
            for j in range(i):
                dp [i] = dp[j]&(s[j:i] in wordSet)
                if dp[i]:
                    break
        print(dp)
        return dp[-1]

if __name__ == '__main__':
    a = Solution()
    testVector = [("abc",["a","b","c","d"]),
                  ("aaaaaaa",["aaaa","aaa"]),
                  ("leetcode",["leet","code"]),
                  ("catseathotdog",["cat","dog","hot","eat","the"])]
    a = Solution()
    #testVector = ["AAAAAAAAAAA"]
    print("Palindrome permutation")
    for test in testVector:
        print(test)
        print("Can broken into words: ",a.wordBreak(test[0],test[1]))
