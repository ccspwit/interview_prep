# -*- coding: utf-8 -*-
"""
Created on Oct 3rd, 2022
LeetCode problem 207
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

Example 1:
Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.

Example 2:
Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Constraints:
1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
@author: K Li
"""
class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        def dfs(crs, alist):
            if crs in visited:
                return False
            visited.add(crs)
            for dep in alist[crs]:
                if not dfs(dep, alist):
                    return False
            visited.remove(crs)
            alist[crs] = []
            return True
        
        # create adjacent list
        alist = {n: [] for n in range(numCourses)}
        for crs, dep in prerequisites:
            alist[crs].append(dep)
        
        visited = set()
        for crs in range(numCourses):
            if not dfs(crs, alist):
                return False
            
        return True        
        

    def canFinish1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def isCyclic(dep, visited, checked):
            if checked[dep]:
                return False
            if visited[dep]:
                return True
            
            visited[dep] = True
            for crs in alist.get(dep, []):
                if isCyclic(crs, visited, checked):
                    visited[dep] = False
                    return True
            visited[dep] = False
            checked[dep] = True

            return False
            
        alist = {}
        # create adjacent list
        for crs, dep in prerequisites:
            if dep not in alist:
                alist[dep] = [crs]
            else:
                alist[dep].append(crs)
        
        # detect whether there exists a loop or not
        checked = [False]*numCourses
        visited = [False]*numCourses
        for dep in alist:
            if isCyclic(dep, visited, checked):
                return False
        return True

