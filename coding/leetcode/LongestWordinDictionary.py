# -*- coding: utf-8 -*-
"""
Created on Jan 18, 2020
LeetCode problem 720
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
Example 1:
Input: 
words = ["w","wo","wor","worl", "world"]
Output: "world"
Explanation: 
The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: 
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
Output: "apple"
Explanation: 
Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".
Note:

All the strings in the input will only contain lowercase letters.
The length of words will be in the range [1, 1000].
The length of words[i] will be in the range [1, 30].
@author: K Li
"""
class Solution:
    def longestWord(self, words: List[str]) -> str:
        # first save words in set, no need to dict_by_len
        wordset = set(words)
        # sort word by len desc, word asc
        w_sorted = sorted(words, key=lambda w: (-len(w), w))
        for w in w_sorted:
            l = len(w)
            # NOTE all([]) is True, any([]) is False
            if all([w[:n] in wordset for n in range(l-1, 0, -1)]):
                return w
        return ''

    def longestWord_bruteforce(self, words: List[str]) -> str:
        set_by_len = {}
        # store word by length
        max_len = 0
        for w in words:
            l = len(w)
            if l > max_len:
                max_len = l
            if l not in set_by_len:
                # NOTE initialize with set([ele])
                set_by_len[l] = set([w])
            else:
                set_by_len[l].add(w)
        # iterate through set_by_len in reverse
        # find the longest word
        for l in range(max_len, 0, -1):
            matched = []
            # set_by_len[l] may not exist
            for w in set_by_len.get(l, []):
                prefix_matched = True
                for m in range(l-1, 0, -1):
                    # set_by_len[m] may not exist
                    if w[:m] not in set_by_len.get(m, set()):
                        prefix_matched = False
                        break
                if prefix_matched == True:
                    matched.append(w)
            if matched:
                return sorted(matched)[0]
        return ''

