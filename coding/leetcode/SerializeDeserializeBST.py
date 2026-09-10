# -*- coding: utf-8 -*-
"""
Created on June 1st, 2017
LeetCode problem 297
erialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer, or
transmitted across a network connection link to be reconstructed later in
the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no 
restriction on how your serialization/deserialization algorithm should work.
You just need to ensure that a binary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

For example, you may serialize the following tree
    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a
binary tree. You do not necessarily need to follow this format, so please be
creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your
serialize and deserialize algorithms should be stateless.
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

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        DFS output
        """
        def dfs(root):
            if root:
                output.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
            else:
                output.append('#')
        output = []
        dfs(root)
        return ",".join(output)
    
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        DFS construct
        """
        def dfs():
            val = next(items)
            if val!="#":
                root = TreeNode(str(val))
            else:
                return None
            root.left = dfs()
            root.right = dfs()
            return root

        items = iter(data.split(","))

        return dfs()
 
    def deserialize1(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        DFS construct
        """
        def dfs():
            val = items[self.pos]
            self.pos += 1
            if val!="#":
                root = TreeNode(str(val))
            else:
                return None
            if self.pos<N:
                root.left = dfs()
            if self.pos<N:
                root.right = dfs()
            return root

        items = data.split(",")
        N = len(items)
        self.pos = 0
        if N==0:
            return None
        #print(items)
        return dfs()
    
    def serializeLC(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        Leetcode format, level order output
        """
        def levelOrder(root):
            """
            :type root: TreeNode
            :rtype:     str
            Level order traversal, from top down
            BFS using two stacks, parent level nodes and child level nodes
            """
            if root is None:
                return ""
            curLevel = [root]
            result = ""
            
            while curLevel:
                for node in curLevel:
                    if node:
                        result += str(node.val)+","
                    else:
                        result += "null,"
                nextLevel = []
                for node in curLevel:
                    if node:
                        if node.left or node.right:
                            # left has no next level
                            nextLevel.extend([node.left, node.right])
                curLevel = nextLevel
            return result
        
        return "["+levelOrder(root)[:-1]+"]"

    def deserializeLC(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        Leetcode format, level order construct
        """
        if len(data)<=2:
            return None
        items = data[1:-1].split(',')
        N = len(items)
        if N==0:
            return None
        if items[0]!= 'null':
            root = TreeNode(int(items[0]))
        else:
            raise ValueError("Value of root can not be None")
        curLevel = [root]
        pos, nNodes = 1, 2
        while pos<N:
            nextLevel = []
            for node in curLevel:
                if pos<N:
                    val = items[pos]
                    node.left = TreeNode(int(val)) if val!="null" else None
                    if node.left:
                        nextLevel.append(node.left)
                else:
                    break
                pos += 1
                if pos<N:
                    val = items[pos]
                    node.right = TreeNode(int(val)) if val!="null" else None
                    if node.right:
                        nextLevel.append(node.right)
                else:
                    break
                pos += 1
            curLevel = nextLevel
        return root
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [1,-1,2,3],[5,3,6,2,4,7],
                  [10,2,4,6,8,12,14,16,18]]
    a = Codec()
    #testVector = [[],[1,-1,2,3]]
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
        b = a.serialize(x)
        print(b)
        c = a.serialize(a.deserialize(b))
        print(c)
