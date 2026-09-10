# -*- coding: utf-8 -*-
"""
Created on June 3rd, 2017
LeetCode problem 422
Given a sequence of words, check whether it forms a valid word square.
A sequence of words forms a valid word square if the kth row and column read
the exact same string, where 0 ≤ k < max(numRows, numColumns).

Note:
The number of words given is at least 1 and does not exceed 500.
Word length will be at least 1 and does not exceed 500.
Each word contains only lowercase English alphabet a-z.

Example 1:
Input:
[ "abcd",
  "bnrt",
  "crmy",
  "dtye"]
Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crmy".
The fourth row and fourth column both read "dtye".
Therefore, it is a valid word square.

Example 2:
Input:
[ "abcd",
  "bnrt",
  "crm",
  "dt"]
Output:
true

Explanation:
The first row and first column both read "abcd".
The second row and second column both read "bnrt".
The third row and third column both read "crm".
The fourth row and fourth column both read "dt".
Therefore, it is a valid word square.

Example 3:
Input:
[ "ball",
  "area",
  "read",
  "lady"]

Output:
false

Explanation:
The third row reads "read" while the third column reads "lead".
Therefore, it is NOT a valid word square.
@author: K Li
"""

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        nRows, nCols = len(words), len(words)
        # three false conditions:
        # row too short, row too long, mismatch
        for r, row in enumerate(words):
            cols = len(row)
            if cols > nRows:
                return False
            for c in range(r+1, nRows):
                # check for extra columns
                x = words[r][c] if c < cols else ""
                # check for missing columns
                # rth col of cth row may not exist
                y = words[c][r] if r<len(words[c]) else ""
                if x!=y:
                    return False
        return True

if __name__ == '__main__':
    a = Solution()
    testVector = [["abcd",
                   "bnrt",
                   "crmy",
                   "dtye"],
                  ["ball",
                   "area",
                   "read",
                   "lady"],
                  ["abcd",
                   "bnrt",
                   "crm",
                   "d"],
                  ["abcd",
                   "bnrt",
                   "crm",
                   "dt"],
                  ["abcd",
                   "bnrt",
                   "crm",
                   "dtt"]]
    a = Solution()
    print("Palindrome permutation")
    for test in testVector:
        for i in range(len(test)): print(test[i])
        print("Valid abbrevation? ", a.validWordSquare(test))
