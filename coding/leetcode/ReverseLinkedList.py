# -*- coding: utf-8 -*-
"""
Created on May 14, 2017
LeetCode problem 206
Remove all elements from a linked list of integers that have value val.

Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        The code is much more concise
        """
        if (head is None) or (head.next is None):
            return head
        # newhead is second node, nextnext is next to 2nd node
        prev = None

        # loop over the linked list
        while head is not None:
            # Advance newHead, and newNext
            curr = head
            head = head.next
            curr.next = prev
            prev = curr

        return curr

    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None) or (head.next is None):
            return head
        # newhead is second node, nextnext is next to 2nd node
        newHead = head.next
        newNext = newHead.next
        # head becomes tail, second node point to head
        head.next = None
        newHead.next = head

        # loop over the linked list
        while newNext is not None:
            # Advance newHead, and newNext
            lastNode = newHead
            newHead = newNext
            newNext = newHead.next
            if newNext is None:
                # found tail
                newHead.next = lastNode
                return newHead
            else:
                # newNext is not tail
                newHead.next = lastNode
        return newHead

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
    testVector = [[1,2,3,4,5]]#[[1],[1,2,3,4,5],[1,1,2,3,2,4,2]]
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        print(test)
        x = genListArray(test)
        y = a.reverseList(x)
        #printList(y)
