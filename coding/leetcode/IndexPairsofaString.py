# -*- coding: utf-8 -*-
"""
Created on June 10, 2019
LeetCode problem 1065
Given a text string and words (a list of strings), return all index pairs [i, j] so that the substring text[i]...text[j] is in the list of words.

Example 1:
Input: text = "thestoryofleetcodeandme", words = ["story","fleet","leetcode"]
Output: [[3,7],[9,13],[10,17]]

Example 2:
Input: text = "ababa", words = ["aba","ab"]
Output: [[0,1],[0,2],[2,3],[2,4]]
Explanation: 
Notice that matches can overlap, see "aba" is found in [0,2] and [2,4].
 
Note:
All strings contains only lowercase English letters.
It's guaranteed that all strings in words are different.
1 <= text.length <= 100
1 <= words.length <= 20
1 <= words[i].length <= 50
Return the pairs [i,j] in sorted order (i.e. sort them by their first coordinate in case of ties sort them by their second coordinate).
@author: K Li
"""
class TrieNode():
    def __init__(self):
        self.child=collections.defaultdict(TrieNode)
        self.isword=False

class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        # brute force
        results = []
        N = len(text)
        for word in words:
            M = len(word)
            for n in range(N-M+1):
                if text[n:n+M] == word:
                    results.append([n, n+M-1])
        return sorted(results)

    def indexPairs1(self, text, words):
        # trie tree method, quick search
        def insert(word, root):
            for ch in word:
                root=root.child[ch]
            root.isword=True

        def searchAndAdd(idx, root):
            #do dfs start from idx to search
            #if bypass isword==True,add into res
            for i in range(idx, n):
                if text[i] not in root.child:
                    return False
                root=root.child[text[i]]
                if root.isword:
                    res.append([idx,i])
            
        res=[]
        n=len(text)
        root=TrieNode()
        word_set=set(words)
        #build Trie and search from each index from 0 to n
        for word in words:
            insert(word, root)
        for i in range(n):
            searchAndAdd(i, root)
        return res
