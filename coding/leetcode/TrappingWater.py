# -*- coding: utf-8 -*-
"""
Created on Thu May 30, 2017
LeetCode problem 42
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

@author: K Li
"""
import matplotlib.pyplot as plt
import seaborn as sns

class Solution(object):
    def trap(self, height):
        """
        Two pointer solution. Really concise solution. Really amazing!
        The idea is water filling from left and right.
        """
        n = len(height)
        l, r, water, minHeight = 0, n - 1, 0, 0
        while l < r:
            while l < r and height[l] <= minHeight:
                water += minHeight - height[l]
                l += 1
            while r > l and height[r] <= minHeight:
                water += minHeight - height[r]
                r -= 1
            minHeight = min(height[l], height[r])
        return water

    def trap1(self, height):
        '''
        Compute water volume from left to right
        1st pass: find all edge points in the chart.
        The edge is defined by greater than left point, and also greater than
        right point. Except for at the begining and the end.
        water hold for this bin.
        2nd pass: merge edges from 1st pass. Remove all edges sourrounded by
        higher edges.
        3nd pass: compute water volume between valid edges.
        The idea is straightforward but the code is quite complicated.
        '''
        def calcVol(edges, h):
            M = len(edges)
            if M<=1:
                return 0
            volume = 0
            for n in range(1,M):
                lowBar = min(h[edges[n-1]], h[edges[n]])
                #print(edges[n-1]+1,edges[n], lowBar)
                for pos in range(edges[n-1]+1,edges[n]):
                    volume += max(lowBar - x[pos], 0)
                #print(volume)
            return volume
        
        x = height
        N = len(x)
        if N <= 2:
            return 0
    
        volume = 0
        edges = []
        # find all potential edge point
        edgeDetected = False
        for n, h in enumerate(x):
            if not edgeDetected:
                if (n<N-1) and (x[n]>x[n+1]):
                    edgeDetected = True
                    edges.append(n)
            else:
                if (n<N-1):
                    if (x[n-1]<x[n]) and (x[n]>=x[n+1]):
                        edges.append(n)
                else:
                    if x[n-1]<x[n]:
                        edges.append(n)
        #print('Edge pos:',edges)
        #print('Edge val:',[x[e] for e in edges])

        M = len(edges)
        if M<=1:
            return 0
        '''if M==2:
            return calcVol(edges, x)'''

        # merge edge points
        left, right = 0, 1
        #maxHeight = x[edges[0]]
        while right<len(edges):
            if right==left+1:
                if x[edges[right]] >= x[edges[right-1]]:
                    left, right = right, right+1
                else:
                    right += 1
            else:
                if x[edges[right]] >= x[edges[right-1]]:
                    edges.pop(right-1)
                    right -= 1
                else:
                    right += 1
        #print('Edge pos:',edges)
        #print('Edge val:',[x[e] for e in edges])
        
        # compute volume of rain water
        return calcVol(edges, x)

if __name__ == '__main__':
    a = Solution()
    testVector = [[1,2],    #0
                  [3, 1 ,2, 4], #3
                  [0,1,0,2,1,0,1,3,2,1,2,1],    #6
                  [5,4,1,2],    #1
                  [16, 3, 17, 10, 9, 12, 13, 6, 6, 7, 8, 13, 7, 16, 15, 8, 3, 6, 17, 7]]
    a = Solution()
    for test in testVector:
        print(test)
        print("Water trapped ",(a.trap(test)))
        print("Water trapped ",(a.trap1(test)))
    
    #test = np.random.randint(0,20,20)