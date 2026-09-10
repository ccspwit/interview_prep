# -*- coding: utf-8 -*-
"""
Created on May 28 2019
LeetCode problem 6
the string "PAYPALISHIRING" is written in a zigzag pattern on a given number of
rows like this: (you may want to display this pattern in a fixed font for
better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number
of rows:
@author: K Li
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str_len = len(s)
        arrs = [[] for n in range(numRows)]
        if numRows==1:
            return s
        if numRows==2:
            return s[::2] + s[1::2]
        # save data in 3 row array
        col = 0
        cum_count = 0
        for n in range(str_len):
            col_rem = col % (numRows-1)
            if col_rem == 0: # first col
                if (n-cum_count) < numRows:
                    arrs[n-cum_count].append(s[n])
                    if (n-cum_count) == (numRows-1):
                        cum_count += numRows
                        col += 1
            else:
                arrs[numRows-col_rem-1].append(s[n])
                cum_count += 1
                col += 1        

        # output by row
        s1 = [''.join(row) for row in arrs]
        s2 = ''.join(s1)
        
        return s2


if __name__ == 'xxx__main__':
    a = Solution()
    testVector = [("PAYPALISHIRING", 3),("PAYPALISHIRING", 4)]
    for test in testVector:
        print(a.convert(test[0],test[1]))
    
