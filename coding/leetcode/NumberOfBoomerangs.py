# -*- coding: utf-8 -*-
"""
Created on May 19, 2017
LeetCode problem 447
Given n points in the plane that are all pairwise distinct, a "boomerang" is
a tuple of points (i, j, k) such that the distance between i and j equals
the distance between i and k (the order of the tuple matters).

Find the number of boomerangs. You may assume that n will be at most 500 and
coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]

Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]

@author: K Li
"""

class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        for each points, creat a hashmap of points with distance as key
        or more efficiently, count the number of points to i with same distance
        """
        N = len(points)
        if N<=2:
            return 0

        number = 0
        # compute distance for all other points
        for i in range(N):
            distDict = {}
            for j in range(N):
                if i!=j:
                    d = (points[j][0]-points[i][0])**2+\
                    (points[j][1]-points[i][1])**2
                    
                    distDict[d] = distDict.get(d,0)+1

            for count in distDict.values():
                number += count*(count-1)
        
        return number

    def numberOfBoomerangs1(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        TLE error.
        """
        N = len(points)
        if N<=2:
            return 0

        distDict = {}
        # compute distance for all possible pairs of points
        for i in range(N-1):
            for j in range(i+1,N):
                d = (points[j][0]-points[i][0])**2+\
                (points[j][1]-points[i][1])**2
                if d not in distDict:
                    distDict[d] = [{i,j}]
                else:
                    distDict[d].append({i,j})
        number = 0
        
        print(distDict)
        # if two pairs share one common points, form a boomerang pair
        # this is not computation efficient, because total pairs of points
        # could be in the order of O(n^2), double looping of all pairs is
        # just too costly
        for k, v in distDict.items():
            pairs = len(v)
            if pairs>=2:
                for i in range(pairs-1):
                    for j in range(i+1, pairs):
                        if v[i]&v[j]:
                            number += 2
        return number
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[],[[1,1]],[[0,0],[1,0],[2,0]],
                  [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0]]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Number of boomerangs is: ',a.numberOfBoomerangs(test))
        print('Number of boomerangs is: ',a.numberOfBoomerangs1(test))

    t = list(range(1,1000))
    t[100] = 999