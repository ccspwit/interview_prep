# -*- coding: utf-8 -*-
"""
Created on June 5, 2017
LeetCode problem 57
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
@author: K Li
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        N = len(intervals)
        #if N==0: return [newInterval]
        result =[]
        newS, newE = newInterval.start, newInterval.end
        s_bound = self.searchLastSmaller(intervals, newS)
        e_bound = self.searchLastSmaller(intervals, newE)
        
        if e_bound>=0:
            newInterval.end = max(newE, intervals[e_bound].end)
            
        # merge interval
        if s_bound==-1:
            if e_bound==-1:
                # add [1,2] to [3,4]
                return [newInterval]+intervals
            else:
                # add [1,3] to [2,4]
                return [newInterval]+intervals[e_bound+1:]
        elif newS>intervals[s_bound].end:
            # add [3,4] to [1,2]
            return intervals[:s_bound+1]+[newInterval]+intervals[e_bound+1:]
        else:
            # add [3,5] to [2,4]
            newInterval.start = intervals[s_bound].start
            return intervals[:s_bound]+[newInterval]+intervals[e_bound+1:]

    def searchLastSmaller(self, arr, val):
        """
        Binary search
        find last end index smaller than or equal to new start
        """
        l, r = 0, len(arr)-1
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if val<arr[mid].start:
                r = mid-1
            elif val>arr[mid].start:
                ans = mid
                l = mid+1
            else:
                return mid
        return ans

    def insert1(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        Actually code using sequential insert/merge is more reable without
        much performance loss.
        """
        if not intervals:
            return [newInterval]
        if not newInterval:
            return intervals
        N = len(intervals)
        #if N==0: return [newInterval]
        result =[]
        newS, newE = newInterval.start, newInterval.end
        
        pos = 0
        # traversa the intervals, merge if overlap
        for n in range(N):
            inter = intervals[n]
            # there are 6 cases to consider
            if (newE<inter.start):
                #print(1)
                # add [1,2] to [3,5]
                result += [newInterval]+intervals[n:]
                return result
            if (newS<=inter.start) and (newE<=inter.end):
                # add to [2,4] to [3,5], merge and return
                #print(2)
                intervals[n].start = newS
                result += intervals[n:]
                return result
            if (newS<=inter.start) and (newE>inter.end):
                # add to [2,6] to [3,5], merge get a new newInterval
                #print(3)
                continue
            if (newS >= inter.start) and (newE<=inter.end):
                # add to [3,4] to [3,5], merge and return
                #inter.start = newS
                #print(4)
                result += intervals[n:]
                return result
            if (newS<=inter.end) and (newE>inter.end):
                # add to [4,6] to [3,5], merge get a new newInterval
                #print(5)
                newInterval.start = inter.start
                newS = inter.start
                continue
            if (newS>inter.end):
                # add [6,7] to [3,5]
                #print(6)
                result.append(inter)
                continue

        result.append(newInterval)
        return result
    
    

        
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([[0,2],[5,8]],[-2,-1]),
                  ([[0,2],[5,8]],[-1,1]),
                  ([[0,2],[5,8]],[-1,3]),
                  ([[0,2],[5,8]],[1,2]),
                  ([[0,2],[5,8]],[1,3]),
                  ([[0,2],[5,8]],[1,6]),
                  ([[0,2],[5,8]],[3,4]),
                  ([[0,2],[5,8]],[3,6]),
                  ([[0,2],[5,8]],[3,9]),
                  ([[0,2],[5,8]],[6,10]),
                  ([[0,2],[5,8]],[9,10]),
                  ([[1,3],[6,9]],[10,11]),
                  ([[1,3],[6,9]],[2,5]),
                  ([[1,2],[3,5],[7,8],[9,11],[12,16]],[6,9])]
    a = Solution()
    #testVector = []
    #[([[1,2],[3,5],[6,7],[8,10],[12,16]],[8,9])]
    #print("Meeting room I")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = []
        for intv in test[0]:
            x.append(Interval(intv[0], intv[1]))
            
        print([(i.start, i.end) for i in x])
        y = Interval(test[1][0], test[1][1])
        z = a.insert(x,y)
        z1 = a.insert1(x,y)
        print("\nNew intervals are ",[(i.start,i.end) for i in z])
        print("\nNew intervals are ",[(i.start,i.end) for i in z1])
    #test = sorted(random.randint(0,100,100))
