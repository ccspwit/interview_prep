# -*- coding: utf-8 -*-
"""
Created on June 15, 2019
LeetCode problem 1002
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

Example 1:
Input: ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: ["cool","lock","cook"]
Output: ["c","o"]
 
Note:
1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter
@author: K Li
"""
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        # loop over letters from first word
        output = []
        for letter in set(A[0]):
            count = 100
            for word in A:
                count = min(count, word.count(letter))
                if count == 0:
                    break
            if count > 0:
                output.extend(count*[letter])
        return output

    def commonChars1(self, A: List[str]) -> List[str]:
        # use counter dict
        counter = {}
        for ind, word in enumerate(A):
            temp = {}
            for ch in word:
                temp[ch] = temp.get(ch, 0)+1
            if ind==0:
                counter = temp
            else:
                key_list = list(counter.keys())
                for key in key_list:
                    if key in temp:
                        counter[key] = min(counter[key], temp[key])
                    else:
                        counter.pop(key)
                if not counter:
                    return []
            #print(counter, temp)
        # return counter
        ans = []
        for k, v in counter.items():
            ans.extend(v*[k])
        return ans
