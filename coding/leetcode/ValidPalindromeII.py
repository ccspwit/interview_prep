# -*- coding: utf-8 -*-
"""
Created on June 3, 2019
LeetCode problem 680
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
@author: K Li
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # becareful, there are two possible ways to delete one char
        def deletePalindrome(substr, del_count):
            N = len(substr)
            if N <= 1:
                return True
            l, r = 0, N-1

            while l < r:
                if substr[l] == substr[r]:
                    l += 1
                    r -= 1
                else:
                    if del_count >= 1:
                        return False
                    else:
                        return deletePalindrome(substr[l:r], 1) or deletePalindrome(substr[l+1:r+1], 1)
            return True

        return deletePalindrome(s, 0)
