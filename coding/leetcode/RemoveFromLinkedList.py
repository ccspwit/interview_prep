# -*- coding: utf-8 -*-
"""
Created on Sun May 7, 2017
LeetCode problem 203
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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return

        # Skip all matching nodes from the begining
        while (head.val == val):
            if (head.next is not None):
                head = head.next
            else:
                return None
        node =  head    # first non matching node
        while node is not None:
            if node.next is None:
                return head
            elif node.next.val == val:
                # next node match, delete
                node.next = node.next.next
            else:
                # next node not match
                node = node.next
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

    a = Solution()
    testVector = [([],1),([1],1),
                  ([1,2,3,4,5],1),([1,2,3,4,5],2),
                  ([1,2,3,4,5],5),([1,1,2,2,3,4,5],1),
                  ([1,1,2,3,2,4,2],2)]
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        print(test)
        x = genListArray(test[0])
        y = a.removeElements(x, test[1])
        printList(y)
