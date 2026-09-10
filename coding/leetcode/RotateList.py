# -*- coding: utf-8 -*-
"""
Created on May 30 2019
LeetCode problem 61
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
@author: K Li
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0:
            return head
        if head is None or head.next is None:
            return head
        
        len_count = 0
        next_head, tail = head, head
        # go through the list, head.next is None
        while tail.next is not None:
            len_count += 1
            tail = tail.next
            if len_count > k:
                next_head = next_head.next
        len_count += 1  # count the total number of nodes

        # swap nodes
        if len_count > k:
            tail.next = head
            new_head = next_head.next
            next_head.next = None
            return new_head
        
        # k > len_list
        m = k % len_count
        if m==0:
            return head

        # already had tail, go through len_count-m
        next_head = head
        for n in range(len_count-m-1):
            next_head = next_head.next

        # swap nodes
        tail.next = head
        new_head = next_head.next
        next_head.next = None
        return new_head
