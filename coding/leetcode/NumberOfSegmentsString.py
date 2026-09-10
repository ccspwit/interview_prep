# -*- coding: utf-8 -*-
"""
Created on Sun May 18, 2017
LeetCode problem 434
Count the number of segments in a string, where a segment is defined to be
a contiguous sequence of non-space characters.

Please note that the string does not contain any non-printable characters.

Example:
Input: "Hello, my name is John"
Output: 5
@author: K Li
"""

class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        if N==0:
            return 0
        nSeg = 0
        wsFlag = 1
        whiteSpace={" ", "\t", "\n", "\r"}
        for ch in s:
            if (ch not in whiteSpace) & wsFlag:
                nSeg += 1
                wsFlag = 0
            elif (ch in whiteSpace):
                wsFlag = 1
        return nSeg

    def countSegments1(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())
    
if __name__ == '__main__':
    a = Solution()
    testVector = ["", "a", " \t \r\n","a b c", " ab c ",
                  "Hello, my name is John","kemin\tLi\n:"]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print(a.countSegments(test))
        print(a.countSegments1(test))
