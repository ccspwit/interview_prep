# -*- coding: utf-8 -*-
"""
Created on June 4, 2017
Leetcode 606
ou need to construct a string consists of parenthesis and integers from a
binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And
you need to omit all the empty parenthesis pairs that don't affect the
one-to-one mapping relationship between the string and the original binary tree.

Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

Output: "1(2(4))(3)"
Explanation: Originallay it needs to be "1(2(4)())(3()())", 
but you need to omit all the unnecessary empty parenthesis pairs. 
And it will be "1(2(4))(3)".

Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example, 
except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.
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

    def tree2str1(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preOrder(node):
            result = ["("+str(node.val)]
            if node.left:
                result.extend(self.tree2str(node.left))
            elif node.right:
                result.append("()")
            if node.right:
                result.extend(self.tree2str(node.right)[:])
            result.append(")")
            return result
        
        if t is None:
            return "()"

        self.ans = preOrder(t)
        print(self.ans, len(self.ans))
        result = "".join(self.ans)
        ret = ""
        for i in range(1,len(result)-1):
            ret += result[i]
        return ret

    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        def preOrder(node):
            result = "("+str(node.val)
            if node.left:
                result += preOrder(node.left)
            elif node.right:
                result += "()"
            if node.right:
                result += preOrder(node.right)
            result += ")"
            return result
        
        if t is None:
            return ""

        ans = preOrder(t)
        return ans[1:-1]
                
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[2,1],[2,1,3],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,7]]
                  #[10,6,14,16,2,8,12,18]]
    a = Solution()
    for n, test in enumerate(testVector):
        print('Test case ----- ', n)
        print(test)
        x = None
        for j in range(len(test)):
            if j == 0:
                x = TreeNode(test[j])
            else:
                x.addNode(test[j])
    
        if x: x.showNode()
        print()
        print(a.tree2str(x))
