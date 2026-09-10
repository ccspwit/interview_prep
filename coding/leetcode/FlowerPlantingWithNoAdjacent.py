# -*- coding: utf-8 -*-
"""
Created on June 14, 2019
LeetCode problem 1042
You have N gardens, labelled 1 to N.  In each garden, you want to plant one of 4 types of flowers.

paths[i] = [x, y] describes the existence of a bidirectional path from garden x to garden y.

Also, there is no garden that has more than 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)-th garden.  The flower types are denoted 1, 2, 3, or 4.  It is guaranteed an answer exists.

Example 1:
Input: N = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]

Example 2:
Input: N = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]

Example 3:
Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 
Note:
1 <= N <= 10000
0 <= paths.size <= 20000
No garden has 4 or more paths coming into or leaving it.
It is guaranteed an answer exists.
@author: K Li
"""
class Solution(object):
    def gardenNoAdj(self, N, paths):
        """
        :type N: int
        :type paths: List[List[int]]
        :rtype: List[int]
        """
        # graph
        G = {}
        # form graph
        for p in paths:
            if p[0] in G:
                G[p[0]].append(p[1])
            else:
                G[p[0]] = [p[1]]
            if p[1] in G:
                G[p[1]].append(p[0])
            else:
                G[p[1]] = [p[0]]

        ans = {k+1:0 for k in range(N)}
        colors = {1,2,3,4}
        for k in ans:
            if k in G:
                neighbor_colors = {ans[p2] for p2 in G[k]}
            else:
                neighbor_colors = set()
            candidates = colors.difference(neighbor_colors)
            ans[k] = candidates.pop()
            #print(k, neighbor_colors, candidates, ans)
        return [v for k, v in ans.items()]
