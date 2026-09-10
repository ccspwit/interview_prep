# -*- coding: utf-8 -*-
"""
Created on Thu June 7, 2017
LeetCode problem 133
Clone an undirected graph. Each node in the graph contains a label and a list
of its neighbors.

OJ's undirected graph serialization:
Nodes are labeled uniquely.
We use # as a separator for each node, and , as a separator for node label
and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.
The graph has a total of three nodes, and therefore contains three parts as
separated by #.
First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming
a self-cycle.
Visually, the graph looks like the following:

       1
      / \
     /   \
    0 --- 2
         / \
         \_/
@author: K Li
"""

# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        
    def addNode(self, nodeList):
        '''
        '''
        self.neighbors.extend(nodeList)
    
    def showNode(self):
        print(self.label,": ",end="")
        for node in self.neighbors:
            print(node.label, end=' ')
        print()
class Solution(object):
    # @param node, a undirected graph node
    # @return a undirected graph node
    # BFS unique
    def cloneGraph(self, node):
        if node is None:
            return node

        stack = [node]
        root = UndirectedGraphNode(node.label)
        nodeVisited = {node:root}

        while stack:
            oldNode = stack.pop()
            curNode = nodeVisited[oldNode]
            #nextLevel = []
            for nn in oldNode.neighbors:
                if nn in nodeVisited:
                    curNode.neighbors.append(nodeVisited[nn])
                else:
                    newNode = UndirectedGraphNode(nn.label)
                    curNode.neighbors.append(newNode)
                    stack.append(nn)
                    nodeVisited[nn] = newNode
            #stack = nextLevel
        return root
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[[0,1,2],[1,2],[2,2]]]
    a = Solution()
    #testVector = [[10,3,4,11,12,13]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x0 = UndirectedGraphNode(0)
        x1 = UndirectedGraphNode(1)
        x2 = UndirectedGraphNode(2)
        x0.addNode([x1,x2])
        x1.addNode([x2])
        x2.addNode([x2])
        x0.showNode()
        x1.showNode()
        x2.showNode()
        #print()

        y = a.cloneGraph(x0)
        y.showNode()
        for node in y.neighbors:
            node.showNode()
        #print(a.largestValues1(x))
