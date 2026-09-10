# -*- coding: utf-8 -*-
"""
Created on May 21, 2017
LeetCode problem 475
Winter is coming! Your first job during the contest is to design a standard
heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find
out minimum radius of heaters so that all houses could be covered by those
heaters.

So, your input will be the positions of houses and heaters seperately, and
your expected output will be the minimum radius standard of heaters.

Note:
1. Numbers of houses and heaters you are given are non-negative and will not
exceed 25000.
2. Positions of houses and heaters you are given are non-negative and will
not exceed 10^9.
3. As long as a house is in the heaters' warm radius range, it can be warmed.
4. All the heaters follow your radius standard and the warm radius are the same.
Example 1:
Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the
radius 1 standard, then all the houses can be warmed.
Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to
use radius 1 standard, then all the houses can be warmed.
@author: K Li
"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        Sort both house and heaters array first, then seqentially found
        minDist for house
        """

        N, M = len(houses), len(heaters)
        if (N==0) | (M==0):
            return 0
        houses.sort()
        heaters.sort()
        ind = 0
        minDist = 0
        for h in houses:
            while (ind<M-1):
                if (heaters[ind]+heaters[ind+1] > 2*h):
                    break
                else:
                    ind += 1
            minDist = max(minDist, abs(h-heaters[ind]))
        return minDist
    
    def findRadius2(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        Sort heaters array first, then use binary search to directly compute
        minimal distance for each houses. Find maximum of minimum.
        Write inline code to improve performance
        """

        N, M = len(houses), len(heaters)
        if (N==0) | (M==0):
            return 0
        #houses.sort()
        heaters.sort()
        radius = 0
        for h in houses:
            left, right = 0, M-1
            while left<right:
                mid = (left+right)//2
                if h == heaters[mid]:
                    left, right = mid, mid
                elif h < heaters[mid]:
                    right = mid
                else:
                    left = mid+1
            # stop condition, left == right
            # left could be left-1
            left = max(left-1, 0)
            curR = min(abs(h-heaters[left]), abs(h-heaters[right]))
            radius = radius if radius > curR else curR
        return radius
    
    def findRadius1(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        Sort heaters array first, then use binary search to find match or
        neightbor indices for each house.
        Find maximum of minimal radius for each house.
        The code is a little cluttered.
        """
        def binarySearch(val, nums):
            """
            binary search val on a sorted array nums
            Found, return index
            Not found, return left, right indices.
            If less than nums[0], return [0,0]
            If greater than nums[N-1], return [N-1,N-1]
            """
            N = len(nums)
            if N==0:
                return None
            left, right = 0, N-1
            while left<right:
                mid = (left+right)//2
                if val == nums[mid]:
                    return (mid, mid)
                elif val < nums[mid]:
                    right = mid
                else:
                    left = mid+1
            if (nums[left] > val):
                left = max(left-1,0)
            #if (nums[left] <= val):
            return (left, right)

        N, M = len(houses), len(heaters)
        if (N==0) | (M==0):
            return 0
        #houses.sort()
        heaters.sort()
        radius = 0
        for h in houses:
            l,r = binarySearch(h, heaters)
            radius = max(radius, min(abs(heaters[r]-h), abs(h-heaters[l])))
        return radius
                
if __name__ == '__main__':
    a = Solution()
    testVector = [([],[1,2,3]),([1,2,3],[1,2,3]),([1,2,3,4,5],[1,10]),
                  ([1,3,2],[2]),([1,2,3,4],[1,4]),
                  ([1,2,3,4,5],[2,3]),([10,1,2,3,4],[2,3])]
    a = Solution()
    for test in testVector:
        print(test)
        print("Minimal radius is ", a.findRadius(test[0],test[1]))
        print("Minimal radius is ", a.findRadius2(test[0],test[1]))
