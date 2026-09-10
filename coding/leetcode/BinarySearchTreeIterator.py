# -*- coding: utf-8 -*-
"""
Created on Thu June 6, 2017
LeetCode problem 173
Implement an iterator over a binary search tree (BST). Your iterator will
be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Note: next() and hasNext() should run in average O(1) time and uses O(h)
memory, where h is the height of the tree.

Credits:
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

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        # push node and all left nodes into stack
        while root:
            # go to left most
            self.stack.append(root)
            #node = root
            root = root.left
            #node.left == None                

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True
        else:
            return False

    def next(self):
        """
        :rtype: int
        """
        #root = self.node
        stack = self.stack

        if stack:
            node = stack.pop()
            if node is None:
                return None
            value = node.val
            if node.right:
                stack.append(node.right)

                node = node.right
                node = node.left
                while node:
                    stack.append(node)
                    node = node.left
            return value
        else:
            print("No next value")

        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,7],[10,2,4,6,8,12,14,16,18]]
    #testVector = [[5,3,6,2,4,7]]#[[10,3,4,11,12,13]]
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
        
        i, v = BSTIterator(x), []
        while i.hasNext(): v.append(i.next())
