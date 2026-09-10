# -*- coding: utf-8 -*-
"""
Created on Fri May 5, 2017
LeetCode problem 141, 142 combined
---#141
Given a linked list, determine if it has a cycle in it.

Follow up: Can you solve it without using extra space?

---#142
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

Note: Do not modify the linked list.
Follow up: Can you solve it without using extra space?
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
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Space O(1) solution. Maintain two pointers, fast and slow.
        Slow pointer move 1 step at a time while fast pointer move 2 steps
        at a time. If fast pointer catches up with slow pointer, return True.
        When fast pointer reaches the END, return False.
        """
        
        if(head is None):
            return False
        elif head.next is None:
            return False
        slow, fast = head, head.next

        while fast.next is not None:
            if fast == slow:
                return True
            else:
                slow = slow.next
                fast = fast.next
                if fast.next is None:
                    return False
                else:
                    fast = fast.next
        return False

    def hasCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Use set to store all previous node. Check if node.next is already
        stored in the hash table, cycle detected. return True.
        """
        
        if(head is None):
            return False
        nodeSet = {head}
        node = head
        nodeExist = False
        while node.next is not None:
            if node.next in nodeSet:
                return True
            else:
                nodeSet.add(node.next)
                node = node.next
        return nodeExist

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Space O(1) solution. Maintain two pointers, fast and slow.
        Slow pointer move 1 step at a time while fast pointer move 2 steps
        at a time.
        Denote distance from head to loop node is m, length of the loop is l,
        k is distance of the meeting point from the begining of the loop node.
        When two pointers meet, the distance they travelled
        D_slow = m+k+l*p, and D_fast = m+k+l*q
        Node D_fast = 2*D_slow, we will get
        m+k = (q-2*p)l, or m = (q-2p)*l -k
        If we reset two pointer, slow start from head with speed 1, while
        fast start at meeting point also with speed one. When slow reaches
        meeting point, it travels m. Fast point travels (q-2p)l -k will also
        reach loop point. Therefore the meeting point is the loop node.
        """
        
        if(head is None):
            return None
        elif head.next is None:
            return None
        slow, fast = head, head

        while fast.next is not None:
            fast = fast.next
            if fast.next is None:
                return None
            else:
                slow = slow.next
                fast = fast.next
                if fast == slow:
                    break
        if fast.next is None:
            # no loop found
            return None
        else:
            # loop found, reset slow to head node
            slow = head
            while slow != fast:
                #print(slow.val, fast.val)
                slow = slow.next
                fast = fast.next
        return slow

    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Use set to store all previous node. Check if node.next is already
        stored in the hash table, cycle detected. return current node.
        """
        
        if(head is None):
            return None
        nodeSet = {head}
        node = head
        nodeExist = False
        while node.next is not None:
            if node.next in nodeSet:
                return node.next
            else:
                nodeSet.add(node.next)
                node = node.next
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
        x.printVal()
    else:
        print('[]')

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [[],[1],[1,2,3,4,5],[1,2,3,4,5]]
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        x = genListArray(test)
        #printList(x)
        y = Solution()
        z = y.hasCycle(x)
        print('YES' if z else 'NO')
        #z = y.detectCycle(x)

    x = genListArray([1,2,3,4,5,6,7])
    z = y.detectCycle(x)
    print(z)
    #x.next.next.next = x.next
    x.next.next.next.next.next = x.next.next.next
    z = y.detectCycle(x)
    print(z.val)
    z = y.detectCycle1(x)
    print(z.val)
