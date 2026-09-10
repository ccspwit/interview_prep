# -*- coding: utf-8 -*-
"""
Created on June 1, 2019
LeetCode problem 86
Given a linked list and a value x, partition it such that all
nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes
in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
@author: K Li
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        # create two new head
        left_head = ListNode(0)
        right_head = ListNode(0)
        curr = head
        left_ptr, right_ptr = left_head, right_head

        while curr:
            if curr.val < x:
                left_ptr.next = curr
                left_ptr = curr
                curr = curr.next
            else:
                right_ptr.next = curr
                right_ptr = curr
                curr = curr.next
        
        # combine two lists
        left_ptr.next = right_head.next
        right_ptr.next = None

        return left_head.next
