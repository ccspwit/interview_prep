# -*- coding: utf-8 -*-
"""
Created on Mon May 8, 2017
LeetCode problem 339, 364 combined
---#339
Given a nested list, calculate sum of number weighted by depth.
For example, [[1,1],2,[1,1]] --- 10
[1,[4,[6]]] --- 27

---#364
Given a nested list of integers, return the sum of all integers in the list
weighted by their depth. Each element is either an integer, or a list whose
elements may also be integers or other lists.

Different from the previous question where weight is increasing from root to
leaf, now the weight is defined from bottom up. i.e., the leaf level integers
have weight 1, and the root level integers have the largest weight.

Example 1:
List [[1,1],2,[1,1]], return 8. (four 1's at depth 1, one 2 at depth 2)

Example 2:
List [1,[4,[6]]], return 17. (one 1 at depth 3, one 4 at depth 2, and one 6
 at depth 1; 1*3 + 4*2 + 6*1 = 17) 
@author: K Li
"""

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger(object):
    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather
        than a nested list.
        :rtype bool
        """

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds
        a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds
        a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """

class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        More efficient solution
        """
        total_sum, level_sum = 0, 0
        while len(nestedList):
            next_level_list = []
            for x in nestedList:
                if x.isInteger():
                    level_sum += x.getInteger()
                else:
                    for y in x.getList():
                        next_level_list.append(y)
            total_sum += level_sum
            nestedList = next_level_list
        return total_sum
    
    def depthSumInverse2(self, nums):
        """
        :type nums: Nested List[int]
        :rtype: Int
        call sum function with weight
        """
        def sumWithDepthInverse(nums, depth, resultList):
            # compute forward and backward cumulative product
            N = len(nums)
            if nums == 0:
                return
            numSum, curListSum = 0, 0
            for ele in nums:
                if isinstance(ele, list):
                    sumWithDepthInverse(ele, depth+1, resultList)
                else:
                    numSum += ele
            resultList.append((numSum, depth))
            return
        
        cache = []
        sumWithDepthInverse(nums, 1, cache)
        maxDepth = max(cache, key=lambda x:x[1])[1]
        result = sum(map(lambda x:x[0]*(maxDepth-x[1]+1), cache))
        return result

    def depthSumInverse1(self, nums):
        """
        :type nums: Nested List[int]
        :rtype: Int
        call sum function with weight
        Use nestedList class implementation which I did not implement.
        Just for reference
        """
        def sumWithDepthInverse(nums, depth, resultList):
            # compute forward and backward cumulative product
            N = len(nums)
            if nums == 0:
                return
            numSum, curListSum = 0, 0
            for ele in nums:
                if not ele.isInteger():
                    sumWithDepthInverse(ele.getList(), depth+1, resultList)
                else:
                    numSum += ele.getInteger()
            resultList.append((numSum, depth))
            return
        
        cache = []
        sumWithDepthInverse(nums, 1, cache)
        maxDepth = max(cache, key=lambda x:x[1])[1]
        result = sum(map(lambda x:x[0]*(maxDepth-x[1]+1), cache))
        return result
    
    def depthSum(self, nums):
        """
        :type nums: Nested List[int]
        :rtype: Int
        call sum function with weight
        """
        
        def sumWithDepthWeight(nums, weight):
            # compute forward and backward cumulative product
            N = len(nums)
            if nums == 0:
                return 0
            result = 0
            for ele in nums:
                if isinstance(ele, list):
                    result += sumWithDepthWeight(ele, weight+1)
                else:
                    result += ele*weight
            return result
        
        return sumWithDepthWeight(nums, 1)
 
    def depthSum1(self, nums):
        """
        :type nums: Nested List[int]
        :rtype: Int
        call sum function with weight
        Use nestedList class implementation which I did not implement.
        Just for reference
        """
        
        def sumWithDepthWeight(nums, weight):
            # compute forward and backward cumulative product
            N = len(nums)
            if nums == 0:
                return 0
            result = 0
            for ele in nums:
                if ele.isInteger():
                    result += ele.getInteger()*weight
                else:
                    result += sumWithDepthWeight(ele.getList(), weight+1)
            return result
        
        return sumWithDepthWeight(nums, 1)

    def depthSum2(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        Use nestedList class implementation which I did not implement.
        Just for reference
        """
        depth, ret = 1, 0
        while nestedList:
            ret += depth * sum([x.getInteger() for x in nestedList if x.isInteger()])
            nestedList = sum([x.getList() for x in nestedList if not x.isInteger()], [])
            depth += 1
        return ret    
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[[1,1],2,[1,1]],
                  [1,[4,[6]]],
                  [1,2,0,0,5,6],
                  [1,[4,[10,[2]],[3]],5]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = a.depthSum(test)
        print(x)
        y = a.depthSumInverse(test)
        print(y)
    #test = sorted(random.randint(0,100,100))
