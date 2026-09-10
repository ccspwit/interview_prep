# -*- coding: utf-8 -*-
"""
Created on June 5, 2017
LeetCode problem 127
Given two words (beginWord and endWord), and a dictionary's word list, find
the length of shortest transformation sequence from beginWord to endWord,
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not
a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
UPDATE (2017/1/20):
The wordList parameter had been changed to a list of strings (instead of a
set of strings). Please reload the code definition to get the latest changes.
@author: K Li
"""

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        Perform BFS over dictionary for diff-1 word (same length)
        Use queue to perform BFS
        """
        from collections import deque
        if beginWord==endWord:
            return 1
        wordSet = set(wordList)
        if len(wordSet)==0 or (endWord not in wordSet):
            return 0
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        queue = deque()
        queue.append((beginWord,0))
        
        while queue:
            word, dist = queue.popleft()
            dist += 1
            if word==endWord:
                return dist
            for n in range(len(word)):
                for m in alpha:
                    if m!=word[n]:
                        newWord = word[:n]+m+word[n+1:]
                        if newWord in wordSet:
                            queue.append((newWord, dist))
                            wordSet.remove(newWord)
        return 0

    def ladderLength01(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        Perform BFS over dictionary for diff-1 word (same length)
        Use list to store all nodes of next level
        """
        if beginWord==endWord:
            return 1
        wordSet = set(wordList)
        if len(wordSet)==0 or (endWord not in wordSet):
            return 0
        
        alpha = "abcdefghijklmnopqrstuvwxyz"
        nextLevel = [beginWord]
        dist = 0
        found = False
        while nextLevel:
            curLevel = nextLevel
            nextLevel = []
            dist += 1
            for word in curLevel:
                if word==endWord:
                    return dist
                for n in range(len(word)):
                    for m in alpha:
                        if m!=word[n]:
                            newWord = word[:n]+m+word[n+1:]
                            if newWord in wordSet:
                                nextLevel.append(newWord)
                                wordSet.remove(newWord)
        return 0
    
if __name__ == '__main__':
    a = Solution()
    testVector = [("hot","dog",["hot","dog"]),
                  ("hit","cot",["hot","dot","dog","lot","log","cog"]),
                  ("hit","hit",["hot","dot","dog","lot","log","cog"]),
                  ("hit","hot",["hot","dot","dog","lot","log","cog"]),
                  ("hit","cog",["hot","dot","dog","lot","log","cog"])]
    a = Solution()
    #testVector = [("A","A")]
    for test in testVector:
        print(test)
        print("Number of steps ",(a.ladderLength(test[0],test[1],test[2])))
        print("Number of steps ",(a.ladderLength01(test[0],test[1],test[2])))
    
    #test = np.random.randint(0,20,20)