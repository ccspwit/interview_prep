# -*- coding: utf-8 -*-
"""
Created on Jan 18, 2020
LeetCode problem 709
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

Example 1:
Input: "Hello"
Output: "hello"
Example 2:
Input: "here"
Output: "here"
Example 3:
Input: "LOVELY"
Output: "lovely"
@author: K Li
"""
class Solution:
    def toLowerCase(self, string: str) -> str:
        th1, th2, diff = ord('A'), ord('Z'), 32
        res = []
        for ch in string:
            res.append(chr(ord(ch) + 32) if th1<=ord(ch)<=th2 else ch)
        return ''.join(res)
