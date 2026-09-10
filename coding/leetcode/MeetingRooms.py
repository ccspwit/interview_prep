# -*- coding: utf-8 -*-
"""
Created on June 2nd, 2017
LeetCode problem 252, 253 combined
---#252
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return false.

---#253
Given an array of meeting time intervals consisting of start and end times
[[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms
required.

For example,
Given [[0, 30],[5, 10],[15, 20]],
return 2.
@author: K Li
"""

# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        N = len(intervals)
        intervals.sort(key = lambda x:x.start)
        if intervals:
            prevEnd = intervals[0].end
        for itv in intervals[1:]:
            if prevEnd > itv.start:
                return False
            prevEnd = itv.end
        return True

    def canAttendMeetings1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        N = len(intervals)
        """if N<=1:
            return True"""
        itv = sorted(intervals, key = lambda x:x.start)
        for n in range(N-1):
            if itv[n].end > itv[n+1].start:
                return False
        return True

    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        Another idea
        Chronically list all start time and end time regardless of original
        interval order. Compare start and end one by one.
        """
        N = len(intervals)
        if N<=1:
            return N
        starts = [i.start for i in intervals]
        ends = [i.end for i in intervals]
        starts.sort()
        ends.sort()

        nRooms, emptyRooms = 0, 0
        s, e = 0, 0
        while s<N:
            if starts[s]<ends[e]:
                if emptyRooms:
                    emptyRooms -= 1
                else:
                    nRooms += 1
                s += 1
            else:
                emptyRooms += 1
                e += 1
            #print(s,e)
        return nRooms

    def minMeetingRooms1(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        Based on the following simple idea.
        Suppose right now maximal m meeting rooms are used, when next
        appointment arrives, check if there are open rooms, where meetings are
        already endend existing.end <= new.start. If yes, pick a room, update
        interval, if not, get a new room.
        """
        N = len(intervals)
        if N<=1:
            return N
        intervals.sort(key = lambda x:x.start)
        nRooms = 0
        rooms = []
        for itv in intervals:
            noRoom = True
            for room in rooms:
                if itv.start >= room.end:
                    noRoom = False
                    room.start = itv.start
                    room.end = itv.end
                    break
            if noRoom:
                rooms.append(itv)
                nRooms += 1
        return nRooms
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[], [[1,2]],[[7,10],[2,4]],
                  [[0,30],[5,10],[15,20]],
                  [[1,3],[2,6],[8,10],[15,18]],
                  [[1,100],[2,200],[3,300],[4,200],[300,400]],
                  [[1293,2986],[848,3846],[4284,5907],[4466,4781],[518,2918],[300,5870]]]
    a = Solution()
    #testVector = [[[1293,2986],[848,3846],[4284,5907],[4466,4781],[518,2918],[300,5870]]]
    #print("Meeting room I")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = []
        for interval in test:
            x.append(Interval(interval[0], interval[1]))
            
        print([(i.start, i.end) for i in x])
        print('Can %s attend'%("" if a.canAttendMeetings(x) else "NOT"))
        print("Need %d meeting rooms"%a.minMeetingRooms(x))
        print("Need %d meeting rooms"%a.minMeetingRooms1(x))
    #test = sorted(random.randint(0,100,100))
