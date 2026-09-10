# -*- coding: utf-8 -*-
"""
Created on June 15, 2019
LeetCode problem 394
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:
s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
@author: K Li
"""
class Solution:
    def decodeString(self, s):
        # iterative using stack
        num = 0
        word = []
        wordStack, numStack = [], []
        
        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == '[':
                # store the current information to stack
                wordStack.append(word)
                numStack.append(num)
                
                # reset the current information
                word = []
                num = 0
            elif c == ']':
                res = wordStack.pop()
                num = numStack.pop()
                
                res += word * (num)
                
                # update current information
                word = res
                num = 0
            else:
                word.append(c)
        
        return ''.join(word)

    def decodeStringR(self, s: str) -> str:
        # recursive
        def decodeR(substr):
            # parse str into prefix, count, substr, suffix
            N = len(substr)
            ans = []
            stack = []
            start = 0
            while start < N:
                if substr[start].isalpha():
                    start += 1
                else:
                    break
            ans.append(substr[:start])
            if start == N:
                return substr
            prefix = substr[:start]
            mid = start
            while mid < N:
                if substr[mid].isnumeric():
                    mid += 1
                else:
                    break
            count = int(substr[start:mid])
            bracket_cnt = 0
            if substr[mid] == '[':
                bracket_cnt += 1
                start, end = mid+1, mid+1
            while bracket_cnt > 0:
                if substr[end] == '[':
                    bracket_cnt += 1
                if substr[end] == ']':
                    bracket_cnt -= 1
                end = end + 1
            mid_str = substr[start:end-1]
            suffix = substr[end:]
            print(prefix, mid_str, suffix)
            return prefix+count*decodeR(mid_str)+decodeR(suffix)
        
        return decodeR(s)
