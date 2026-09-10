# -*- coding: utf-8 -*-
"""
Created on June 3rd, 2017
LeetCode problem 149
Given n points on a 2D plane, find the maximum number of points that lie on
the same straight line.
@author: K Li
"""

# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        def lineProperty(p1, p2):
            """
            To avoid rounding error when represent a line by y=kx+b,
            use representation ay+bx+c=0, where a,b,c are all integers.
            1. Handle case where a.x==b.x
            2. Divide by GCD to keep uniqueness
            """
            dx = p2[0]-p1[0]
            dy = p2[1]-p1[1]
            # no special treatment of dx==0 is needed
            a,b,c = dx, -dy, p1[1]*p2[0]-p1[0]*p2[1]
            if (a<0) or (a==0 and b<0):
                a, b, c = -a, -b, -c
            g = self.gcd(self.gcd(abs(a),abs(b)),abs(c))
            #print(a,b,c,g)
            return (a//g, b//g, c//g)
        
        pointTuples = [(pts.x, pts.y) for pts in points]
        counter = {}
        for x,y in pointTuples:
            counter[(x, y)] = counter.get((x, y),0)+1
        uPoints = list(set(pointTuples))
        N = len(uPoints)
        if N==0:
            return 0
        if N==1:
            return counter[(uPoints[0][0],uPoints[0][1])]
        lineMap = {}
        for n in range(N-1):
            for m in range(n+1, N):
                p1, p2 = uPoints[n], uPoints[m]
                a, b, c = lineProperty(p1, p2)
                if (a,b,c) not in lineMap:
                    lineMap[(a,b,c)] = set([(p1[0], p1[1]),(p2[0], p2[1])])
                else:
                    lineMap[(a,b,c)].update([(p1[0], p1[1]),(p2[0], p2[1])])
        maxPoints = 0
        
        for pSet in lineMap.values():
            nPoints = sum([counter[(x,y)] for x, y in pSet])
            maxPoints = max(maxPoints, nPoints)
        return maxPoints

    def gcd(self, a, b):
        """ Compute GCD, greatest common divisor
        """
        while b:
            a, b = b, a % b
        return a
    
if __name__ == '__main__':
    import numpy as np
    testVector = [[],[[1,2],[1,2],[1,2]],
                  [[1,2], [3,6], [1,1], [1,3],[1,3]],
                   [[0, 0], [1, 8], [11, 4], [7, 0], [9, 11], [8, 1], [3, 6], [0, 9], [9, 9], [7, 4], [10, 5], [11, 1]]]
    a = Solution()
    print("Maximum points on a line.")
    for test in testVector:
        x = []
        for p in test:
            x.append(Point(p[0], p[1]))
        print("Max points on a line? ", a.maxPoints(x))
    x1 = np.random.randint(0,12,12)
    x2 = np.random.randint(0,12,12)
    test = [[x,y] for x,y in zip(x1,x2)]
    print(test)
