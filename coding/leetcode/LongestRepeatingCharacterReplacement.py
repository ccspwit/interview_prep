# -*- coding: utf-8 -*-
"""
Created on Oct 24th, 2022
LeetCode problem 424
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
@author: K Li
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # two pointer solution
        # keep track of max count within the window
        # optimal way of computing max_count hard to understand
        counter = {}
        l = 0
        max_count, res = 0, 0
        for r in range(len(s)):
            counter[s[r]] = counter.get(s[r], 0) + 1
            # max_count = max(counter.values())
            max_count = max(max_count, counter[s[r]])
            if (r - l + 1 - max_count <= k):
                res = max(res, r - l + 1)
            else:
                counter[s[l]] = counter[s[l]] - 1
                #if not counter[s[l]]:
                #    counter.pop(s[l])
                l += 1
            #print(counter)
            #print(l,r,res)
        return res
        

if __name__ == "__main__":
    a = Solution()
    testVector = [("ABAB", 2), ("AABABBA", 1), ("CBAAACBBBBBCA", 2)]
    for string, k in testVector:
        print(string, k)
        print('Longest Repeating Character Replacement ', a.characterReplacement(string, k))
