# -*- coding: utf-8 -*-
"""
Created on Feb 20, 2020
LeetCode problem 1213
Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example 1:
Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
Output: [1,5]
Explanation: Only 1 and 5 appeared in the three arrays.

Constraints:
1 <= arr1.length, arr2.length, arr3.length <= 1000
1 <= arr1[i], arr2[i], arr3[i] <= 2000
@author: K Li
"""
class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        
        p1 = 0
        p2 = 0
        p3 = 0
        
        result = []
        
        while(p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3)):
            
            if(arr1[p1] == arr2[p2] == arr3[p3]):
                result.append(arr1[p1])
                p1, p2, p3 = p1+1, p2+1, p3+1
                continue
                
            max_of_three = max(arr1[p1], arr2[p2], arr3[p3])
            # compare with max_value, cleaner code
            if(arr1[p1] < max_of_three):
                p1 += 1
            
            if(arr2[p2] < max_of_three):
                p2 += 1
                
            if(arr3[p3] < max_of_three):
                p3 += 1
                
        return result

    def arraysIntersection1(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        N1, N2, N3 = len(arr1), len(arr2), len(arr3)
        res = []
        i1, i2, i3 = 0, 0, 0
        while i1<N1 and i2<N2 and i3<N3:
            if arr1[i1] == arr2[i2]:
                if arr2[i2] == arr3[i3]:
                    res.append(arr1[i1])
                    i1 += 1
                    i2 += 1
                    i3 += 1
                elif arr2[i2] > arr3[i3]:
                    i3 += 1
                else: # arr2[i2] < arr3[i3]
                    i1 += 1
                    i2 += 1
            elif arr1[i1] > arr2[i2]:
                if arr2[i2] == arr3[i3]:
                    i2 += 1
                    i3 += 1
                elif arr2[i2] > arr3[i3]:
                    i2 += 1
                    i3 += 1
                else: # arr2[i2] < arr3[i3]:
                    i2 += 1
                    if arr1[i1] > arr3[i3]:
                        i3 += 1
                    elif arr1[i1] < arr3[i3]:
                        i1 += 1
            else: # arr1[i1] < arr2[i2]:
                if arr2[i2] == arr3[i3]:
                    i1 += 1
                elif arr2[i2] > arr3[i3]:
                    i3 += 1
                    i1 += 1
                else: # arr2[i2] < arr3[i3]:
                    i1 += 1
                    i2 += 1
        return res
