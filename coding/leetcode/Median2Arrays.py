# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 2017
LeetCode problem 4
Two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
Further performance tuning is needed

nums1 = [1, 3]
nums2 = [2]
The median is 2.0

nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5
@author: K Li
"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N1, N2 = len(nums1), len(nums2)
        #print('N1=%d, N2=%d' %(N1,N2))

        N = N1+N2
        nHalf = (N-1)//2    # or (N-1)>>1
        nLow, nHigh = 0,0

        lowInd1, lowInd2 = 0,0
        highInd1, highInd2 = N1,N2
        
        numLeft1, numLeft2 = highInd1-lowInd1, highInd2-lowInd2
        delta = (min(nHalf-nLow, numLeft1, numLeft2)+1)//2
        #print(nLow, nHigh, nHalf, delta)
        
        # loop over array while delta is not 0, and number of lower half
        # (or higher hlaf) is less than nHalf
        #while((nHigh<nHalf) & (delta!=0)):
        while (delta!=0):
            #print('delta = ',delta)
            # Compute new indices for
            # nums1 high/low threshold
            # nums2 high/low threshold
            h1 = highInd1 -delta
            l1 = lowInd1 + delta-1
            h2 = highInd2 -delta
            l2 = lowInd2 + delta-1
            #print(l1,h1,l2,h2)
            if(nums1[h1]>nums2[h2]):
                # higher part of nums1 is the largerest, update highInd1
                highInd1 = h1
                numLeft1 -= delta
            else:
                # higher part of nums2 is the largest, update highInd2
                highInd2 = h2
                numLeft2 -= delta
            
            if(nums1[l1]<nums2[l2]):
                # lower part of nums1 is the smallest, update lowInd1
                lowInd1 = l1+1
                numLeft1 -= delta
            else:
                # lower part of nums2 is the smallest, update lowInd2
                lowInd2 = l2+1
                numLeft2 -= delta

            nHigh += delta
            nLow += delta
            delta = (min(nHalf-nLow, numLeft1, numLeft2)+1)//2
            #print('nLow, nHigh, delta',nLow, nHigh, delta)

        # print (lowInd1, highInd1, lowInd2, highInd2)
        if(lowInd1 == highInd1):
            # Median falls in nums2 array
            ind1 = (highInd2+lowInd2)//2
            ind2 = (highInd2+lowInd2-1)//2
            medianValue = (nums2[ind1]+nums2[ind2])/2.0
        elif(lowInd2 == highInd2):
            # Median falls in nums1 array
            ind1 = (highInd1+lowInd1)//2
            ind2 = (highInd1+lowInd1-1)//2
            medianValue = (nums1[ind1]+nums1[ind2])/2.0
        else:
            # High threshold and low threshold are the same for both arrays
            # Median will be average of threshold
            medianValue = (nums1[lowInd1]+nums2[lowInd2])/2.0
        return medianValue

    def testMedian(self, nums1, nums2):
        import numpy as np
        return np.median(nums1+nums2)

if __name__ == '__main__':
    a = Solution()
    testVector = [([1],[2]),
                  ([1,3],[2,4]),
                  ([1,2],[3]),
                  ([2,3],[1]),
                  ([3],[1,2]),
                  ([2],[1,3]),
                  ([1,2],[3,4]),
                  ([1,4],[2,3])]
    for test in testVector:
        print(a.testMedian(test[0],test[1]) - a.findMedianSortedArrays(test[0],test[1]))
    
    testVector = [(list(range(1,10,2)), list(range(0,13,2))),
                  (list(range(1,10,2)), list(range(0,15,2))),
                  (list(range(1,10,2))+[100], list(range(0,13,2))),
                  (list(range(1,10,2))+[100], list(range(0,15,2))),
                  (list(range(1,10,2)), list(range(10,15,2))),
                  (list(range(1,10,2)), list(range(10,25,2)))]
    for test in testVector:
      print(a.testMedian(test[0],test[1]) - a.findMedianSortedArrays(test[0],test[1]))
  
    testVector = [([],[1,2,3,4,5]),
                  ([1,2],[3,4,5,6,7,8,9]),
                  ([8,9],[0,1,2,3,4,5,6,7]),
                  ([1,10],[2,3,4,5,6,7,8,9]),
                  ([1,10],[2,3,4,5,6,7,8,10]),
                  ([4,5],[1,2,3,6,7,8,9]),
                  ([4,5],[1,2,3,4,5,6,7,8,9])]
    for test in testVector:
      print(a.testMedian(test[0],test[1]) - a.findMedianSortedArrays(test[0],test[1]))
  