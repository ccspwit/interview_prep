# -*- coding: utf-8 -*-
"""
Created on Thu May 4 2017
Leetcode 118, 119 combined
---#118
Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

---#119
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
Note: Could you optimize your algorithm to use only O(k) extra space?
@author: K Li
"""

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1],[1,1]]
        if (numRows<=0):
            return []
            #raise ValueError("Parameter n must be a positive integer")
        if numRows==1:
            return result[numRows-1]
        if numRows==2:
            return result[numRows-1]
        for n in range(2,numRows):
            lastRow = result[n-1]
            curRow = [1]
            for i in range(len(lastRow)-1):
                curRow.append(lastRow[i]+lastRow[i+1])
            curRow.append(1)
            result.append(curRow)

        return result

    '''def generate1(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]'''

    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        In place computation, memory use rowIndex+1
        """
        
        if (rowIndex<0):
            return []
        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]
        result = [1,1]
        for n in range(2,rowIndex+1):
            for i in range(len(result)-1,0,-1):
               result[i] = result[i]+result[i-1]
            result.append(1)

        return result

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [5]#[1,2,3,4,5]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Pascal triangle sequence is')
        print(a.generate(test))
        print(a.getRow(test))
