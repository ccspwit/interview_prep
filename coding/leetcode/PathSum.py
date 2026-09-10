# -*- coding: utf-8 -*-
"""
Created on May 19 2017
Leetcode 112, 113, 437 combined
---#112
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

---#113
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example: for the above tree
return
[[5,4,11,2],
[5,8,4,5]]

---#437
You are given a binary tree in which each node contains an integer value. Find
the number of paths that sum to a given value. The path does not need to
start or end at the root or a leaf, but it must go downwards (traveling only
from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
@author: K Li
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def addNode(self, val):
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
    def showNode(self):
        if self.left is not None:
            self.left.showNode()
        print(self.val, end=' ')
        if self.right is not None:
            self.right.showNode()

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        path sum III, brute-force recursive solution
        Similar to regular DFS recursion. So not as many as recursions for
        brute-force recusion. The trick is
        1. keep track of path sum from current level to root, reverse/prefix
        cumsum.
        2. At each level, get count of target values from prefix cumsum.
        3. Aggregate all counts.
        Use list to implement prefix cumsum, count is O(n). Could use dict
        to count O(1)
        """
        self.sum = sum
        self.result = 0
        if not root:
            return 0
        self.countPathSum(root, [])
        return self.result
        
    def countPathSum(self, node, vl):
        if not node:
            return
        vl = [i+node.val for i in vl] + [node.val]
        self.result += vl.count(self.sum)
        self.countPathSum(node.left, vl)
        self.countPathSum(node.right, vl)
        return

    def pathSumR(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        path sum III, brute-force recursive solution
        Call two functions recursively, for each node
        1. Call pathSumR to recursively count of left/right subtrees with
        target path sum
        2. Call countPathSumR to recursively count path originated from current
        node with sum of target
        Will perform a lot of recursions. Performance is O(nlogn) ~ O(n^2)
        """
        if root is None:
            return 0

        count = self.countPathSumR(root, target) + \
        self.pathSumR(root.left, target) + \
        self.pathSumR(root.right, target)
        
        return count
    
    def countPathSumR(self, root, target):
        """
        Compute the number of subarrays that sums to num
        """
        if root:
            val = root.val
            count = int(val == target)
            count += self.countPathSumR(root.left, target-val)
            count += self.countPathSumR(root.right, target-val)
            return count
        return 0    

    def hasPathSum(self, root, num):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        Decide if sum of any path from root-leaf equals to num.
        Recursive solution
        """
        if (root is None):
            return False
        result = False
        if (root.left is None) & (root.right is None):
            return num==root.val
        if root.left is not None:
            result |= self.hasPathSum(root.left, num-root.val)
        if root.right is not None:
            result |= self.hasPathSum(root.right, num-root.val)
        return result

    def pathSumI(self, root, num):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        Call getPathSum with path as a parameter.
        Use self.result to store found path
        """
        if root is None:
            return []
        path = []
        self.result = []
        self.getPathSumI(root, num, path)
        
        return self.result
    
    def getPathSumI(self, root, num, path):
        """
        Traverse the tree recursively, deduct current node value when step
        into left/right node. keep trace of path value in path (list).
        When reach leaf node, check if pathSum==num, save path if yes.
        A slightly memory optimzed version. add root.val to path in the beging
        and remove root.val from path at the end.
        """
        if root is None:
            return []
        path.append(root.val)
        if (root.left is None) & (root.right is None):
            #print(num, root.val)
            if num==root.val:
                self.result.append(path[:]) # NOTE, need to make a copy here
            #print(path, self.result)

        if root.left is not None:
            self.getPathSumI(root.left, num-root.val, path)
        if root.right is not None:
            self.getPathSumI(root.right, num-root.val, path)
        
        path.pop()
        return 

    def getPathSumI1(self, root, num, path):
        """
        Traverse the tree recursively, deduct current node value when step
        into left/right node. keep trace of path value in path (list).
        When reach leaf node, check if pathSum==num, save path if yes.
        Note you need to keep a copy of path for different paths which is not
        very memory efficient.
        """
        if root is None:
            return []
        path.append(root.val)
        if (root.left is None) & (root.right is None):
            #print(num, root.val)
            if num==root.val:
                self.result.append(path)

        if root.left is not None:
            self.getPathSumI1(root.left, num-root.val, path[:])
        if root.right is not None:
            self.getPathSumI1(root.right, num-root.val, path[:])
        
        return 

        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([],0),([22],22),
                  ([2,2,2,2,2],4),
                  ([0,0,0,0,0,0],0),
                  ([6,4,8,2,5,7,10],10),
                  ([5,4,8,11,13,4,7,2,5,1],15)]
    #testVector = [([2,2,2,2,2],4),([0,0,0,0,0,0],0)]
    a = Solution()
    testVector = [(list(random.randint(1,1000,100)),111)]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        array, number = test[0], test[1]
        x = None
        for j in range(len(array)):
            if j == 0:
                x = TreeNode(array[j])
            else:
                x.addNode(array[j])

        if x: x.showNode()
        print()
        #print('Tree has sum', number, 'YES' if a.hasPathSum(x,number) else 'NO')
        #print('Root--Leaf paths with sum', number, 'are',a.pathSumI(x,number))
        print('The number of paths with sum %d is: %d'%(number, a.pathSum(x,number)))
        print('The number of paths with sum %d is: %d'%(number, a.pathSumR(x,number)))