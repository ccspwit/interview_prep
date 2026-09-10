# -*- coding: utf-8 -*-
"""
Created on Jan 19, 2020
LeetCode problem 744
Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.
Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
@author: K Li
"""
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        N = len(letters)
        low, high = 0, N-1
        while low < high:
            mid = (low+high) // 2
            if target >= letters[mid]:
                low = mid + 1
            else:
                high = mid
        # check whethe need to wrap around
        if letters[low] <= target:
            low += 1
        return letters[low % N]
