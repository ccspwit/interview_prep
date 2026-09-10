# -*- coding: utf-8 -*-
"""
Created on May 14, 2017
Leetcode 235, 236 combined
---#235
Given a binary search tree (BST), find the lowest common ancestor (LCA) of
two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes v and w as the lowest node in T that has both
v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6.
Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant
of itself according to the LCA definition.

---#236
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes
in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor
is defined between two nodes v and w as the lowest node in T that has both v
and w as descendants (where we allow a node to be a descendant of itself).”

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
For example, the lowest common ancestor (LCA) of nodes
5 and 1 is 3. Another example is LCA of nodes 5 and 4 is 5,
since a node can be a descendant of itself according to the
LCA definition.
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
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        #return self.lowestCommonAncestorI(root, p, q)
        return self.lowestCommonAncestorII(root, p, q)

    def lowestCommonAncestorII(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Recursively call getLCA function, the key observation
        is if the node is not common ancester, then one of
        the subtree (left or right) can not match p or q.
        O(h) time and O(h) space
        """
        def lcaRecursive(root, node1, node2):
            """
            Return lca node in a binary tree recursively.
            """
            if (root == node1) or (root==node2):
                return root
            if (root.left is None) and (root.right is None):
                return None

            a1, a2 = None, None
            if root.left is not None:
                a1 = lcaRecursive(root.left, node1, node2)
            if root.right is not None:
                a2 = lcaRecursive(root.right, node1, node2)
            if a1 and a2:
                return root
            elif a1 is None:
                return a2
            else:
                return a1
        
        lca = lcaRecursive(root, p, q)
        return lca

    def lowestCommonAncestorII2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Get list of ancestors of p and q first,
        then compare two lists for LCA from start
        working, but use too much memory
        """
        def getAncestorsRecursive(root, node, path, res):
            """
            Return a list of ancesters of a node in a binary tree recursively.
            """
            if root == node:
                res.extend(path)
                #print(len(res),res)
                return

            if root.left is not None:
                getAncestorsRecursive(root.left, node,
                                      path+[root.left], res)
            if root.right is not None:
                getAncestorsRecursive(root.right, node,
                                      path+[root.right], res)
            return
        
        a1, a2 = [], []
        getAncestorsRecursive(root, p, [root], a1)
        getAncestorsRecursive(root, q, [root], a2)
        n1, n2 = len(a1), len(a2)
        #print(n1,n2)
        for n in range(min(n1,n2)):
            if a1[n] == a2[n]:
                n += 1
            else:
                break
        if n>0:
            return a1[n-1]
        else:
            return None

    def lowestCommonAncestorI(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        A more efficient way is two compare p and q with current node,
        if they are same direction, i.e. both left or right, go to that
        direction. If not, return current node.
        O(h) time and O(1) space
        """
        if p.val > q.val:
            p, q  = q, p
        node = root
        while node is not None:
            print(p.val, q.val, root.val)
            if (node.val==p.val) or (node.val==q.val):
                return node
            elif (q.val<node.val):
                node = node.left
            elif (p.val>node.val):
                node = node.right
            elif (p.val < node.val <q.val):
                return node
        return None

    def lowestCommonAncestorI2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        Get list of ancestors of p and q first, then compare two lists for
        LCA from start
        O(h) time and O(h) space
        """
        def getAncestors(root, val):
            """Return a list of ancesters of a node in a BST
            """
            ancestors = []
            node = root
            while node is not None:
                ancestors.append(node)
                if node.val == val:
                    return ancestors
                elif val < node.val:
                    node = node.left
                else:   #val>node.val
                    node = node.right
            return [None]
        a1 = getAncestors(root, p.val)
        a2 = getAncestors(root, q.val)
        n1, n2 = len(a1), len(a2)
        for n in range(min(n1,n2)):
            if a1[n] == a2[n]:
                n += 1
            else:
                break
        if n>0:
            return a1[n-1]
        else:
            return None


if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    """testVector = [[],[1],[1,2],
                  [2,2,2,2,2],[9,7,5,3,1],
                  [5,3,6,2,4,1],
                  [10,6,14,16,2,8,12,18]]"""
    test = [5,3,6,2,4,1]
    a = Solution()
    print(test)
    x = None
    for j in range(len(test)):
        if j == 0:
            x = TreeNode(test[j])
        else:
            x.addNode(test[j])

    if x: x.showNode()
    print()
    y = x.left.left
    z = x.left.right
    print('Lowest common ancestor of is', a.lowestCommonAncestor(x,y,z).val)
    y = x.left.left
    z = x.left.right
    print('Lowest common ancestor of is', a.lowestCommonAncestorI2(x,y,z).val)