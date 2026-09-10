# -*- coding: utf-8 -*-
"""
Created on Fri May 5, 2017
LeetCode problem 160
Write a program to find the node at which the intersection of two singly
linked lists begins.

For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.

Notes:
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
@author: K Li
"""

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def printVal(self):
	# print value of link list start with self
        print(self.val, end = ' ')
        nextNode = self.next
        while(nextNode):
            print('-> ', nextNode.val, end = ' ')
            nextNode = nextNode.next
        print()

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        Traverse A and B to get length of A and B. Denote as M, N respectively.
        Let say length of common path is  l, M = m+L, N = n+L.
        Then we known difference D = M-N = m-n . So 
        """
        M = self.getLen(headA)
        N = self.getLen(headB)
        print(M,N)
        if (M>=N):
            D = M-N
            node1, node2 = headA, headB
        else:
            D = N-M
            node1, node2 = headB, headA
        while D>0:
            node1 = node1.next
            D -= 1
        while node1 != node2:
            node1 = node1.next
            node2 = node2.next

        return node1

    def getLen(self, head):
        length = 0
        node = head
        while node is not None:
            node = node.next
            length += 1
        return length
        
def genListArray(num):
    '''
    Generate a linked list from an integer from right to left.
    For example, number 123 will generate 3 -> 2 -> 1
    '''
    if len(num)<=0:
        return None
    FirstNode = ListNode(num[0])
    CurNode = FirstNode
    for n in num[1:]:
        nextNode = ListNode(n)
        CurNode.next = nextNode
        CurNode = nextNode
        
    return FirstNode
        
def printList(x):
    if x:
        x.printVal()
    else:
        print('[]')

if __name__ == '__main__':
	# test case to generate ListNode and run test function

    a = Solution()
    #x = genListArray([1,2,3,4,5,6,7])
    #y = genListArray([7,6,5,4,3,2,1])
    x = genListArray([1,2,3])
    y = genListArray([7,6,5])
    z = a.getIntersectionNode(x, y)
    print(z)
    #x.next.next.next = x.next
    x.next.next.next = y.next.next.next
    z = a.getIntersectionNode(x,y)
    print(z.val)
