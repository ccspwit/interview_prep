# -*- coding: utf-8 -*-
"""
Created on May 14 2017
LeetCode problem 234
Given a singly linked list, determine if it is a palindrome.

Follow up:
Could you do it in O(n) time and O(1) space?
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
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        If we really want to only used O(1) extra space, we could reverse
        the first half of the linked list, also find mid-pointer. Compare
        the first half and second half of the linked list. Then restore
        the first half in normal order. Although this use O(1) extra space,
        it is not recommended because it involves o(n) memory write operation
        which is not very time efficient.
        O(n) time, O(1) space
        """
        rev = None
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, head = head, rev, head.next
        tail = head.next if fast else head
        isPali = True
        while rev:
            isPali = isPali and rev.val == tail.val
            head, head.next, rev = rev, head, rev.next
            tail = tail.next
        return isPali

    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Straightforward solution, get a list from the LinkedList first.
        It's easier to check if the list is palindrome or not.
        O(n) time, O(n) space
        """
        def getList(node):
            result = []
            while node is not None:
                result.append(node.val)
                node  = node.next
            return result
        numList = getList(head)
        N = len(numList)
        if N<=1:
            return True
        for n in range(N//2):
            if numList[n] != numList[N-1-n]:
                return False
        return True

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
    testVector = [[],[1],[1,2,3,2,1],
                  [1,2,3,3,2,1],[1,2,3,3,2,2,1]]
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        print(test)
        x = genListArray(test)
        y = a.isPalindrome(x)
        print('Is palindrome? ', y)
