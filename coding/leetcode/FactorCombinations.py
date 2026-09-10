# -*- coding: utf-8 -*-
"""
Created on June 1st, 2017
LeetCode problem 254
Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible
combinations of its factors.

Note: 
You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Examples: 
input: 1
output: 
[]
input: 37
output: 
[]
input: 12
output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
input: 32
output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
@author: K Li
"""

class Solution(object):
    def getFactors(self, num):
        """
        :type n: int
        :rtype: List[List[int]]
        One steps iterative approach
        Code is more compact but less understandable
        1. compute factor and creating factor combination at the same time.
        """
        
        # get combinations
        path, self.comb = [], []
        #factComb(num, 2, path)
        stack = [(num, 2, path)]

        """Find factor, and create combination"""
        while stack:
            num, factor, path = stack.pop()
            while (factor*factor) <= num:
                if (num%factor) == 0:
                    self.comb.append(path+[factor, num//factor])
                    stack.append((num//factor,factor, path+[factor]))
                factor += 1

        return self.comb
    
    def getFactorsR(self, num):
        """
        :type n: int
        :rtype: List[List[int]]
        One steps recursive solution.
        Code is more compact but less understandable
        1. compute factor and creating factor combination at the same time.
        """
        def factComb(num, factor, path):
            """Find factor, and"""
            while (factor*factor) <= num:
                if (num%factor) == 0:
                    self.comb.append(path+[factor, num//factor])
                    factComb(num//factor,factor, path+[factor])
                factor += 1
            return
        
        # get combinations
        path, self.comb = [], []
        factComb(num, 2, path)
            
        return self.comb
    
    def getFactors1(self, num):
        """
        :type n: int
        :rtype: List[List[int]]
        Two steps recursive solution
        1. get all factors from num
        2. generate factor combinations from the factor list recursively
        """
        def dfs(start, prod, num, path):
            """Use DFS to search for all possible factor combinations"""
            for n in range(start, self.N):
                factor = self.factors[n]
                new = prod * factor
                if (new)==num:
                    path.append(factor)
                    self.comb.append(path)
                elif (new)<num:
                    dfs(n, new, num, path+[factor])
            return
        
        # get factors
        self.factors = []
        for i in range(2, int(num**0.5)+1):
            if (num%i) == 0:
                if i!= num//i:
                    self.factors.extend([i, num//i])
                else:
                    self.factors.append(i)
        self.factors.sort()
        self.N = len(self.factors)

        # get combinations
        self.comb = []
        path = []
        dfs(0, 1, num, path)
            
        return self.comb
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [1,4,6,8,17,28,32]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        #print('Test case %d-----------'%i)
        print(test)
        print("Factor combinations\n",a.getFactors(test))
        

