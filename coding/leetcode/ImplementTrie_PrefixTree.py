# -*- coding: utf-8 -*-
"""
Created on June 9, 2017
LeetCode problem 208
Implement a trie with insert, search, and startsWith methods.
Note:
You may assume that all inputs are consist of lowercase letters a-z.
@author: K Li
"""

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.isEnd = False

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curNode = self.root
        for ch in word:
            if ch not in curNode.children:
                curNode.children[ch] = TrieNode()
            curNode = curNode.children[ch]
        curNode.isEnd = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curNode = self.root
        for ch in word:
            curNode = curNode.children.get(ch, None)
            if curNode is None:
                return False
        return curNode.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curNode = self.root
        for ch in prefix:
            curNode = curNode.children.get(ch, None)
            if curNode is None:
                return False
        return True

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    a = Trie()
