# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 36
Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled
with the character '.'.

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only
the filled cells need to be validated.
@author: K Li
"""

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        Amazing solution!!! Iterate all elements.
        Save all occurance of (row, ele), (ele, col), and
        (gridRow, gridCol, element).
        Use set operation to determine if duplicates exist
        """
        seen = []
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col != '.':
                    seen += [(col, j), (i,col), (i//3,j//3,col)]
        return len(seen)==len(set(seen))
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [["187654329",
                   "2........",
                   "3........",
                   "4........",
                   "5........",
                   "6........",
                   "7........",
                   "8........",
                   "9........"]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Is valid sudoku?',a.isValidSudoku(test))

    t = list(range(1,1000))
    t[100] = 999