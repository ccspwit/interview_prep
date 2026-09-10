# -*- coding: utf-8 -*-
"""
Created on Feb 20, 2020
LeetCode problem 1228
In some array arr, the values were in arithmetic progression: the values arr[i+1] - arr[i] are all equal for every 0 <= i < arr.length - 1.
Then, a value from arr was removed that was not the first or last value in the array.
Return the removed value.

Example 1:
Input: arr = [5,7,11,13]
Output: 9
Explanation: The previous array was [5,7,9,11,13].

Example 2:
Input: arr = [15,13,12]
Output: 14
Explanation: The previous array was [15,14,13,12].

Constraints:
3 <= arr.length <= 1000
0 <= arr[i] <= 10^5
@author: K Li
"""
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        missing_val = arr[0]
        for n in range(2, len(arr)):
            d1, d2 = arr[n-1]-arr[n-2], arr[n]-arr[n-1]
            if d1 > 0:
                if d1 == d2: continue
                elif d1 > d2:
                    missing_val = arr[n-1] - d2
                else:
                    missing_val = arr[n-1] + d1
            if d1 < 0:
                if d1 == d2: continue
                elif d1 > d2:
                    missing_val = arr[n-1] + d1
                else:
                    missing_val = arr[n-1] - d2
        return missing_val
