# -*- coding: utf-8 -*-
"""
Created on Thu May 3rd 2017
LeetCode problem 102, 104, 107, 111 combined
---#102
Given a binary tree, return the level order traversal of its nodes' values.
(ie, from left to right, top level to bottom level).

For example:
Given binary tree [3,9,20,null,null,15,7],
return its level order traversal as:
[[3],
[9,20],
[15,7]]

---#104
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path from the root
node down to the farthest leaf node.

---#107
Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
return its bottom-up level order traversal as:
[[15,7],
 [9,20],
 [3]]

---#111
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root
node down to the nearest leaf node.
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Level order traversal, from top down
        BFS using two stacks, parent level nodes and child level nodes
        """
        if root is None:
            return []
        curLevel = [root]
        result = []
        level = 0
        
        while curLevel:
            values = [node.val for node in curLevel]
            result.append(values)
            nextLevel = [c for nd in curLevel for c in [nd.left, nd.right] if c]
            curLevel = nextLevel

        return result

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Do level order traversal, from bottom up
        Recursive solution. Level order top down, then reverse output
        """
        if root is None:
            return []
        curLevel = [root]
        result = []
        level = 0
        
        while curLevel:
            values = [node.val for node in curLevel]
            result.append(values)
            nextLevel = [c for nd in curLevel for c in [nd.left, nd.right] if c]
            curLevel = nextLevel

        return result[::-1]
 
    def levelOrder1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Level order traversal, from top down
        BFS using queue, need to pass level information when add node.val
        into result/List
        """
        from collections import deque

        if root is None:
            return []
        queue = deque()
        queue.append((root,0))
        result = [[]]
        level = 0
        
        while queue:
            node, level = queue.popleft()
            if level < len(result):
                result[level].append(node.val)
            else:
                result.append([node.val])
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right, level+1))

        return result

    def levelOrderR(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Do level order traversal, from top down
        Quite inefficient
        """
        if root is None:
            return []
        depth = self.maxDepth(root)
        result = []
        for i in range(depth):
            result.append(self.getIthLevel(root, i))

        return result
    
    def levelOrderBottom1(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        Do level order traversal, from bottom up
        Recursive solution
        """
        if root is None:
            return []
        depth = self.maxDepth(root)
        result = []
        for i in range(depth-1,-1,-1):
            result.append(self.getIthLevel(root, i))

        return result

    def getIthLevel(self, root, i):
        '''Traverse ith level recursively
        '''
        ithLevel = []
        if root is None:
            return ithLevel
        level = 0
        if level == i:
            return [root.val]
        if level < i:
            if root.left is not None:
                ithLevel.extend(self.getIthLevel(root.left, i-1))
            if root.right is not None:
                ithLevel.extend(self.getIthLevel(root.right, i-1))
        return ithLevel
            
        

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Find maximal depth of a binary tree iteratively
        """
        if root == None:
            return 0

        maximum = 0
        stack = [(root, 1)]
        while(len(stack)>0):
            node, depth = stack.pop()
            if(node is None):
                continue
            else:
                if(node.left is not None):
                    stack.append((node.left, depth+1))
                if(node.right is not None):
                    stack.append((node.right, depth+1))
                if (node.left is None) and (node.right is None):
                    maximum = max(maximum, depth)

        return maximum

    def maxDepthR(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Find maximal depth of a binary tree recursively
        """
        if root == None:
            return 0
        depth = 0

        n1 = self.maxDepth(root.left)
        n2 = self.maxDepth(root.right)
        depth = max(n1,n2)+1

        return depth

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Find minimum depth of a binary tree recursively
        """
        if root == None:
            return 0
        depth = 1

        if (root.left is None) and (root.right is None):
            return 1
        else:
            n1 = self.minDepth(root.left)
            n2 = self.minDepth(root.right)
            if (n1 != 0) & (n2!=0):
                depth = min(n1,n2)+1
            else:
                if n1==0:
                    depth = n2+1
                if n2==0:
                    depth = n1+1

        return depth

    def minDepthNR(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Find minimal depth of a binary tree iteratively
        """
        if root == None:
            return 0
        minimal = 1

        stack = [root]
        if (root.left is None) and (root.right is None):
            return 1
        else:
            n1 = self.minDepth(root.left)
            n2 = self.minDepth(root.right)
            if (n1 != 0) & (n2!=0):
                depth = min(n1,n2)+1
            else:
                if n1==0:
                    depth = n2+1
                if n2==0:
                    depth = n1+1

        return depth
        
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

        #print('Maximum depth of a tree is: ', a.maxDepthNR(x))R
        #print('Minimum depth of a tree is: ', a.minDepthNR(x))
        print(a.levelOrder(x))
        print(a.levelOrder1(x))
        print(a.levelOrderBottom(x))
