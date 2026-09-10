# -*- coding: utf-8 -*-
"""
Created on May 26, 2017
LeetCode problem 370, 598 combined
---#370
Assume you have an array of length n initialized with all 0's and are given
k update operations. Each operation is represented as a triplet,
[startIndex, endIndex, inc] which increments each element of subarray
A[startIndex ... endIndex] (startIndex and endIndex inclusive) with inc.

Return the modified array after all k operations were executed.

Example:
Given:
    length = 5,
    updates = [
        [1,  3,  2],
        [2,  4,  3],
        [0,  2, -2]    ]
Output:
    [-2, 0, 3, 5, 3]
Explanation:

Initial state:
[ 0, 0, 0, 0, 0 ]
After applying operation [1, 3, 2]:
[ 0, 2, 2, 2, 0 ]
After applying operation [2, 4, 3]:
[ 0, 2, 5, 5, 3 ]
After applying operation [0, 2, -2]:
[-2, 0, 3, 5, 3 ]

---#598
Given an m * n matrix M initialized with all 0's and several update operations.
Operations are represented by a 2D array, and each operation is represented
by an array with two positive integers a and b, which means M[i][j] should be
added by one for all 0 <= i < a and 0 <= j < b.

You need to count and return the number of maximum integers in the matrix
after performing all the operations.

Example 1:
Input: 
m = 3, n = 3
operations = [[2,2],[3,3]]
Output: 4
Explanation: 
Initially, M = 
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]

After performing [2,2], M = 
[[1, 1, 0],
 [1, 1, 0],
 [0, 0, 0]]

After performing [3,3], M = 
[[2, 2, 1],
 [2, 2, 1],
 [1, 1, 1]]

So the maximum integer in M is 2, and there are four of it in M. So return 4.
Note:
The range of m and n is [1,40000].
The range of a is [1,m], and the range of b is [1,n].
The range of operations size won't exceed 10,000.
@author: K Li
"""

class Solution(object):
    def getModifiedArray(self, length, updates):
        """
        :type length: int
        :type updates: List[List[int]]
        :rtype: List[int]
        """
        result = [0 for i in range(length)]
        for upd in updates:
            st, end, inc = upd[0], upd[1], upd[2]
            result[st] += inc
            if end<length-1:
                result[end+1] -=inc
        for n in range(1,length):
            result[n] += result[n-1]
        return result
    
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops)==0:
            return m*n
        a,b = zip(*ops)
        return min(a)*min(b)

    def maxCount1(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        minA, minB = m, n
        #lenOps = len(ops)
        for a,b in ops:
            minA = min(minA, a)
            minB = min(minB, b)
        return minA*minB
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    a = Solution()
    testVector = [(3,[]),(3,[[1,2,1]]),   # problem here?
                  (5,[[1,3,2],[2,4,3],[0,2,-2]]),
                  (5,[[2,2,1],[3,3,-1],[1,2,2]])]
    print('Range addition I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        l, updates = test[0], test[1]
        print('Array after updates',a.getModifiedArray(l, updates))
        #print('Count of maximum values',a.maxCount1(m,n,ops))

    testVector = [(3,3,[]),(3,3,[[0,0]]),   # problem here?
                  (4,5,[[1,2],[3,4],[2,2],[3,3]]),
                  (5,5,[[2,2],[3,3],[1,2]])]
    print('\nRange addition II')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        m, n, ops = test[0], test[1], test[2]
        print('Count of maximum values',a.maxCount(m,n,ops))
        print('Count of maximum values',a.maxCount1(m,n,ops))

    t = list(range(1,1000))
    t[100] = 999