# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 2017
LeetCode problem 19
Given a linked list, remove the nth node from the end of list and return its head.
Given n will always be valid. Try to do this in one pass.

For example,
Given linked list: 1->2->3->4->5, and n = 2.
After removing the 2nd node from the end, the linked list becomes 1->2->3->5.

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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Maintain two pointers that are n+1 apart, prevNode, and nthNode
        remove listNode after prevNode depending on boundary conditions
        """
        
        # assume the length of linked list >= n
        head
        curNode = head
        prevNode = head
        nthNode = head
        for i in range(n-1):
            if nthNode.next is None:
                raise ValueError('Reach the end of list, n is too large!')
            nthNode = nthNode.next
        if nthNode.next!= None:
            nthNode = nthNode.next
        else:
            return head.next
        while nthNode.next!= None:
            nthNode = nthNode.next
            prevNode = prevNode.next
            
        prevNode.next = prevNode.next.next
            
        return head

    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        Maintain three pointers, prevNode, curNode, and nthNode
        remove curNode depending on boundary conditions
        """
        
        # assume the length of linked list >= n
        head
        curNode = head
        prevNode = curNode
        nthNode = head
        for i in range(n-1):
            if nthNode.next is None:
                raise ValueError('Reach the end of list, n is too large!')
            nthNode = nthNode.next
        while nthNode.next!= None:
            nthNode = nthNode.next
            prevNode = curNode
            curNode = curNode.next
            
        # Consider the edge cases
        if (curNode == head):
            return head.next
        else:
            prevNode.next = curNode.next
            
        return head
        
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
    import numpy.random as random
    testVector = [([1,2,3,4,5],1),([1,2,3,4,5],2),
                  ([1,2,3,4,5],5),([1],1)]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        x = genListArray(test[0])
        printList(x)
        print(test[1])
        y = Solution()
        z = y.removeNthFromEnd(x, test[1])
        printList(z)
