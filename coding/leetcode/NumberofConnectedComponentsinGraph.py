# -*- coding: utf-8 -*-
"""
Created on Thu June 9, 2017
LeetCode problem 323
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
edge is a pair of nodes), write a function to find the number of connected
components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

Note:
You can assume that no duplicate edges will appear in edges. Since all edges
are undirected, [0, 1] is the same as [1, 0] and thus will not appear together
in edges.@author: K Li
"""

class Solution(object):
    def countComponents2(self, nodes, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        Union Find solution???
        """
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(xy):
            x, y = map(find, xy)
            if rank[x] < rank[y]:
                parent[x] = y
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        parent, rank = [n for n in range(nodes)], [0 for _ in range(nodes)]
        map(union, edges)
        return len({find(x) for x in parent})

    def countComponents(self, nodes, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        BFS solution
        """
        
        connect = {x:[] for x in range(nodes)}
        for x,y in edges:
            connect[x].append(y)
            connect[y].append(x)
            
        count = 0
        for i in range(nodes):
            queue = [i]
            count += 1 if i in connect else 0
            for j in queue:
                if j in connect:
                    queue.extend(connect[j])
                    del connect[j]

        return count

    def countComponents1(self, nodes, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        DFS solution
        """
        def dfs(n, connect, visited):
            if visited[n]:
                return
            visited[n]=1
            for x in connect[n]:
                dfs(x,connect,visited)
        
        visited = [0 for n in range(nodes)]
        connect = {x:[] for x in range(nodes)}
        for x,y in edges:
            connect[x].append(y)
            connect[y].append(x)
            
        result = 0
        for i in range(nodes):
            if not visited[i]:
                dfs(i, connect, visited)
                result += 1

        return result
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [(5,[[0, 1], [1, 2], [3, 4]],),
                  (5,[[0, 1], [1, 2], [2, 3], [3, 4]])]
    a = Solution()
    #testVector = [[10,3,4,11,12,13]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)

        print(a.countComponents(test[0],test[1]))
