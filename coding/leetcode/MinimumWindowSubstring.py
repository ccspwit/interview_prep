# -*- coding: utf-8 -*-
"""
Created on June 4, 2017
LeetCode problem 76
Given a string S and a string T, find the minimum window in S which will
contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the
empty string "".
If there are multiple such windows, you are guaranteed that there will always
be only one unique minimum window in S.
@author: K Li
"""

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        Other's solution, similar idea. But code are quite clean
        """
        from collections import Counter, defaultdict
        st, c1, min_so_far, result, fmap = 0, Counter(t), len(s)+1, "", defaultdict(int)
        unique_ch = len(c1)
        for end in range(len(s)):
            if s[end] in c1:
                fmap[s[end]] += 1
                if fmap[s[end]] == c1[s[end]]:
                    unique_ch -= 1
                while st <= end and unique_ch == 0:
                    if end - st + 1 < min_so_far:
                        min_so_far, result = end - st + 1, s[st:end+1]
                    if s[st] in fmap:
                        fmap[s[st]] -= 1
                        if fmap[s[st]] < c1[s[st]]:
                            unique_ch += 1
                    st += 1
        return result
    
    def minWindow1(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        My solution, quite long, corner cases are tricky. Took some time to
        pass
        """
        N, M = len(s), len(t)
        if N<M:
            return ""
        freqS, freqT = {}, {}
        self.S, self.T = freqS, freqT
        for ch in t:
            freqT[ch] = freqT.get(ch, 0)+1        

        minLen = len(s)+1
        minWin = (0,N-1)
        start, end = 0, 0
        matchCount, matchFound = 0, False

        while end < N:
            ch = s[end]
            # first sliding end point to find a substring containing window
            if ch in freqT:
                freqS[ch] = freqS.get(ch, 0)+1
                if freqS[ch]<=freqT[ch]:
                    matchCount += 1
                if matchCount == M:
                    matchFound = True
                    #print('Move right',start,end)
            if matchFound or (end==N):
                #mtaching substring found, sliding start pointer
                while (start<=(end-(M-1))) and matchFound:
                    ch = s[start]
                    if ch in freqT:
                        if freqS[ch] > freqT[ch]:
                            freqS[ch] -= 1
                        elif freqS[ch] == freqT[ch]:
                            if (end-start+1)<minLen:
                                minLen = (end-start)+1
                                minWin = (start, end+1)
                            freqS[ch] -= 1
                            matchCount -= 1
                            matchFound = False
                            #print('Move left',start, end)
                    start += 1
            end += 1

        l,r = minWin
        #print(l,r,minLen,N)
        return s[l:r] if minLen<=N else ""
    
if __name__ == '__main__':
    a = Solution()
    testVector = [("A","B"),("A","A"),("AA","AB"),
                  ("cabwefgewcwaefgcf","cae"),
                  ("ADOBECODEBANC","ABC"),
                  ("ADOBECODEBANC","BBC")]
    a = Solution()
    #testVector = [("A","A")]
    for test in testVector:
        print(test)
        print("Minwindow substring: ",(a.minWindow(test[0],test[1])))
    
    #test = np.random.randint(0,20,20)