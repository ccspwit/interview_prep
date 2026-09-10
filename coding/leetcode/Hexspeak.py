# -*- coding: utf-8 -*-
"""
Created on Feb 19, 2020
LeetCode problem 1271
A decimal number can be converted to its Hexspeak representation by first converting it to an uppercase hexadecimal string, then replacing all occurrences of the digit 0 with the letter O, and the digit 1 with the letter I.  Such a representation is valid if and only if it consists only of the letters in the set {"A", "B", "C", "D", "E", "F", "I", "O"}.
Given a string num representing a decimal integer N, return the Hexspeak representation of N if it is valid, otherwise return "ERROR".

Example 1:
Input: num = "257"
Output: "IOI"
Explanation:  257 is 101 in hexadecimal.

Example 2:
Input: num = "3"
Output: "ERROR"

Constraints:
1 <= N <= 10^12
There are no leading zeros in the given string.
All answers must be in uppercase letters.
@author: K Li
"""
class Solution:
    def toHexspeak(self, num: str) -> str:
        invalid=set("23456789")
        hex_string = f"{int(num):x}"
        if set(hex_string).intersection(invalid):
            return "ERROR"
        else:
            return hex_string.replace("0", 'o').replace('1','i').upper()
