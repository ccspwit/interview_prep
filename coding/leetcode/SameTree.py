# -*- coding: utf-8 -*-
"""
Created on Thu May 1st 2017
LeetCode problem 100
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and
the nodes have the same value.
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        Iterative solution, preorder traverse: root, left, right
        Use list implementation of stack to preserve intermediate treeNode.
        """
        '''if (p is None) | (q is None):
            return p==q
        if (p.val != q.val):
            return False
        else:
            isSame = True'''
        
        stack1, stack2 = [], []
        if (p is None) | (q is None):
            return p==q
        else:
            stack1.append(p)
            stack2.append(q)
        #ptr1, ptr2 = p, q

        isSame = True
        while (len(stack1)>0) & (len(stack2)>0):
            ptr1 = stack1.pop()
            ptr2 = stack2.pop()
            
            #if (ptr1 is not None) & (ptr2 is not None):
            isSame &= (ptr1.val==ptr2.val)
        
            if(ptr1.right is not None) & (ptr2.right is not None):
                stack1.append(ptr1.right)
                stack2.append(ptr2.right)
            else:
                isSame &= (ptr1.right==ptr2.right)
                
            if(ptr1.left is not None) & (ptr2.left is not None):
                stack1.append(ptr1.left)
                stack2.append(ptr2.left)
            else:
                isSame &= (ptr1.left==ptr2.left)
                    
        return isSame

    def isSameTree3(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        Iterative solution, inorder traverse: left, root, right
        Use list implementation of stack to preserve intermediate treeNode.
        """
        '''if (p is None) | (q is None):
            return p==q
        if (p.val != q.val):
            return False
        else:
            isSame = True'''
        
        stack1, stack2 = [], []
        ptr1, ptr2 = p,q
        done = False
        isSame = True
        while not done:
            if (ptr1 is not None)&(ptr2 is not None):
                # go left first
                stack1.append(ptr1)
                stack2.append(ptr2)
                ptr1 = ptr1.left
                ptr2 = ptr2.left
            else:
                #reach the end of left most, pop a, evaluate
                isSame &= (ptr1==ptr2)
                if (len(stack1)>0)&(len(stack2)>0):
                    ptr1 = stack1.pop()
                    ptr2 = stack2.pop()
                    isSame &= (ptr1.val==ptr2.val)
                    ptr1 = ptr1.right
                    ptr2 = ptr2.right
                else:
                    done = True
                    
        return isSame

    def isSameTree2(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        Simplified version of the recursive solution.
        """
        if (p is None) | (q is None):
            return p==q
        if (p.val != q.val):
            return False
        else:
            isSame = True

        isSame = isSame & self.isSameTree2(p.left, q.left) & self.isSameTree2(p.right, q.right)
        return isSame

    def isSameTree1(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        Recursive solution. A little complicated
        """
        if (p is None) | (q is None):
            return p==q
        if (p.val != q.val):
            return False
        else:
            isSame = True

        if (p.left is not None) & (q.left is not None):
            isSame &= self.isSameTree1(p.left, q.left)
        elif (p.left is not None) & (q.left is None):
            return False
        elif (p.left is None) & (q.left is not None):
            return False
        else:
            pass

        if (p.right is not None) & (q.right is not None):
            isSame &= self.isSameTree1(p.right, q.right)
        elif (p.right is not None) & (q.right is None):
            return False
        elif (p.right is None) & (q.right is not None):
            return False
        else:
            pass
        return isSame
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([],[]),([],[1]),([1],[1]),([1],[2]),
                  ([1,3,4,7,9],[1,3,5,7,9]),
                  ([1,3,5,7,9],[1,3,5,7,9]),
                  ([1,3,5,7,9],[1,3,5,7,9,11])]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = None
        y = None
        for j in range(len(test[0])):
            if j == 0:
                x = TreeNode(test[0][j])
            else:
                x.addNode(test[0][j])
        for j in range(len(test[1])):
            if j == 0:
                y = TreeNode(test[1][j])
            else:
                y.addNode(test[1][j])

        if x: x.showNode()
        print()
        if y: y.showNode()
        print()
        print('Is same or not: {}'.format(a.isSameTree(x, y)))
        print('Is same or not: {}'.format(a.isSameTree2(x, y)))
    random.seed(0)
    #test = random.randint(-1000,1000,500)
