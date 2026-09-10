# -*- coding: utf-8 -*-
"""
Created on June 1, 2019
LeetCode problem 82
Given a sorted linked list, delete all nodes that have duplicate
numbers, leaving only distinct numbers from the original list.

Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:
Input: 1->1->1->2->3
Output: 2->3
@author: K Li
"""
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # cleaner version
        prev_head = ListNode(0)
        prev_head.next = head
        prev, curr = prev_head, head
        while curr and curr.next:
            if curr.val == curr.next.val:
                dup_val = curr.val
                while curr.next and curr.next.val == dup_val:
                    curr = curr.next
                # prune nodes
                prev.next = curr.next
                if curr.next is None:
                    curr = None
                else:
                    curr = curr.next
            else:
                prev = curr
                curr = curr.next

        return prev_head.next

    def deleteDuplicates1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        # create a node that points to head
        prev_head = ListNode(0)
        prev_head.next = head
        prev_node = prev_head
        curr_node = head
        next_node = curr_node.next
        
        dup_count = 0
        
        while next_node is not None:
            if curr_node.val != next_node.val:
                prev_node = curr_node
                curr_node = curr_node.next
                next_node = next_node.next
            else:
                # go to next different value
                last_val = curr_node.val
                while  next_node.next is not None and (next_node.next.val==last_val):
                    next_node = next_node.next
                # prune nodes
                if next_node.next is not None:
                    prev_node.next = next_node.next
                    curr_node = next_node.next
                    next_node = curr_node.next
                else:
                    prev_node.next = None
                    curr_node = None
                    next_node = None
                
                # move head if necessary
                if head.val == last_val:
                    head = curr_node

        # handle the head/prev_node
        return head
