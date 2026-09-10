# -*- coding: utf-8 -*-
"""
Created on June 2, 2019
LeetCode problem 482
Given an array of characters, compress it in-place.
The length after compression must always be smaller than or equal to the original array.
Every element of the array should be a character (not int) of length 1.
After you are done modifying the input array in-place, return the new length of the array.

Follow up:
Could you solve it using only O(1) extra space?
 
Example 1:
Input:
["a","a","b","b","c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
 
Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array
should be: ["a"]
Explanation:
Nothing is replaced.
 
Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
 
Note:
All characters have an ASCII value in [35, 126].
1 <= len(chars) <= 1000.
@author: K Li
"""
class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        # remove '-'
        x = S.split('-')
        y = ''.join(x).upper()
        L = len(y)
        if (L%K) == 0:
            N, k = L//K, K
        else:
            N, k = (L//K)+1, L%K
        l = []
        for n in range(N):
            if n==0:
                l.append(y[:k])
            else:
                start, end = k+(n-1)*K, k+n*K
                l.append(y[start:end])
        return '-'.join(l)
