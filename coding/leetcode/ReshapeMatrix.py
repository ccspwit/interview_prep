# -*- coding: utf-8 -*-
"""
Created on May 26, 2017
LeetCode problem 566
You're given a matrix represented by a two-dimensional array, and two positive
integers r and c representing the row number and column number of the wanted
reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original
matrix in the same row-traversing order as they were. If the 'reshape'
operation with given parameters is possible and legal, output the new
reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4
matrix, fill it row by row by using the previous list.

Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the
original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.

@author: K Li
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        N = len(nums)
        if N==0:
            raise ValueError("Input array can not be empty.")
        M = len(nums[0])
        if M==0:
            raise ValueError("Elements of input array can not be empty.")
        if (N*M)!=r*c:
            return nums
        if N==r:
            return nums
        # Warning !!!
        # the following statement is problematic, use list comprehension instead
        # result = [[0]*c]*r
        result = [[0 for i in range(c)] for j in range(r)]
        for rind in range(r):
            for cind in range(c):
                fullInd = (rind*c)+cind
                r0 = fullInd//M
                c0 = fullInd%M
                #print(rind,cind, r0,c0)
                result[rind][cind] = nums[r0][c0]
        return result

    def matrixReshape1(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        N = len(nums)
        if N==0:
            raise ValueError("Input array can not be empty.")
        M = len(nums[0])
        if M==0:
            raise ValueError("Elements of input array can not be empty.")
        if (N*M)!=r*c:
            return nums
        if N==r:
            return nums
        #print(N,M,r,c)
        result = []
        for rind in range(r):
            rowVec = []
            for cind in range(c):
                fullInd = (rind*c)+cind
                r0 = fullInd//M
                c0 = fullInd%M
                #print(fullInd, r0,c0)
                rowVec.append(nums[r0][c0])
            result.append(rowVec)
        return result
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [([[1,2,3,4,5,6,7,8]],(2,4)),
                  ([[1,2,3,4,5,6,7,8]],(1,8)),
                  ([[1,2,3,4,5,6,7,8]],(8,1)),
                  ([[1,2],[3,4]],(2,2)),
                  ([[1,2],[3,4]],(1,4))]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        nums = test[0]
        r, c = test[1]
        print('Reshaped maetrix: ',a.matrixReshape(nums, r, c))
        print('Reshaped maetrix: ',a.matrixReshape1(nums, r, c))

    t = list(range(1,1000))
    t[100] = 999