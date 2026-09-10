# -*- coding: utf-8 -*-
"""
Created on June 15, 2019
LeetCode problem 1037
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
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        # compare slope, use multiplication to avoid float error
        # points are all distinct
        x, y, z = points

        return (y[1]-x[1]) * (z[0]-y[0]) != (z[1]-y[1]) * (y[0]-x[0])

    def isBoomerang1(self, points: List[List[int]]) -> bool:
       # compute distance, a little expensive to compute
        # subject to float error
        def distance(p1, p2):
            return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**0.5
        N = len(points)
        dist = [0 for _ in range(N)]
        dist[0] = distance(points[0], points[1])
        dist[1] = distance(points[0], points[2])
        dist[2] = distance(points[1], points[2])

        sort_dist = sorted(dist)
        print(sort_dist)
        return sort_dist[2] != (sort_dist[0]+sort_dist[1])
