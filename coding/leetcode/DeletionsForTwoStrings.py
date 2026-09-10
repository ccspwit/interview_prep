# -*- coding: utf-8 -*-
"""
Created on May 27, 2017
LeetCode problem 583
Given two words word1 and word2, find the minimum number of steps required
to make word1 and word2 the same, where in each step you can delete one
character in either string.

Example 1:
Input: "sea", "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make
"eat" to "ea".
Note:
The length of given words won't exceed 500.
Characters in given words can only be lower-case letters.
@author: K Li
"""

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        N, M = len(word1), len(word2)
        return N+M-2*self.LongestCommonSubstring(word1, word2)
    
    def LongestCommonSubstring(self, w1, w2):
        """
        Compute the longest common substring of two strings.
        O(N*M) time, O(M) space
        """
        N, M = len(w1), len(w2)
        if (N==0)|(M==0):
            return 0
        dp1 = [0 for i in range(M+1)]
        dp2 = [0 for i in range(M+1)]

        for n in range(N):
            dp1, dp2 = dp2, dp1
            for m in range(M):
                if w1[n] == w2[m]:
                    dp2[m+1] = dp1[m] + 1
                else:
                    dp2[m+1] = max(dp1[m+1], dp2[m])
        return dp2[M]

    def minDistance1(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        N, M = len(word1), len(word2)
        return N+M-2*self.LongestCommonSubstring1(word1, word2)
    
    def LongestCommonSubstring1(self, w1, w2):
        """
        Compute the longest common substring of two strings.
        O(N*M) time, O(N*M) space
        """
        N, M = len(w1), len(w2)
        if (N==0)|(M==0):
            return 0
        dp = [[0 for i in range(M+1)] for j in range(N+1)]
        for n in range(N):
            for m in range(M):
                if w1[n] == w2[m]:
                    dp[n+1][m+1] = dp[n][m] + 1
                else:
                    dp[n+1][m+1] = max(dp[n][m+1], dp[n+1][m])
        return dp[N][M]
    
if __name__ == '__main__':
    a = Solution()
    testVector = [("","a"),("a",""),("a","aaa"),
                  ("sea","aet"),("leetcoding","linkedincode"),
                  ("heart","earth"),("intention","execution")]
    a = Solution()
    print("Minimal characters to delete")
    for test in testVector:
        #print(test)
        print("%s = %d"%(test, a.minDistance(test[0],test[1])))
        print("%s = %d"%(test, a.minDistance1(test[0],test[1])))
