# -*- coding: utf-8 -*-
"""
Created on June 1 2019
LeetCode problem 92
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
@author: K Li
"""
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        # find begin and end nodes for the swap
        pre_head = ListNode(0)
        pre_head.next = head
        prev, curr = pre_head, head
        
        count = 1
        # find the node to start swapping
        while count < m:
            prev = curr
            curr = curr.next
            count += 1
        # start swapping until reach the end node
        tail, next_node = curr, curr.next
        while count < n:
            last = curr
            curr = next_node
            next_node = next_node.next
            curr.next = last
            count += 1
        tail.next = next_node
        prev.next = curr

        # head may be reversed
        if m==1:
            return curr
        else:
            return head
