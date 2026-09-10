# -*- coding: utf-8 -*-
"""
Created on May 26, 2017
LeetCode problem 594
Given the coordinates of four points in 2D space, return whether the four
points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two
integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal
angles (90-degree angles).
Input points have no order.
@author: K Li
"""

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        def dist2(p,q):
            return (p[0]-q[0])**2+(p[1]-q[1])**2

        D = []
        points = [p1, p2, p3, p4]
        N = 4
        for i in range(4):
            for j in range(i+1, 4):
                D.append(dist2(points[i], points[j]))
        D.sort()
        if D[0]==0:
            return False
        return (D[0]==D[3]) and (D[4]==D[5]) and (D[4]==D[0]*2)
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[[0,0],[0,0],[0,0],[0,0]],
                  [[1,2],[3,4],[2,2],[3,3]],
                  [[0,0],[1,1],[1,0],[0,1]]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        p1, p2, p3, p4 = test[0], test[1], test[2], test[3]
        print('Is a valid square? ',a.validSquare(p1,p2,p3,p4))
        #print('Reshaped maetrix: ',a.matrixReshape1(nums, r, c))

    t = list(range(1,1000))
    t[100] = 999