# -*- coding: utf-8 -*-
"""
Created on Sun May 14, 2017
LeetCode problem 249， 250 combined
---#249
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.

---#245
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2, 2].

Note:
Each element in the result should appear as many times as it shows in both
arrays. The result can be in any order.
Follow up:
What if the given array is sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited
such that you cannot load all elements into the memory at once?
@author: K Li
"""

class Solution(object):
    def intersect1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Sort + 2 pointers solution
        """
        N1, N2 = len(nums1), len(nums2)
        if min(N1, N2)<=0:
            return []
        result = []
        if N1 > N2:
            nums1, nums2 = nums2, nums1
            N1, N2 = N2, N1

        nums1.sort()
        nums2.sort()

        p1, p2 = 0, 0
        while (p1<N1) & (p2<N2):
            n1,n2 = nums1[p1], nums2[p2]
            if n1 == n2:
                result.append(nums1[p1])
                p1 += 1
                p2 += 1
                #print(n, p2)
            elif n1 < n2:
                p1 += 1
            else:
                p2 += 1
                
        return result

    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Use dictionary to keep counter of an element
        """
        N1, N2 = len(nums1), len(nums2)
        if min(N1, N2)<=0:
            return []

        result = []
        if N1 > N2:
            nums1, nums2 = nums2, nums1
            N1, N2 = N2, N1

        counter1 = {}
        for i in nums1:
            counter1[i] = counter1.get(i,0)+1
            
        for i in nums2:
            if i in counter1 and counter1[i]>0:
                result.append(i)
                counter1[i] -= 1
        return result
        
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Set &
        """
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1&s2)

    def intersection1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        Set intersection
        """
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([],[1,2,3]),([1,2],[1,1]),([1],[2,3]),
                  ([1,1,3,3],[2,2,4,4]),([2,2],[1,2,1,2,3]),
                  ([3,4,2,2,2],[1,2,3,4,5,2]),
                  ([1,2,3,4,5,2],[3,4,2,2,2])]
    a = Solution()
    for test in testVector:
        print(test)
        print("Intersection part is: ", a.intersect(test[0],test[1]))
        print("Intersection part is: ", a.intersect1(test[0],test[1]))
        #print("Intersection part is: ", a.intersection(test[0],test[1]))
