# Curated LeetCode Interview Prep List

High-frequency problems grouped by data structure / technique. Each category has 2 Easy and 2 Medium problems, followed by a set of well-known Hard problems.

## Categories

1. [Array & Hashing](#1-array--hashing)
2. [Two Pointers](#2-two-pointers)
3. [Sliding Window](#3-sliding-window)
4. [Stack](#4-stack)
5. [Binary Search](#5-binary-search)
6. [Linked List](#6-linked-list)
7. [Trees (Binary Tree / BST)](#7-trees-binary-tree--bst)
8. [Graphs (BFS / DFS)](#8-graphs-bfs--dfs)
9. [Topological Sort](#9-topological-sort)
10. [Dynamic Programming](#10-dynamic-programming)
11. [Heap / Priority Queue](#11-heap--priority-queue)
12. [Backtracking](#12-backtracking)
13. [Intervals](#13-intervals)
- [Well-Known Hard Problems](#well-known-hard-problems)

## 1. Array & Hashing

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 1 | Easy | [Two Sum](https://leetcode.com/problems/two-sum/) | Find two numbers in an array that add up to a target; return their indices. |
| 217 | Easy | [Contains Duplicate](https://leetcode.com/problems/contains-duplicate/) | Determine if any value appears at least twice in the array. |
| 49 | Medium | [Group Anagrams](https://leetcode.com/problems/group-anagrams/) | Group strings that are anagrams of each other. |
| 347 | Medium | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | Return the k most frequent elements in an array. |

## 2. Two Pointers

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 125 | Easy | [Valid Palindrome](https://leetcode.com/problems/valid-palindrome/) | Check if a string is a palindrome considering only alphanumeric chars. |
| 167 | Easy | [Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/) | Find two numbers in a sorted array that add to the target (two-pointer). |
| 15 | Medium | [3Sum](https://leetcode.com/problems/3sum/) | Find all unique triplets in the array that sum to zero. |
| 11 | Medium | [Container With Most Water](https://leetcode.com/problems/container-with-most-water/) | Maximize water area between two lines using two pointers. |

## 3. Sliding Window

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 121 | Easy | [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Maximize profit from one buy/sell transaction. |
| 643 | Easy | [Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/) | Find the contiguous subarray of length k with the maximum average. |
| 3 | Medium | [Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Length of the longest substring with all distinct chars. |
| 424 | Medium | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Longest substring achievable by replacing at most k chars. |

## 4. Stack

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 20 | Easy | [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/) | Check if a string of brackets is well-formed using a stack. |
| 155 | Easy | [Min Stack](https://leetcode.com/problems/min-stack/) | Design a stack supporting push, pop, top, and getMin in O(1). |
| 150 | Medium | [Evaluate Reverse Polish Notation](https://leetcode.com/problems/evaluate-reverse-polish-notation/) | Evaluate an expression given in postfix notation. |
| 739 | Medium | [Daily Temperatures](https://leetcode.com/problems/daily-temperatures/) | Days until a warmer temperature, using a monotonic stack. |

## 5. Binary Search

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 704 | Easy | [Binary Search](https://leetcode.com/problems/binary-search/) | Standard binary search on a sorted array. |
| 278 | Easy | [First Bad Version](https://leetcode.com/problems/first-bad-version/) | Find the first bad version with a boolean API. |
| 33 | Medium | [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/) | Binary search in a rotated sorted array. |
| 153 | Medium | [Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/) | Locate the rotation point in O(log n). |

## 6. Linked List

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 206 | Easy | [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/) | Reverse a singly linked list iteratively or recursively. |
| 21 | Easy | [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/) | Merge two sorted linked lists into one sorted list. |
| 141 | Medium | [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) | Detect if a linked list has a cycle (fast/slow pointers). |
| 19 | Medium | [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/) | Remove the nth node from the end in one pass. |

## 7. Trees (Binary Tree / BST)

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 226 | Easy | [Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/) | Swap every left/right child in the tree. |
| 104 | Easy | [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/) | Compute the tree's height. |
| 102 | Medium | [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | BFS traversal returning values level by level. |
| 98 | Medium | [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/) | Check that a binary tree is a valid BST. |

## 8. Graphs (BFS / DFS)

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 733 | Easy | [Flood Fill](https://leetcode.com/problems/flood-fill/) | Paint a connected region of an image (DFS/BFS). |
| 200 | Medium* | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | Count connected groups of '1's in a grid. |
| 133 | Medium | [Clone Graph](https://leetcode.com/problems/clone-graph/) | Deep-copy an undirected graph from a given node. |
| 994 | Medium | [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | Multi-source BFS: minutes until all oranges rot. |

*#200 is often rated Medium but is a classic starter; treated here as the easy pick for graph practice.

## 9. Topological Sort

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 207 | Medium | [Course Schedule](https://leetcode.com/problems/course-schedule/) | Determine if all courses can be finished given prerequisites (cycle detection via Kahn's/DFS). |
| 210 | Medium | [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/) | Return a valid order to take all courses (topological order). |

*Note: LeetCode has no Easy-tagged topological sort problems; these two are the high-frequency standards.*

## 10. Dynamic Programming

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 70 | Easy | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/) | Count distinct ways to climb n stairs taking 1 or 2 steps. |
| 198 | Easy | [House Robber](https://leetcode.com/problems/house-robber/) | Maximize loot without robbing adjacent houses. |
| 152 | Medium | [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | Contiguous subarray with the largest product. |
| 300 | Medium | [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/) | Length of the longest strictly increasing subsequence. |

## 11. Heap / Priority Queue

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 703 | Easy | [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/) | Maintain the kth largest value as numbers stream in. |
| 1046 | Easy | [Last Stone Weight](https://leetcode.com/problems/last-stone-weight/) | Repeatedly smash the two heaviest stones (max-heap). |
| 215 | Medium | [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/) | Find the kth largest element (heap or quickselect). |
| 621 | Medium | [Task Scheduler](https://leetcode.com/problems/task-scheduler/) | Minimum intervals to finish tasks with cooldown gaps. |

## 12. Backtracking

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 78 | Medium* | [Subsets](https://leetcode.com/problems/subsets/) | Generate all subsets of a set of distinct integers. |
| 46 | Medium* | [Permutations](https://leetcode.com/problems/permutations/) | Generate all permutations of distinct integers. |
| 39 | Medium | [Combination Sum](https://leetcode.com/problems/combination-sum/) | Find combinations summing to target (reuse allowed). |
| 79 | Medium | [Word Search](https://leetcode.com/problems/word-search/) | Search for a word along grid paths (DFS + backtracking). |

*#78 and #46 are the standard backtracking starters despite their Medium tag.*

## 13. Intervals

| # | Level | Problem | Description |
|---|-------|---------|-------------|
| 228 | Easy | [Summary Ranges](https://leetcode.com/problems/summary-ranges/) | Condense a sorted array into range strings. |
| 252 | Easy | [Meeting Rooms](https://leetcode.com/problems/meeting-rooms/) | Determine if a person can attend all meetings. |
| 56 | Medium | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | Merge overlapping intervals. |
| 57 | Medium | [Insert Interval](https://leetcode.com/problems/insert-interval/) | Insert a new interval and merge where needed. |

---

## Well-Known Hard Problems

| # | Problem | Description |
|---|---------|-------------|
| 4 | [Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/) | Find the median in O(log(m+n)) via binary search partition. |
| 23 | [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/) | Merge k sorted linked lists efficiently with a heap. |
| 25 | [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/) | Reverse linked list nodes in groups of k. |
| 42 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | Compute water trapped between bar heights (two pointers / DP). |
| 124 | [Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/) | Max path sum between any two nodes in a tree. |
| 128 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) | Longest run of consecutive numbers in O(n) (hashing). |
| 212 | [Word Search II](https://leetcode.com/problems/word-search-ii/) | Find all dictionary words on the board using a Trie. |
| 239 | [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/) | Max of each window of size k (monotonic deque). |
| 297 | [Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/) | Encode/decode a binary tree to/from a string. |
| 76 | [Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/) | Smallest window in s containing all chars of t. |
