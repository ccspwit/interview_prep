# -*- coding: utf-8 -*-
"""
Created on Thu May 2nd 2017
LeetCode problem 94
Given a binary tree, return the inorder/preorder/postorder traversal of
its nodes' values.

For example:
Given binary tree [1,null,2,3], return [1,3,2]
Note: Recursive solution is trivial, could you do it iteratively?
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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Iterative inorder transversal, very very concise. Beautiful!!!
        left, root, right
        """
        
        stack = []
        result = []
        
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                result.append(node.val)
                root = node.right
        return result

    def inorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Iterative inorder transversal
        left, root, right
        """
        
        inorderList = []
        nodeStack = []
        if root is None:
            return []

        curNode = root
        Done = False
        while not Done:
            if(curNode is not None):
                nodeStack.append(curNode)
                curNode = curNode.left
            else:
                if nodeStack:
                    curNode = nodeStack.pop()
                    inorderList.append(curNode.val)
                    if(curNode is not None):
                        curNode = curNode.right
                else:
                    Done = True
                
        return inorderList

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Iterative preorder transversal.
        root, left, right
        """
        
        if root is None:
            return []
        nodeStack, result = [root], []
        while nodeStack:
            node = nodeStack.pop()
            result.append(node.val)
            if node.right is not None:
                nodeStack.append(node.right)
            if node.left is not None:
                nodeStack.append(node.left)
        return result

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Iterative postorder transversal
        left, right, root
        """
        
        if root is None:
            return []

        ans = []
        stack = []

        notDone = True
        while notDone:
            while root:
                # Push root's right child and then root to stack
                if root.right is not None:
                    stack.append(root.right)
                stack.append(root)
                # Set root as root's left child
                root = root.left
            
            # Pop an item from stack and set it as root
            root = stack.pop()
            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
            if stack:
                if (root.right is not None) and (stack[-1] == root.right):
                    stack.pop() # Remove right child from stack 
                    stack.append(root) # Push root back to stack
                    root = root.right # change root so that the 
                    # righ childis processed next
                else:
                    # get root's data and set root as None
                    ans.append(root.val)
                    root = None
            else:
                ans.append(root.val)
                notDone = False
                
        return ans

    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Iterative postorder transversal.
        left, right, root. Amazingly simple
        swap left and right in preordertraversal. Then reverse the result.
        """
        
        if root is None:
            return []
        nodeStack, result = [root], []
        node = root
        while nodeStack:   # or (node is not None):
            node = nodeStack.pop()
            result.append(node.val)
            
            if node.left is not None:
                nodeStack.append(node.left)
            if node.right is not None:
                nodeStack.append(node.right)

        return result[::-1]

    def inorderTraversalR(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Recursive inorder transversal
        """
        retVal = []
        if root is None:
            return []
        if root.left is not None:
            retVal.extend(self.inorderTraversalR(root.left))
        retVal.append(root.val)
        if root.right is not None:
            retVal.extend(self.inorderTraversalR(root.right))
        
        return retVal

    def postorderTraversalR(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        Recursive postorder transversal
        """
        retVal = []
        if root is None:
            return []
        if root.left is not None:
            retVal.extend(self.postorderTraversalR(root.left))
        if root.right is not None:
            retVal.extend(self.postorderTraversalR(root.right))
        retVal.append(root.val)
        
        return retVal
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],
                  [1,3,5,7,9],[9,7,5,3,1],
                  [5,3,6,2,4,1],
                  [10,2,4,6,8,12,14,16,18]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        x = None
        y = None
        for j in range(len(test)):
            if j == 0:
                x = TreeNode(test[j])
            else:
                x.addNode(test[j])

        if x: x.showNode()
        print()

        print('Inorder traversal: ', a.inorderTraversal(x))
        print('Preorder traversal: ', a.preorderTraversal(x))
        print('Postorder traversal: ', a.postorderTraversal(x))
        print('Postorder traversal: ', a.postorderTraversalR(x))
    random.seed(0)
    #test = random.randint(-1000,1000,500)
