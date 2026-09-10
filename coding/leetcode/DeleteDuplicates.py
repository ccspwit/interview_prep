# -*- coding: utf-8 -*-
"""
Created on Thu May 1st 2017
LeetCode problem 83
Given a sorted linked list, delete all duplicates such that each element
appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

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
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head

        curVal = head.val
        curNode = head
        nextNode = head.next
        while nextNode:
            if nextNode.val == curVal:
                curNode.next = nextNode.next
            else:
                curVal = nextNode.val
                curNode = nextNode
            nextNode = nextNode.next

        return head
    
    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        prevVal = head.val
        prevNode = head
        curNode = head.next
        duplicate = False
        while curNode:
            if curNode.val == prevVal:
                duplicate = True
            else:
                if duplicate:   # remove duplicated nodes
                    prevNode.next = curNode
                prevVal = curNode.val
                prevNode = curNode
                duplicate = False
            curNode = curNode.next
        if duplicate:
            prevNode.next = curNode
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
    testVector = [[1,2,3,4],[1,1,1,2,3,4,4],
                  [1,2,2,2],[]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        x = genListArray(test)
        a = Solution()
        y = a.deleteDuplicates(x)
        x = genListArray(test)
        z = a.deleteDuplicates1(x)
        printList(x)
        printList(y)
        printList(z)
