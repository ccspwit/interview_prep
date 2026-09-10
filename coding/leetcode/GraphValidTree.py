# -*- coding: utf-8 -*-
"""
Created on Thu June 9, 2017
LeetCode problem 261
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
edge is a pair of nodes), write a function to check whether these edges make
up a valid tree.

For example:
Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note: you can assume that no duplicate edges will appear in edges. Since all
edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear
together in edges.
@author: K Li
"""

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([[0,1],[0,2],[0,3],[1,4]],5),
                  ([[0,1],[1,2],[2,3],[1,3],[1,4]],5)]
    a = Solution()
    #testVector = [[10,3,4,11,12,13]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)

        print(a.validTree(test[1],test[0]))
