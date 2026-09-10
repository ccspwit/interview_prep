# -*- coding: utf-8 -*-
"""
Created on June 7, 2017
LeetCode problem 77
Given two integers n and k, return all possible combinations of k numbers
out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[ [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],]

@author: K Li
"""

class Solution(object):
    """def combine(self, n, k):
        ans = []
        stack = []
        x = 1
        while True:
            l = len(stack)
            if l == k:
                ans.append(stack[:])
            if l == k or x > n - k + l + 1:
                if not stack:
                    return ans
                x = stack.pop() + 1
            else:
                stack.append(x)
                x += 1
    """
    
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Iterative solution, in descenting order, 245ms beat 60%
        """
        result = []
        comb = []
        stack = [(n,k,comb)]
        while stack:
            n, k, comb = stack.pop()
            if k==0:
                result.append(comb)
                continue
            M = len(comb)
            for v in range(n, k-1, -1):
                if M == 0:
                    stack.append((n-1, k-1,comb+[v]))
                else:
                    if v <comb[-1]:
                        stack.append((n-1, k-1,comb+[v]))

        return result

    def combineR(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Recursive solution, in descenting order, 278ms beat 40%
        """
        def combineDown(n, k, comb):
            if k==0:
                self.result.append(comb)
                return
            M = len(comb)
            for v in range(n, k-1, -1):
                if M == 0:
                    combineDown(n-1, k-1,comb+[v])
                else:
                    if v <comb[-1]:
                        combineDown(n-1, k-1,comb+[v])
            return
        
        self.result = []
        combineDown(n,k,[])
        return self.result
    
    def combineR1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Recursive solution, in ascending order, TLE for (20,16)
        """
        def combineUp(start, n, k, comb):
            if k==0:
                self.result.append(comb)
                return
            M = len(comb)
            for v in range(start, n+1):
                if M == 0:
                    combineUp(start+1, n, k-1,comb+[v])
                else:
                    if v > comb[-1]:
                        combineUp(start+1, n, k-1, comb+[v])
            return
        
        self.result = []
        combineUp(1, n, k, [])
        return self.result

    def combineDESC(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Iterative solution, in descenting order, TLE for (20,16)
        """
        result = [[]]
        for i in range(k):
            temp = []
            for j in range(n-i, 0, -1):
                M = len(result)
                #print(i, n, M , result)
                for m in range(M):
                    if M==1:
                        temp.append(result[m]+[j])
                    else:
                        if j < result[m][-1]:
                            temp.append(result[m]+[j])
            result = temp
        return result

    def combineASC(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        Iterative solution, in ascending order, TLE for (20,16)
        """
        result = [[]]
        for i in range(k):
            temp = []
            for j in range(1+i,n+1):
                M = len(result)
                for m in range(M):
                    if M==1:
                        temp.append(result[m]+[j])
                    else:
                        if j> result[m][-1]:
                            temp.append(result[m]+[j])
            result = temp
        return result
        

if __name__ == '__main__':
    a = Solution()
    testVector = [(1,1),(4,2),(4,3)]#,(6,3)]
    a = Solution()
    #testVector=[(10,11)]
    for test in testVector:
        print(test)
        x = a.combine(test[0],test[1])
        print("Combination number", len(x))
        print(x)
        #print(a.combineDESC(test[0],test[1]))
    
    #test = np.random.randint(0,20,20)