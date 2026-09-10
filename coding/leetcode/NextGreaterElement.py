# -*- coding: utf-8 -*-
"""
Created on May 20, 2017
LeetCode problem 496, 503, 556 combined
---#496
You are given two arrays (without duplicates) nums1 and nums2 where nums1’s
elements are subset of nums2. Find all the next greater numbers for nums1's
elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number
to its right in nums2. If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number
    for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the
    second array is 3.
    For number 2 in the first array, there is no next greater number for it
    in the second array, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the
    second array is 3.
    For number 4 in the first array, there is no next greater number for it
    in the second array, so output -1.
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.

--#503
Given a circular array (the next element of the last element is the first
element of the array), print the Next Greater Number for every element.
The Next Greater Number of a number x is the first greater number to its
traversing-order next in the array, which means you could search circularly
to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.

---#556
Given a positive 32-bit integer n, you need to find the smallest 32-bit
integer which has exactly the same digits existing in the integer n and is
greater in value than n. If no such positive 32-bit integer exists, you need
to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1
@author: K Li
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<=0:
            raise ValueError("n must be a positive number.")
        if n<=11:
            return -1
        MAX_INT32 = 2**31
        nums = list(str(n))
        N = len(nums)

        # next permutation
        for n in range(N-2,-1,-1):
            if nums[n]<nums[n+1]:
                #find number just greater than nums[n] from the right
                m = N-1
                while nums[m]<=nums[n]:
                    m -= 1
                nums[n], nums[m] = nums[m], nums[n]
                nums[n+1:] = sorted(nums[n+1:])
                result = int("".join(nums))
                return result if result<MAX_INT32 else -1
        return -1

    def nextGreaterElement1(self, n):
        """
        :type n: int
        :rtype: int
        """
        def nextPermutation(nums):
            """
            :type nums: List[int]
            :rtype: void Do not return anything, modify nums in-place instead.
            """
            N = len(nums)
            if N<=1:
                return
    
            pseFound = False
            for n in range(N-2,-1,-1):
                if nums[n]<nums[n+1]:
                    pseFound = True
                    break
    
            if pseFound:
                left = n
                minPos, minVal = n+1, nums[n+1]
                for n in range(left+2,N):
                    if (nums[n]>nums[left])&(nums[n]<minVal):
                        minVal = nums[n]
                        minPos = n
    
                #print(left, minPos)
                nums[left], nums[minPos] = nums[minPos], nums[left]
                nums[left+1:] = sorted(nums[left+1:])

            return pseFound
        
        if n<=0:
            raise ValueError("n must be a positive number.")
        if n<=11:
            return -1
        MAX_INT32 = 2**31
        nList = list(str(n))
        # get a list nge indices
        if nextPermutation(nList):
            result = int("".join(nList))
            return result if result<MAX_INT32 else -1
        else:
            return -1

        
    def nextGreaterElements(self, nums):
        """
        This is really a concise solution
        Use index, no need for dictionary mapping
        """
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res

    def nextGreaterElements1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        Use stack to create NGE mapping.
        Return a dictionary nums[i] : its NGE
        Use a list to keep track of duplicate values           
        """
        N = len(nums)
        stack, mapping = [], {}
        
        # Traversal nums twice to find circular NGE of each elements
        # To handle duplicate, use (ind, val) as key to store NGE
        for ind, val in enumerate(nums):
            while stack and (stack[-1][1]<val):
                mapping[stack.pop()] = val
            stack.append((ind, val))
        for ind, val in enumerate(nums):
            while stack and (stack[-1][1]<val):
                mapping[stack.pop()] = val
            #stack.append((ind, val))
        while stack:
            mapping[stack.pop()] = -1
        # Output circular NGEs for each element
        result = [mapping[(ind,val)] for ind,val in enumerate(nums)]
        return result

    def nextGreaterElements2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def circularNGE(nums):
            """
            Use stack to create NGE mapping.
            Return a dictionary nums[i] : its NGE
            Use a list to keep track of duplicate values           
            """
            N = len(nums)
            stack, result = [], {}
            if (N==0):
                return result
            for n in range(N):
                while stack and (stack[-1]<nums[n]):
                    val = stack.pop()
                    if val not in result:
                        result[val] = [nums[n]]
                    else:
                        result[val].append(nums[n])
                stack.append(nums[n])

            for n in range(N):
                while stack and (stack[-1]<nums[n]):
                    val = stack.pop()
                    if val not in result:
                        result[val] = [nums[n]]
                    else:
                        result[val].append(nums[n])
            
            while stack:
                val = stack.pop()
                if val not in result:
                    result[val] = [-1]
                else:
                    result[val].append(-1)
            return result

        if len(nums)==0:
            return []
        cngeMap = circularNGE(nums)
        result = [cngeMap[e].pop(0) for e in nums]
        return result
            
    def nextGreaterElementI(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        The problem is tackled in the following steps
        1. Compute next greater element (NGE) for array nums using array
        2. Create a hashmap of nums[i] and NGE of nums[i]
        3. Output NGE of findNums
        """
        def computeNGE(nums):
            """
            Use stack to create NGE mapping.
            Return a dictionary nums[i] : its NGE
            Note elements of nums[i] need to be unique, hashmap can't handle
            duplicate values
            """
            N = len(nums)
            stack = []
            result = {}
            if (N==0):
                return result
            for n in nums:
                while stack and (stack[-1] <n):
                    result[stack.pop()] = n
                stack.append(n)
            while stack:
                result[stack.pop()] = -1
            return result

        if (len(nums)==0) | (len(findNums)==0):
            return []
        ngeMap = computeNGE(nums)

        result = findNums[:]
        for n in range(len(findNums)):
            result[n] = ngeMap[findNums[n]]

        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([],[1,2,3]),([1,2,3],[3,2,1]),
                  ([1,2,3,4], [1,2,3,4]),([4,1,2],[1,3,4,2])]
    print("-----Next greatest element I-----")
    for test in testVector:
        print(test)
        print("Next greater element is ", a.nextGreaterElementI(test[0],test[1]))
        #print("Number of content children is ", a.nextGreaterElement1(test[0],test[1]))

    testVector = [[],[1,2,3],[1,2,1],[1,2,1,3],
                  [1,1,1,1],[1,3,2,5,7,6,4,2]]
    print("-----Next greatest element II-----")
    for test in testVector:
        print(test)
        #print("Next greater element is ", a.nextGreaterElements(test))
        print("Next greater element is ", a.nextGreaterElements1(test))

    testVector = [1,11,12,21,3421,437432,1652531,2147483684,1999999999]
    print("-----Next greatest element III-----")
    for test in testVector:
        print(test)
        print("Next greater element is ", a.nextGreaterElement(test))
        print("Next greater element is ", a.nextGreaterElement1(test))