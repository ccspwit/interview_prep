# -*- coding: utf-8 -*-
"""
Created on May 14th, 2017
LeetCode problem 46, 47 combined
---#46
Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[ [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]]

---#47
Given a collection of numbers that might contain duplicates, return all
possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[  [1,1,2],
  [1,2,1],
  [2,1,1]]
@author: K Li
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Iterative solution that add elements one by one. Later elements can
        be added to position 0--i, check for duplicate element
        Be careful with the handling of the list
        """
        N = len(nums)
        if N<=1:
            return [nums]
        result = [[]]
        
        for n in nums:
            temp = []  # hold intermediate result
            for prev in result:
                M = len(prev)
                for k in range(M+1):
                    temp.append(prev[:k]+[n]+prev[k:])
                    if(k<M) and (prev[k]==n):
                        break
            result = temp
        return result
    
    def permuteUniqueR(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Recursive solution: pick a unique element from the list, and pass
        the remain list (with the pick removed) recursively until only
        one element left in the list
        Be careful with the handling of the list
        """
        def permuteListUnique(nums, combination, retList):
            """
            """
            if len(nums)==1:
                combination.append(nums[0])
                retList.append(combination)
            else:
                uniqueSet = set()
                for n in range(len(nums)):
                    ni = nums[n]
                    if ni not in uniqueSet:
                        uniqueSet.add(ni)
                        remain = nums[:n]+nums[n+1:]
                        newcomb = combination+[ni]
                        permuteListUnique(remain, newcomb, retList)
                    else:
                        continue
            return
    
        N = len(nums)
        if N<=1:
            return [nums]
        result = []
        
        uniqueSet = set()
        for n in range(N):
            ni = nums[n]
            if ni not in uniqueSet:
                uniqueSet.add(ni)
                remain = nums[:n]+nums[n+1:]
                permuteListUnique(remain, [ni], result)
            else:
                continue
        return result
        
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Iterative solution that add elements one by one. Later elements can
        be added to position 0--i
        Be careful with the handling of the list
        """
        N = len(nums)
        if N<=1:
            return [nums]
        result = [[]]
        
        for n in nums:
            temp = []  # hold intermediate result
            for prev in result:
                M = len(prev)
                for k in range(M+1):
                    temp.append(prev[:k]+[n]+prev[k:])
            #print(temp)
            result = temp
        return result

    def permuteR(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Recursive solution: pick an element from the list, and pass
        the remain list (with the pick removed) recursively until only
        one element left in the list
        Be careful with the handling of the list
        """
        def permuteList(nums, combination, retList):
            """
            """
            if len(nums)==1:
                combination.append(nums[0])
                retList.append(combination)
            else:
                for n in range(len(nums)):
                    remain = nums[:]
                    ni = remain.pop(n)
                    # ni = nums[n]
                    # remain = nums[:n]+nums[n+1:]
                    newcomb = combination+[ni]
                    permuteList(remain, newcomb, retList)
            return
    
        N = len(nums)
        if N<=1:
            return [nums]
        result = []

        for n in range(N):
            remain = nums[:]
            ni = remain.pop(n)
            # ni = nums[n]
            # remain = nums[:n]+nums[n+1:]
            permuteList(remain, [ni], result)
        return result

        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,2,3],[1,1,2],
                  [1,1,2,2],[1,2,3,4]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print(a.permute(test))
        print(a.permuteUnique(test))
