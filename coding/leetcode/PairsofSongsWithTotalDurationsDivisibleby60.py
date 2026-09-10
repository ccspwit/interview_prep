# -*- coding: utf-8 -*-
"""
Created on June 15, 2019
LeetCode problem 1010
In a list of songs, the i-th song has a duration of time[i] seconds. 

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

Example 1:
Input: [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Example 2:
Input: [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.
 
Note:
1 <= time.length <= 60000
1 <= time[i] <= 500
@author: K Li
"""
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # first creat a %60 dictionary
        rem_count = {}
        for t in time:
            rem = t % 60
            rem_count[rem] = rem_count.get(rem, 0) + 1

        rem_list = list(rem_count.keys())
        print(rem_list)
        # loop over all combination
        pairs, N = 0, len(rem_list)
        for n in range(0, N-1):
            for m in range(n+1, N):
                if (rem_list[n]+rem_list[m]) % 60 == 0:
                    pairs += rem_count[rem_list[n]] * rem_count[rem_list[m]]
        if 30 in rem_count:
            pairs += rem_count[30]*(rem_count[30]-1)//2
        if 0 in rem_count:
            pairs += rem_count[0]*(rem_count[0]-1)//2
        return pairs
