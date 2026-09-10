# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 39, 40, 216 combined
---#39
Given a set of candidate numbers (C) (without duplicates) and a target number
(T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[ [7],
  [2, 2, 3]]

---#40
Given a collection of candidate numbers (C) and a target number (T), find
all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[ [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]]

---#216
Find all possible combinations of k numbers that add up to a number n, given
that only numbers from 1 to 9 can be used and each combination should be a
unique set of numbers.
Example 1:
Input: k = 3, n = 7
Output:
[[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output:
[[1,2,6], [1,3,5], [2,3,4]]
@author: K Li
"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs(nums, target, path):
            """
            """
            N = len(nums)
            if N==0:
                return
            '''if N==1:
                if nums[0]==target:
                    self.result.append(path+nums)
                else:
                    return'''
            while nums:
                val = nums[-1]
                if val > target:
                    nums.pop()
                elif val == target:
                    self.result.append(path+[nums[-1]])
                    nums.pop()
                else:
                    dfs(nums[:], target-val, path+[val])
                    nums.pop()
            return
        
        self.result = []
        N = len(candidates)
        if N==0:
            return []
        if 0 in candidates:
            return []
        candidates.sort()
        
        dfs(candidates[:], target, [])
        return self.result

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def dfs2(start, target, path):
            if start>=len(candidates):
                return
            for n in range(start,N):
                val = candidates[n]
                if (n>start)&(val==candidates[n-1]):
                    continue
                if val == target:
                    self.ans.append(path+[val])
                elif val < target:
                    dfs2(n+1, target-val, path+[val])                
            return
        
        N = len(candidates)
        if N==0:
            return []
        self.ans=[]
        candidates.sort()
        dfs2(0, target, [])
        return self.ans

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        Optimized, use num as the biggest number left
        Do not use a list
        """
        def dfs3(_num, depth, target, path):
            if (depth==0):
                if (target==0):
                    self.ret.append(path)
                    return
                if target<0:
                    return
                
            while _num>0:
                if _num > target:
                    _num -= 1
                else:
                    dfs3(_num-1, depth-1, target-_num, path+[_num])
                    _num -= 1
            return

        if (k>9) and (k<=0):
            return []
        self.ret = []
        dfs3(9, k, n, [])
        return self.ret
        
if __name__ == '__main__':
    a = Solution()
    testVector = [([],1),([1,2],2),
                  ([2,3,6,7,8,9,10,11],7),
                  ([1,2,3,4,5,6],6),
                  ([1,-1,0,1,-1,0,1,-1,0],0)]
    print("\nCombination sum I")
    for test in testVector:
        print(test)
        test1 = test[:]
        print("Combination sum ", a.combinationSum(test[0], test[1]))
        
    testVector = [([],1),([2],2),([1,1,1,2],3),
                  ([1,1,2,3,4,5,6],6)]
    print("\nCombination sum II")
    for test in testVector:
        print(test)
        test1 = test[:]
        print("Combination sum ", a.combinationSum2(test[0], test[1]))

    testVector = [(0,1),(1,0),(3,10)]
                  #([1,-1,0,1,-1,0,1,-1,0],0)]
                  #([1,2,3,3,3,4],3),([5,7,7,8,8,10],8)]
    print("\nCombination sum III")
    for test in testVector:
        print(test)
        test1 = test[:]
        print("Combination sum ", a.combinationSum3(test[0], test[1]))

