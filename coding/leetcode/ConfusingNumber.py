# -*- coding: utf-8 -*-
"""
Created on June 11, 2019
LeetCode problem 1056
Given a number N, return true if and only if it is a confusing
number, which satisfies the following condition:

We can rotate digits by 180 degrees to form new digits. When
0, 1, 6, 8, 9 are rotated 180 degrees, they become 0, 1, 9,
8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees,
they become invalid. A confusing number is a number that when
rotated 180 degrees becomes a different number with each
digit valid.

Example 1:
Input: 6
Output: true
Explanation: 
We get 9 after rotating 6, 9 is a valid number and 9!=6.

Example 2:
Input: 89
Output: true
Explanation: 
We get 68 after rotating 89, 86 is a valid number and 86!=89.

Example 3:
Input: 11
Output: false
Explanation: 
We get 11 after rotating 11, 11 is a valid number but the value
remains the same, thus 11 is not a confusing number.

Example 4:
Input: 25
Output: false
Explanation: 
We get an invalid number after rotating 25.
 
Note:
0 <= N <= 10^9
After the rotation we can ignore leading zeros, for example if
after rotation we have 0008 then this number is considered as
just 8.
@author: K Li
"""
class Solution:
    def confusingNumber1(self, N: int) -> bool:
        if N == 0:
            return False
        mapping = {0:0, 1:1, 6:9, 8:8, 9:6}
        # convert number to list
        nums = []
        while N > 0:
            N, r = divmod(N, 10)
            nums.append(r)
        L = len(nums)
        # actually 10 -> 01, 01 may not be a va;id number
        #if L>1 and nums[0]==0:
        #    return False
        lo, hi = 0, L-1
        equal = True
        while lo<=hi:
            # check whether a valid number
            if nums[lo] in mapping and nums[hi] in mapping:
                # check if equal
                if mapping[nums[lo]] != nums[hi] or mapping[nums[hi]] != nums[lo]:
                    equal = False
            else:
                return False
            lo += 1
            hi -= 1
        return not equal
        
    def confusingNumber(self, N: int) -> bool:
        # simple solution
        mapping = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        s = str(N)
        valid = set(s).issubset('01689')
        if valid:
            s_180 = [mapping.get(c) for c in s][::-1]
            # print(s, ''.join(s_180))
            return s!=''.join(s_180)
        else:
            return valid
