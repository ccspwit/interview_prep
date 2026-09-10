# -*- coding: utf-8 -*-
"""
Created on Jan 20, 2020
LeetCode problem 746
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].
Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
@author: K Li
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost_2 = 0
        cost_1 = cost[0]
        # dynamic programming
        for n in range(1, len(cost)):
            cur_cost = cost[n] + min(cost_1, cost_2)
            cost_2, cost_1 = cost_1, cur_cost
        return min(cost_2, cost_1)