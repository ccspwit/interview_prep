# -*- coding: utf-8 -*-
"""
Created on Thu June 11, 2017
LeetCode problem 295
Median is the middle value in an ordered integer list. If the size of the
list is even, there is no middle value. So the median is the mean of the two
middle value.

Examples: 
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data
structure.
double findMedian() - Return the median of all elements so far.
For example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
@author: K Li
"""

class MedianFinder(object):
    import heapq

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = [] # smaller half of stream, max-heap, save negative number
        self.large = [] # larger half of stream, min-heap

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.small) == len(self.large):
            heapq.heappush(self.large, -heapq.heappushpop(self.small,-num))
        else:
            heapq.heappush(self.small, -heapq.heappushpop(self.large, num))

    def findMedian(self):
        """
        :rtype: float
        """
        S, L = len(self.small), len(self.large)
        if L>0:
            if L==S:
                return (-self.small[0]+self.large[0])/2.0
            else:
                return self.large[0]
        else:
            return None
        
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[1,3,5,7,9]]
    a = MedianFinder()
    #testVector = [[10,3,4,11,12,13]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)

        for n in test:
            print(a.findMedian())
            a.addNum(n)
