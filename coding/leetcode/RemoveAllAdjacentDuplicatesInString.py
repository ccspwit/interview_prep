# -*- coding: utf-8 -*-
"""
Created on June 11, 2019
LeetCode problem 1047
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.
Return the final string after all such duplicate removals have been made.  It is guaranteed the answer is unique.

Example 1:
Input: "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

Note:
1 <= S.length <= 20000
S consists only of English lowercase letters.
@author: K Li
"""
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        use stack
        """
        st = []
        for n in range(len(S)):
            if st:
                if S[n] != st[-1]:
                    st.append(S[n])
                else:
                    st.pop()
            else:
                st.append(S[n])
        return "".join(st)
