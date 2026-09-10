# -*- coding: utf-8 -*-
"""
Created on Oct 2nd, 2022
LeetCode problem 1419
---#453
You are given the string croakOfFrogs, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so multiple "croak" are mixed.
Return the minimum number of different frogs to finish all the croaks in the given string.

A valid "croak" means a frog is printing five letters 'c', 'r', 'o', 'a', and 'k' sequentially. The frogs have to print all five letters to finish a croak. If the given string is not a combination of a valid "croak" return -1.

Example 1:
Input: croakOfFrogs = "croakcroak"
Output: 1 
Explanation: One frog yelling "croak" twice.

Example 2:
Input: croakOfFrogs = "crcoakroak"
Output: 2 
Explanation: The minimum number of frogs is two. 
The first frog could yell "crcoakroak".
The second frog could yell later "crcoakroak".

Example 3:
Input: croakOfFrogs = "croakcrook"
Output: -1
Explanation: The given string is an invalid combination of "croak" from different frogs.

Constraints:
1 <= croakOfFrogs.length <= 105
croakOfFrogs is either 'c', 'r', 'o', 'a', or 'k'.
@author: K Li
"""
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = 0
        croaks = [0]*len('croak')
        min_frogs = 0
        for ch in croakOfFrogs:
            if ch not in 'croak':
                return -1
            if ch == 'c':
                count += 1
                croaks[0] = croaks[0] + 1
            if ch == 'r':
                if croaks[1] < croaks[0]:
                    croaks[1] = croaks[1] + 1
                else:
                    return -1
            if ch == 'o':
                if croaks[2] < croaks[1]:
                    croaks[2] = croaks[2] + 1
                else:
                    return -1
            if ch == 'a':
                if croaks[3] < croaks[2]:
                    croaks[3] = croaks[3] + 1
                else:
                    return -1
            if ch == 'k':
                if croaks[4] < croaks[3]:
                    croaks[4] = croaks[4] + 1
                    count -= 1
                    min_frogs = max(min_frogs, croaks[0] - croaks[-1] + 1)
                else:
                    return -1
            # print(ch, min_frogs)
        for n in range(1, len('croak')):
            if croaks[n] != croaks[n-1]:
                return -1
        return min_frogs

        
if __name__ == '__main__':
    testVector = [
        "croakcroak",
        "crcoakroak",
        "croakcrook",
        "crccoakrroakoak"
    ]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Minimum Number of Frogs Croaking : ',a.minNumberOfFrogs(test))
