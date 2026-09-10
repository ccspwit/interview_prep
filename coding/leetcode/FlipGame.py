# -*- coding: utf-8 -*-
"""
Created on May 31, 2017
LeetCode problem 293
You are playing the following Flip Game with your friend: Given a string
that contains only these two characters: + and -, you and your friend take
turns to flip two consecutive "++" into "--". The game ends when a person
can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid
move.

For example, given s = "++++", after one move, it may become one of the
following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list [].@author: K Li
"""

class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        for n in range(len(s)-1):
            if s[n]=="+" and s[n+1]=="+":
                result.append(s[:n]+"--"+s[n+2:])
        return result

if __name__ == '__main__':
    a = Solution()
    testVector = ["--++", "+--+", "++++","++-+--++++-"]

    a = Solution()
    print("Palindrome permutation")
    for test in testVector:
        print(test)
        print("After one move", a.generatePossibleNextMoves(test))
        #print("%s is %s"%(test, a.isStrobogrammatic1(test)))
