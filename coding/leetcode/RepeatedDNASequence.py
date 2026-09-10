# -*- coding: utf-8 -*-
"""
Created on June 3rd, 2017
LeetCode problem 187
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
Return:
["AAAAACCCCC", "CCCCCAAAAA"].
@author: K Li
"""

class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        N=len(s)
        if N<=10:
            return []
        binMap = {"A":0, "C":1, "G":2, "T":3}
        repeat, added = set(), set()
        mask = 0xfffff
        slidingVal = 0
        result = []

        for n in range(N):
            val = binMap[s[n]]
            slidingVal |= val
            if n>=9:
                if slidingVal in repeat:
                    if slidingVal not in added:
                        added.add(slidingVal)
                        result.append(s[(n-9):(n+1)])
                else:
                    repeat.add(slidingVal)
            slidingVal = (slidingVal<<2)&mask

        #print(repeat, added)
        return result

    def findRepeatedDnaSequences2(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        N=len(s)
        if N<=10:
            return []
        pattern = {}    #{'A':[],'C':[],'G':[],'T':[]}
        result = []
        for n in range(N-10+1):
            subs = s[n:n+10]
            pattern[subs] = pattern.get(subs,0)+1
        result = [key for key in pattern if pattern[key]>1]
        return result

    def findRepeatedDnaSequences1(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        N=len(s)
        if N<=10:
            return []
        self.pattern = {}    #{'A':[],'C':[],'G':[],'T':[]}
        for n in range(N-10+1):
            subs = s[n:n+10]
            self.pattern[subs] = self.pattern.get(subs,[])+[n]

        result = []
        for pat, pos in self.pattern.items():
            if len(pos)>=2:
                p1 = pos[0]
                result.append(s[p1:p1+10])
        
        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = ["AAAAAAAAAAA",
                  "AAAAACCCCCA",
                  "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
                  "AAAAACCCCCAAAAAAACCCCCCCCAAAAAGGGTTT",                  
                  "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTTAAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"]
    a = Solution()
    #testVector = ["AAAAAAAAAAA"]
    print("Palindrome permutation")
    for test in testVector:
        print(test)
        print("Repeated DNA sequences: ",a.findRepeatedDnaSequences(test))
        print("Repeated DNA sequences: ",a.findRepeatedDnaSequences1(test))