# -*- coding: utf-8 -*-
"""
Created on June 7, 2017
LeetCode problem 103
Given a binary tree, return the zigzag level order traversal of its nodes'
values. (ie, from left to right, then right to left for the next level and
alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
@author: K Li
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def addNode(self, val):
        '''
        Binary search Tree, compare with root value, add to left is smaller
        add to right if otherwise recursively
        '''
        if val < self.val:  # add node to left
            if(self.left) is None:
                leftNode = TreeNode(val)
                self.left = leftNode
            else:
                self.left.addNode(val)
        else:   # add node to right
            if(self.right) is None:
                rightNode = TreeNode(val)
                self.right = rightNode
            else:
                self.right.addNode(val)
        return
    
    def genTreeArray():
        pass

    def showNode(self):
        if self.left is not None:
            self.left.showNode()
        print(self.val, end=' ')
        if self.right is not None:
            self.right.showNode()

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Use regular BFS with deque
        """
        from collections import deque
        
        if root is None:
            return []
        queue = deque()
        queue.append((root, 0))
        result = [[]]
        level = 0
        
        while queue:
            node, level = queue.popleft()
            if level < len(result):
                if level&1:     #zigzag here
                    result[level].insert(0,node.val)
                else:
                    result[level].append(node.val)
            else:
                result.append([node.val])
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right, level+1))

        return result
    
    def zigzagLevelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Use regular BFS, reverse nextLevel list for each odd level, if root
        is at level 0
        """
        if root is None:
            return []
        curLevel = [root]
        result = []
        level = 0
        
        while curLevel:
            if level&1:     #zigzag here
                values = [node.val for node in curLevel[::-1]]
            else:
                values = [node.val for node in curLevel]
            result.append(values)
            nextLevel = [c for nd in curLevel for c in [nd.left, nd.right] if c]
            curLevel = nextLevel
            level += 1
        return result

        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,7],[10,2,4,6,8,12,14,16,18]]
    a = Solution()
    #testVector = [[10,3,4,11,12,13]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = None
        for j in range(len(test)):
            if j == 0:
                x = TreeNode(test[j])
            else:
                x.addNode(test[j])

        if x: x.showNode()
        print()

        print(a.zigzagLevelOrder(x))
        print(a.zigzagLevelOrder1(x))
