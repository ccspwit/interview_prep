# -*- coding: utf-8 -*-
"""
Created on Oct 2nd, 2022
LeetCode problem 792
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".

Example 1:
Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:
Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2

Constraints:
1 <= s.length <= 5 * 104
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
@author: K Li
"""
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def isSubseq(string, w):
            # two pointer O(N)
            large, small = len(string), len(w)
            l, s = 0, 0
            while l<large and s<small:
                if string[l] == w[s]:
                    l += 1
                    s += 1
                else:
                    l += 1
            return s == small
        
        count = 0
        # save checked words
        cache = {}
        for word in words:
            if word not in cache:
                if isSubseq(s, word):
                    count += 1
                    cache[word] = 1
                else:
                    cache[word] = 0
            else:
                count += cache[word]
        return count
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [
        ["abcde", ["a","bb","acd","ace"]],
        ["dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]]
    ]
    a = Solution()
    for i, (target, words) in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(target)
        print("Number of matching subsequences", numMatchingSubseq(target, words))

