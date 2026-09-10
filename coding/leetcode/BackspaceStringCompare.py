# -*- coding: utf-8 -*-
"""
Created on June 7, 2019
LeetCode problem 844
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:
Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:
Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:
Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:
Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
@author: K Li
"""
class Solution:
    def backspaceCompareStack(self, S: str, T: str) -> bool:
    # use stack
        st1, st2 = [], []
        for ch in S:
            if ch != '#':
                st1.append(ch)
            else:
                if st1:
                    st1.pop()

        for ch in T:
            if ch != '#':
                st2.append(ch)
            else:
                if st2:
                    st2.pop()

        return ''.join(st1) == ''.join(st2)

    def backspaceCompare(self, S, T):
        # generator solution for reverse scan, really simple
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))

    def backspaceCompareReverse(self, S: str, T: str) -> bool:
        # more efficiently compare backward, the logic really complicated
        NS, NT = len(S), len(T)
        equal = True
        
        rs, rt = NS-1, NT-1
        s_bs, t_bs = 0, 0
        while rs>=0 or rt>=0:
            # check for next non '#' of S from right side
            bs_count = 0
            while rs>=0 and (S[rs]=='#' or bs_count>0):
                if bs_count > 0:
                    if S[rs] == '#':
                        bs_count += 1
                        rs -= 1
                    else:
                        bs_count -= 1
                        rs -= 1
                else:
                    # S[rs]=='#'
                    bs_count += 1
                    rs -= 1
            bs_count = 0
            while rt>=0 and (T[rt]=='#' or bs_count>0):
                if bs_count > 0:
                    if T[rt] == '#':
                        bs_count += 1
                        rt -= 1
                    else:
                        bs_count -= 1
                        rt -= 1
                else:
                    # S[rs]=='#'
                    bs_count += 1
                    rt -= 1
            # compare current character
            if rs>=0 and rt>=0:
                if S[rs] == T[rt]:
                    rs -= 1
                    rt -= 1
                else:
                    return False
            elif (rs>=0 and rt<0):
                if S[rs] != '#':
                    return False
            elif (rs<0 and rt>=0):
                if T[rt] != '#':
                    return False
        #if (rs>=0 and rt<0) or (rs<0 and rt>=0):
        #    return False
        return True
