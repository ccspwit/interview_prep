# -*- coding: utf-8 -*-
"""
Created on May 31, 2017
LeetCode problem 266, 267 combined
---#266
Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

---#267
Given a string s, return all the palindromic permutations (without duplicates)
of it. Return an empty list if no palindromic permutation could be form.

For example:
Given s = "aabb", return ["abba", "baab"].
Given s = "abc", return [].
@author: K Li
"""

class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)<=1:
            return True
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch,0)+1
        oddCount = 0
        #print(cnt)
        for freq in cnt.values():
            if (freq&1)==1:
                oddCount += 1
            if oddCount>1:
                return False
        return True

    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        

if __name__ == '__main__':
    a = Solution()
    testVector = ["code","aab",
                  "carerac"]
    a = Solution()
    print("Palindrome permutation")
    for test in testVector:
        #print(test)
        print("%s is %s"%(test, a.canPermutePalindrome(test)))
