# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 2017
LeetCode problem 2
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a
single digit. Add the two numbers and return it as a linked list. You may assume
the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
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

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = l1.val+l2.val
        if(result>=10):
            result -= 10
            carry = 1
        else:
            carry = 0
        retNode = ListNode(result)
        curNode = retNode

        while (l1.next!=None) | (l2.next!=None):
            result = carry
            if(l1.next!=None):
                l1 = l1.next
                result += l1.val

            if(l2.next!=None):
                l2 = l2.next
                result += l2.val

            if(result>=10):
                result -= 10
                carry = 1
            else:
                carry = 0
            nextNode = ListNode(result)
            curNode.next = nextNode
            curNode = nextNode
        
        if(carry):
            nextNode = ListNode(carry)
            curNode.next = nextNode
            
        return retNode

    def addTwoNumbers1(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: integer
        """
        result = 0
        carry = 0
        scale = 1
        result = l1.val+l2.val
        while (l1.next!=None) | (l2.next!=None):
            scale *= 10
            if(l1.next!=None):
                l1 = l1.next
                result += l1.val*scale
            if(l2.next!=None):
                l2 = l2.next
                result += l2.val*scale

        return result

def genListInt(num):
    '''
    Generate a linked list from an integer from right to left.
    For example, number 123 will generate 3 -> 2 -> 1
    '''
    if not isinstance(num, int):
        raise TypeError('Input number must be of integer type')
    if num < 0:
        raise ValueError('Input number must not be NEGATIVE')
    rem = num % 10
    firstNode = ListNode(rem)
    prevNode = firstNode
    while num>= 10:
        num = num//10
        rem = num % 10
        nextNode = ListNode(rem)
        prevNode.next = nextNode
        prevNode = nextNode
        
    return firstNode
        
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    n1 = random.randint(0,2**8)
    n2 = random.randint(0,2**8)
    xl = genListInt(n1)
    #xl.printVal()
    yl = genListInt(n2)
    #yl.printVal()
    z = Solution()
    #print('%d + %d = %d'%(n1,n2,n1+n2))
    zl = genListInt(n1+n2)
    zl.printVal()
    print()
    z.addTwoNumbers(xl,yl).printVal()
    print('-----------')