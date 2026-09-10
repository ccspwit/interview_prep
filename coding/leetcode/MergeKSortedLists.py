# -*- coding: utf-8 -*-
"""
Created on June 6, 2017
LeetCode problem 23
Merge k sorted linked lists and return it as one sorted list. Analyze and
describe its complexity.
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
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        use heap to maintain k current nodes, to avoid node comparison error
        store (node.val, index)
        Try use replace to optimize performance
        """
        import heapq
        
        head = ListNode(0)
        ptr = head
        heap = []
        # push first element of each LL into heap
        for n in range(len(lists)):
            node = lists[n]
            if node:
                heapq.heappush(heap, (node.val, n))
        heapq.heapify(heap)
        
        #get node with minimal values, and push next node in the list
        while heap:
            val, ind = heap[0]
            ptr.next = lists[ind]
            ptr = ptr.next
            if ptr.next:
                lists[ind] = ptr.next
                heapq.heapreplace(heap, (ptr.next.val, ind))
            else:
                heapq.heappop(heap)

        return head.next

    def mergeKLists1(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        use heap to maintain k current nodes, to avoid node comparison error
        store (node.val, index)
        """
        import heapq
        
        head = ListNode(0)
        ptr = head
        heap = []
        # push first element of each LL into heap
        for n in range(len(lists)):
            node = lists[n]
            if node:
                heapq.heappush(heap, (node.val, n))

        #get node with minimal values, and push next node in the list
        while heap:
            val, ind = heapq.heappop(heap)
            ptr.next = lists[ind]
            ptr = ptr.next
            if ptr.next:
                lists[ind] = ptr.next
                heapq.heappush(heap, (ptr.next.val, ind))

        return head.next

    def mergeKLists0(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        use heap to maintain k current nodes
        directly push (val, node) does not work in my python 3.6
        """
        import heapq
        
        K = len(lists)
        head = ListNode(0)
        ptr = head
        heap = []
        # push first element of each LL into heap
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))

        #get node with minimal values, and push next node in the list
        while heap:
            val, ptr.next = heapq.heappop(heap)
            ptr = ptr.next
            if ptr.next:
                heapq.heappush(heap, (ptr.next.val, ptr.next))

        return head.next
        

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
    testVector = [[1,3,5,7,9],[4,6,8,10,12],[0,4,11,13]]
    listLL = []
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        print(test)
        x = genListArray(test)
        listLL.append(x)
    y = a.mergeKLists(listLL)
    printList(y)
