# -*- coding: utf-8 -*-
"""
Created on May 29, 2017
LeetCode problem 24
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values
in the list, only nodes itself can be changed.
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
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Need to keep track of previous node and current Node
        """
        if (head is None) or (head.next is None):
            return head
        
        curNode = head
        head = head.next
        prevNode = None
        #print(curNode.val)
        
        while (curNode is not None) and (curNode.next is not None):
            nextPair = curNode.next.next
            #print(curNode.val, nextPair.val)
            if prevNode:
                prevNode.next = curNode.next
            curNode.next.next = curNode
            curNode.next = nextPair
            prevNode = curNode
            curNode = nextPair
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
    testVector = [[],[1],[1,2,3,4,5],[1,1,2,3,2,4]]
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        print(test)
        x = genListArray(test)
        printList(x)
        y = a.swapPairs(x)
        printList(y)
