# -*- coding: utf-8 -*-
"""
Created on Tue May 9, 2017
LeetCode problem 56
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
@author: K Li
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        N = len(intervals)
        if N<=1:
            return intervals
        sortedList = sorted(intervals, key = lambda x:x.start)
        result = [sortedList[0]]
        
        for n in range(1,N):
            if sortedList[n].start<=result[-1].end:
                if sortedList[n].end > result[-1].end:
                    result[-1].end = sortedList[n].end
            else:
                result.append(sortedList[n])
                
        return result
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[[1,3],[2,6],[8,10],[15,18]],
                  [[1,9],[2,6],[8,10],[15,18],[16,17]]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        x = []
        for interval in test:
            x.append(Interval(interval[0], interval[1]))
            
        print([(i.start, i.end) for i in x])
        y = a.merge(x)
        print([(i.start, i.end) for i in y])
    #test = sorted(random.randint(0,100,100))
