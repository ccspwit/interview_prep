# -*- coding: utf-8 -*-
"""
Created on May 31 2019
LeetCode problem 79
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent
cell, where "adjacent" cells are those horizontally or vertically
neighboring. The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
@author: K Li
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find_match(board, M, N, m, n, subword, trace):
            found = False
            next_coord = [(m-1, n), (m+1, n), (m, n-1), (m, n+1)]
            for x, y in next_coord:
                if (x>=0 and x<M) and (y>=0 and y<N) and (x, y) not in trace:
                    if board[x][y] == subword[0]:
                        if len(subword)==1:
                            return True
                        # trace.append((x,y))
                        if find_match(board, M, N, x, y, subword[1:], trace+[(x,y)]):
                            return True
            return found

        M, N = len(board), len(board[0])
        len_word = len(word)
        if not word:
            return False

        found = False
        for m in range(M):
            for n in range(N):
                if board[m][n] == word[0]:
                    if len_word == 1:
                        return True
                    if find_match(board, M, N, m, n, word[1:], [(m, n)]):
                        return True

        return found
