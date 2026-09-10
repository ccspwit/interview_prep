# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 2017
LeetCode problem 21
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
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
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        FirstNode = ListNode(-1)
        curNode = FirstNode
        count = 0
        
        while (l1 != None) & (l2 != None):
            if l1.val <= l2.val:    # l1 <= l2
                curNode.next = l1
                curNode = l1
                l1 = l1.next
            else:   #l2 between curNode and l1
                curNode.next = l2
                curNode = l2
                l2 = l2.next
            count += 1
            #FirstNode.printVal()
            #if count>=20:
            #    return None
        # either l1 or l2 reach the end
        if l1 is None:
            curNode.next = l2
        if l2 is None:
            curNode.next = l1
        return FirstNode.next

    def mergeTwoLists1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        FirstNode = ListNode(-1)
        FirstNode.next = l1
        curNode = FirstNode
        while (l1.next != None) & (l2.next != None):
            if l1.val <= l2.val:    # l1 <= l2
                l1 = l1.next
                curNode = l1
            else:   #l2 between curNode and l1
                curNode.next = l2
                temp1 = l1
                temp2 = l2
                l1 = l1.next
                l2 = l2.next
                temp2.next = temp1.next
                temp1.next = temp2
            if l2.val <= l1.val:
                pass
            else:# l1> l2
                if l2.next.val<= l1.val:
                    l2 = l2.next
                else:   #l1 between l2 and l2.next
                    temp1 = l1
                    temp2 = l2
                    l1 = l1.next
                    l2 = l2.next
                    temp1.next = temp2.next
                    temp2.next = temp1
        
        # either l1 or l2 reach the end
        return None

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
        print(x.printVal())
    else:
        print('[]')
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([1,2],[3,4]),([1,3],[2,4]),
                  ([],[]),([],[1,2,3,4,5]),([1,2,3,4,5],[]),
                  ([1,3,5,99],[2,4,6,8,10])]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        x1 = genListArray(test[0])
        x2 = genListArray(test[1])
        printList(x1); printList(x2)
        y = Solution()
        z = y.mergeTwoLists(x1,x2)
        printList(z)
