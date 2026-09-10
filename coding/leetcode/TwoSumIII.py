# -*- coding: utf-8 -*-
"""
Created on May 31, 2017
LeetCode problem 170
Design and implement a TwoSum class. It should support the following
operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
@author: K Li
"""

class TwoSum(object):
    """
    Runtime 350ms, beat 97% python submissions
    The key point is to creat hash map when adding elements.
    Other things that might be helpful
    1. for key in dict:  is quicker than
    for key, val in dict.items():
    2. make object local can make execution faster, e.g.
    count = self.valCount
    """
    def __init__(self):
        """
        Initialize your data structure here.
        Use hash tables to store added values and all possible two sums
        Val O(n) space, cache unlimited size
        """
        self.valCount = {}
        #self.cache = set()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        O(1) time
        """
        self.valCount[number] = self.valCount.get(number,0)+1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        use two sum to check existence. If find, save result in cache set.
        O(n) time, O(n) space
        """
        count = self.valCount
        for num in count:
            diff = value - num
            if (diff in count) and ((diff!=num) or (count[num]>1)):
                return True
        return False
    
class TwoSum1(object):
    """1276 ms run time"""
    def __init__(self):
        """
        Initialize your data structure here.
        Use hash tables to store added values and all possible two sums
        Val O(n) space, cache unlimited size
        """
        self.values = []
        self.cache = set()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        O(1) time
        """
        self.values.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        use two sum to check existence. If find, save result in cache set.
        O(n) time, O(n) space
        """
        if value in self.cache:
            return True
        # Two sum use hasp map
        diffs = {}
        for ind, num in enumerate(self.values):
            diffs[value-num] = ind
        for ind, num in enumerate(self.values):
            if (num in diffs) and (diffs[num]!=ind):
                self.cache.add(value)
                return True
        return False

if __name__ == "__main__":
    testVector = [([1,2,3,4,5,5],[2,6,10]),
                  ([2**n for n in range(11)],[1,5,9,101])]
    for test in testVector:
        print(test)
        a = TwoSum()
        for val in test[0]:
            a.add(val)
        
        for s in test[1]:
            print('%d is %s in two sum table'%(s,a.find(s)))
        print('values',len(a.valCount))
