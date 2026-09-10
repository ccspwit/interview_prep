# -*- coding: utf-8 -*-
"""
Created on May 25, 2017
LeetCode problem 344, 345 combined
---#344
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

---#345
Write a function that takes a string as input and reverse only the vowels of
a string.

Examples:
Given s = "hello", return "holle".
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

---#541
Given a string and an integer k, you need to reverse the first k characters
for every 2k characters counting from the start of the string. If there are
less than k characters left, reverse all of them. If there are less than 2k
but greater than or equal to k characters, then reverse the first k characters
and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
@author: K Li
"""

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        N = len(s)
        if (N<=1)|(k==1):
            return s
        if (k<1) & (k>10000):
            raise ValueError("k is out of [1,10000] range")
        revStr = ""
        left, right = 0, k
        while left<N:
            revStr += s[left:right][::-1]
            left += k
            right += k
            if left < N:
                revStr += s[left:right]
            left += k
            right += k
            
        return revStr
    
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        vowel = set("aeiouAEIOU")
        N = len(l)
        left, right = 0, N-1
        while left < right:
            while (left<right)&(l[left] not in vowel):
                left += 1
            if left>=right:
                break
            while (left<right)&(l[right] not in vowel):
                right -= 1
            if left>=right:
                break
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1
        return ''.join(l)

    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
    
if __name__ == '__main__':
    a = Solution()
    testVector = ["","Aa","heart","leetcode","universe"]
    a = Solution()
    for test in testVector:
        print(test)
        print("%s -- %s"%(test, a.reverseString(test)))
        print("%s -- %s"%(test, a.reverseVowels(test)))

    testVector = [("",0),("Aa",1),("Aa",2),
                  ("abcdefghijk",1),("abcdefghijk",2),("abcdefghijk",10),
                  ("leetcode",3),("universe",1)]
    print("\nReverse string II")
    for test in testVector:
        print(test[0], test[1])
        print("k-reversed string is %s"%(a.reverseStr(test[0], test[1])))

