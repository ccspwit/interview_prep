# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 547
There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct
friend of B, and B is a direct friend of C, then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct or
indirect friends.

Given a N*N matrix M representing the friend relationship between students in
the class. If M[i][j] = 1, then the ith and jth students are direct friends
with each other, otherwise not. And you have to output the total number of
friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a
friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd
students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the
same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
@author: K Li
"""

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        beat 99% python submissions
        """
        N = len(M)
        if N==0:
            raise ValueError("Matrix can not be empty.")
        # column that are not checked
        unchecked = list(range(N))
        count = 0
        while unchecked:
            checkRow = [unchecked.pop(0)]
            count += 1
            while checkRow:
                row = checkRow.pop()
                checkCol = unchecked[:]
                for col in checkCol:
                    if M[row][col]==1:
                        unchecked.remove(col)
                        checkRow.append(col)
        return count

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [[[1]],[[0]],[[1,0,0],[0,1,0],[0,0,1]],
                  [[1,1,0],[1,1,0],[0,0,1]],
                  [[1,1,0],[1,1,1],[0,1,1]]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Least number of bricks to cross ',a.findCircleNum(test))
        #print('Reshaped maetrix: ',a.matrixReshape1(nums, r, c))

    t = list(range(1,1000))
    t[100] = 999