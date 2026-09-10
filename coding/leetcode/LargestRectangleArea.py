# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 2017
LeetCode problem 84
Given n non-negative integers representing the histogram's bar height where
the width of each bar is 1, find the area of largest rectangle in the histogram.

Given height = [2,1,5,6,2,3].
return 10.
@author: K Li
"""

class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if(min(height)<0):
            raise ValueError("Input must be non negative.")
        N = len(height)
        if(N==0):
            raise ValueError("Length of the input must be at least 1.")
        maxVal = height[0]
        left, right = 0, N-1
        while left<right:
            if height[left]<height[right]:
                area = (right-left+1)*height[left]
                left += 1
            else:
                area = (right-left+1)*height[right]
                right -= 1
            if area > maxVal:
                maxVal = area
        
        return maxVal


if __name__ == '__main__':
    a = Solution()
    testVector = [[2,1,5,6,2,3],
                  [1,2,3,4,6],[5,4,7,3,9,2,1],
                  [9,  3, 13,  7, 17, 10,  5,  8,  9, 17],
                  [26, 35, 89,  7, 76, 11, 22, 71, 23,  8]]
    for test in testVector:
        print(test)
        print('Max area is {}'.format(a.largestRectangleArea(test)))

    test = [28,342,418,485,719,670,878,752,662,994,654,504,929,660,424,855,922,744,600,229,728,33,371,863,561,772,271,178,455,449,426,835,143,845,321,214,867,199,967,881,193,973,386,122,633,810,330,907,906,282,136,986,315,860,849,229,632,473,759,87,922,185,922,418,382,243,632,250,795,599,131,988,924,869,463,558,680,145,465,938,427,954,925,94,814,126,323,798,599,434,885,874,620,159,292,354,755,924,956,550,876,88,890,800,309,705,358,989,850,176,280,629,130,205,724,296,331,399,94,283,186,331,157,806,490,801,512,597,725,469,499,601,909,390,754,218,447,112,560,298,640,840,279,122,397,355,418,80,755,864,363,293,195,872,451,38,673,963,635,751,432,487,352,341,229,458,912,676,923,472,326,563,312,606,686,709,313,456,789,420,321,505,713,868,377,164,258,403,128,246,154,912,733,858,606,962,317,518,990,240,990,317,803,302,275,841,363,588,650,504,9,323,9,74,191,387,239,450,790,367,48,944,279,781,802,885,743,471,755,85,711,745,402,867,399,29,708,762,970,710,267,331,33,276,405,577,15,644,379,157,363,427,453,995,208,608,232,303,79,988,388,791]