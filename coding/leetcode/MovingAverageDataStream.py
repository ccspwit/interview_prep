# -*- coding: utf-8 -*-
"""
Created on June 2nd, 2017
LeetCode problem 346
Given a stream of integers and a window size, calculate the moving average
of all integers in the sliding window.

For example,
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3

@author: K Li
"""

class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.mem = [0 for _ in range(size)]
        self.size = size
        self.ptr = 0
        self.sum = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        # treat memory as circular buffer
        self.ptr += 1
        circPtr = self.ptr %self.size
        nDelete = self.mem[circPtr]
        self.mem[circPtr] = val
        self.sum += (val-nDelete)
        return self.sum/float(min(self.ptr, self.size))

    def __init1__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.mem = [0 for _ in range(size)]
        self.size = size
        self.nData = 0
        self.ptr = -1
        self.sum = 0

    def next1(self, val):
        """
        :type val: int
        :rtype: float
        """
        if self.nData < self.size:
            self.ptr += 1
            self.mem[self.ptr] = val
            self.nData += 1
            self.sum = self.sum + val
            return self.sum/float(self.nData)
        else:
            # treat memory as circular buffer
            self.ptr = (self.ptr+1) % self.size
            nDelete = self.mem[self.ptr]
            self.mem[self.ptr] = val
            self.sum += (val-nDelete)
            return self.sum/float(self.size)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

if __name__ == '__main__':
    testVector = [1,2,3,4,5,6,7,8]
    a = MovingAverage(4)
    print("Compute moving average from a data stream...")
    for test in testVector:
        print('Moving average is',a.next(test))