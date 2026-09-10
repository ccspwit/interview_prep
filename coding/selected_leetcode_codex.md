# Selected LeetCode Problems for Coding Round Preparation

Curated, high-frequency LeetCode problems organized by data structure and algorithmic pattern. Each core category contains **2 Easy + 2 Medium** problems. Categories where LeetCode has few or no Easy-tagged problems (Topological Sort, Backtracking, Trie, Union-Find, Intervals) are clearly noted and list Medium problems instead. A final section lists well-known Hard problems.

## Table of Contents
1. [Array](#array)
2. [String](#string)
3. [Two Pointers](#two-pointers)
4. [Sliding Window](#sliding-window)
5. [Stack](#stack)
6. [Queue](#queue)
7. [Linked List](#linked-list)
8. [Hash Map / Set](#hash-map-set)
9. [Binary Search](#binary-search)
10. [Sorting](#sorting)
11. [Binary Tree / BST](#binary-tree-bst)
12. [Heap / Priority Queue](#heap-priority-queue)
13. [Graph (BFS/DFS)](#graph)
14. [Topological Sort](#topological-sort)
15. [Dynamic Programming](#dynamic-programming)
16. [Greedy](#greedy)
17. [Matrix](#matrix)
18. [Intervals](#intervals)
19. [Backtracking](#backtracking)
20. [Trie](#trie)
21. [Union-Find (Disjoint Set)](#union-find)
22. [Bit Manipulation](#bit-manipulation)
- [Well-Known Hard Problems](#hard-problems)
- [Additional High-Frequency Problems](#bonus-practice)

## How to Use This List
- Start with the data structures you are weakest in.
- Solve Easy problems first as warm-ups, then move to Medium.
- For each Medium/Hard problem, explain the approach out loud, then state time and space complexity.
- Re-attempt problems a few days later without notes (spaced repetition).
- Links go to LeetCode. Sides of LeetCode marked Premium may require a subscription.

---

<a id="array"></a>
## 1. Array

#### Easy
- **[1. Two Sum](https://leetcode.com/problems/two-sum/)** — Easy — Return the indices of the two numbers that add up to a target.
- **[217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)** — Easy — Return `true` if any value appears at least twice.

#### Medium
- **[238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)** — Medium — Return an array where each element is the product of all other elements without using division.
- **[31. Next Permutation](https://leetcode.com/problems/next-permutation/)** — Medium — Rearrange numbers into the lexicographically next greater permutation in-place.

<a id="string"></a>
## 2. String

#### Easy
- **[242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)** — Easy — Determine if two strings are anagrams of each other.
- **[14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/)** — Easy — Find the longest common prefix shared by all strings in an array.

#### Medium
- **[5. Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/)** — Medium — Return the longest palindromic substring in a string.
- **[151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/)** — Medium — Reverse the order of words while removing extra whitespace.

<a id="two-pointers"></a>
## 3. Two Pointers

#### Easy
- **[125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)** — Easy — Check whether a string is a palindrome after ignoring non-alphanumeric characters and case.
- **[392. Is Subsequence](https://leetcode.com/problems/is-subsequence/)** — Easy — Determine whether one string is a subsequence of another.

#### Medium
- **[11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)** — Medium — Find two lines that, together with the x-axis, form a container holding the most water.
- **[15. 3Sum](https://leetcode.com/problems/3sum/)** — Medium — Find all unique triplets that sum to zero.

<a id="sliding-window"></a>
## 4. Sliding Window

#### Easy
- **[121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)** — Easy — Find the maximum profit from a single buy and a single sell.
- **[643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)** — Easy — Find the contiguous subarray of length `k` with the maximum average.

#### Medium
- **[3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)** — Medium — Find the length of the longest substring without repeating characters.
- **[424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)** — Medium — After at most `k` replacements, find the longest substring of all identical characters.

<a id="stack"></a>
## 5. Stack

#### Easy
- **[20. Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)** — Easy — Check whether a string of brackets `(){}[]` is valid.
- **[155. Min Stack](https://leetcode.com/problems/min-stack/)** — Easy — Design a stack supporting push, pop, top, and retrieving the minimum element in constant time.

#### Medium
- **[739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)** — Medium — For each day, return how many days you must wait until a warmer temperature.
- **[394. Decode String](https://leetcode.com/problems/decode-string/)** — Medium — Decode an encoded string with nested repetition rules such as `3[a2[c]]`.

<a id="queue"></a>
## 6. Queue

#### Easy
- **[232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)** — Easy — Implement a FIFO queue using two stacks.
- **[933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)** — Easy — Return the number of valid requests within the last 3,000 milliseconds.

#### Medium
- **[622. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/)** — Medium — Design a fixed-size circular queue.
- **[752. Open the Lock](https://leetcode.com/problems/open-the-lock/)** — Medium — Find the minimum number of turns to unlock a combination lock using BFS over states.

<a id="linked-list"></a>
## 7. Linked List

#### Easy
- **[206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)** — Easy — Reverse a singly linked list iteratively and recursively.
- **[21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)** — Easy — Merge two sorted linked lists into one sorted list.

#### Medium
- **[2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)** — Medium — Add two numbers represented by linked lists in reverse digit order.
- **[19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)** — Medium — Remove the nth node from the end of a linked list in one pass.

<a id="hash-map-set"></a>
## 8. Hash Map / Set

#### Easy
- **[387. First Unique Character in a String](https://leetcode.com/problems/first-unique-character-in-a-string/)** — Easy — Find the index of the first non-repeating character.
- **[350. Intersection of Two Arrays II](https://leetcode.com/problems/intersection-of-two-arrays-ii/)** — Easy — Return the intersection of two arrays, including duplicate counts.

#### Medium
- **[49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)** — Medium — Group strings that are anagrams of each other.
- **[128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)** — Medium — Find the length of the longest consecutive elements sequence in an unsorted array.

<a id="binary-search"></a>
## 9. Binary Search

#### Easy
- **[704. Binary Search](https://leetcode.com/problems/binary-search/)** — Easy — Implement classic binary search on a sorted array.
- **[278. First Bad Version](https://leetcode.com/problems/first-bad-version/)** — Easy — Find the first bad version among `n` versions using the given API.

#### Medium
- **[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)** — Medium — Search for a target in a rotated sorted array in `O(log n)` time.
- **[153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)** — Medium — Find the minimum element in a rotated sorted array.

<a id="sorting"></a>
## 10. Sorting

#### Easy
- **[88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/)** — Easy — Merge two sorted arrays into the first array in non-decreasing order.
- **[977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)** — Easy — Return the squares of each number in sorted order.

#### Medium
- **[75. Sort Colors](https://leetcode.com/problems/sort-colors/)** — Medium — Sort an array of 0s, 1s, and 2s in place (Dutch National Flag).
- **[148. Sort List](https://leetcode.com/problems/sort-list/)** — Medium — Sort a linked list in `O(n log n)` time using merge sort.

<a id="binary-tree-bst"></a>
## 11. Binary Tree / BST

#### Easy
- **[226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)** — Easy — Invert a binary tree by swapping left and right children at every node.
- **[104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)** — Easy — Return the maximum depth of a binary tree.

#### Medium
- **[98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)** — Medium — Determine whether a binary tree is a valid BST.
- **[102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)** — Medium — Return the level-by-level traversal of a binary tree.

<a id="heap-priority-queue"></a>
## 12. Heap / Priority Queue

#### Easy
- **[1046. Last Stone Weight](https://leetcode.com/problems/last-stone-weight/)** — Easy — Repeatedly smash the two heaviest stones until one or none remain.
- **[703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)** — Easy — Return the kth largest element in a stream.

#### Medium
- **[215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)** — Medium — Find the kth largest element in an unsorted array.
- **[347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)** — Medium — Return the `k` most frequent elements.

<a id="graph"></a>
## 13. Graph (BFS/DFS)

#### Easy
- **[733. Flood Fill](https://leetcode.com/problems/flood-fill/)** — Easy — Perform a flood fill on an image starting from a given pixel.
- **[1971. Find if Path Exists in Graph](https://leetcode.com/problems/find-if-path-exists-in-graph/)** — Easy — Determine whether a valid path exists between two vertices.

#### Medium
- **[200. Number of Islands](https://leetcode.com/problems/number-of-islands/)** — Medium — Count the number of connected islands in a 2D grid.
- **[994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)** — Medium — Find the minimum time for all oranges to rot using multi-source BFS.

<a id="topological-sort"></a>
## 14. Topological Sort

> Note: High-frequency topological sort problems are almost all Medium/Hard on LeetCode. The two listed here are the canonical entry points.

- **[207. Course Schedule](https://leetcode.com/problems/course-schedule/)** — Medium — Detect whether all courses can be finished given prerequisite pairs (cycle detection / topological order).
- **[210. Course Schedule II](https://leetcode.com/problems/course-schedule-ii/)** — Medium — Return a valid ordering of courses using Kahn's algorithm or DFS.
- **[310. Minimum Height Trees](https://leetcode.com/problems/minimum-height-trees/)** — Medium — Find the roots that minimize the height of a tree-like graph (topological peeling).

<a id="dynamic-programming"></a>
## 15. Dynamic Programming

#### Easy
- **[70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)** — Easy — Count distinct ways to climb `n` stairs taking 1 or 2 steps at a time.
- **[53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)** — Easy — Find the contiguous subarray with the largest sum.

#### Medium
- **[198. House Robber](https://leetcode.com/problems/house-robber/)** — Medium — Maximize money robbed from non-adjacent houses.
- **[322. Coin Change](https://leetcode.com/problems/coin-change/)** — Medium — Find the fewest coins needed to make a given amount.

<a id="greedy"></a>
## 16. Greedy

#### Easy
- **[860. Lemonade Change](https://leetcode.com/problems/lemonade-change/)** — Easy — Determine whether you can provide correct change to every customer.
- **[455. Assign Cookies](https://leetcode.com/problems/assign-cookies/)** — Easy — Maximize the number of children who can be satisfied with cookies.

#### Medium
- **[55. Jump Game](https://leetcode.com/problems/jump-game/)** — Medium — Determine whether you can reach the last index using maximum jump lengths.
- **[134. Gas Station](https://leetcode.com/problems/gas-station/)** — Medium — Find the starting gas station index to complete a full circuit.

<a id="matrix"></a>
## 17. Matrix

#### Easy
- **[867. Transpose Matrix](https://leetcode.com/problems/transpose-matrix/)** — Easy — Return the transpose of a matrix.
- **[566. Reshape the Matrix](https://leetcode.com/problems/reshape-the-matrix/)** — Easy — Reshape a matrix to given row and column dimensions.

#### Medium
- **[48. Rotate Image](https://leetcode.com/problems/rotate-image/)** — Medium — Rotate an `n x n` matrix by 90 degrees in place.
- **[54. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/)** — Medium — Return all elements of a matrix in spiral order.

<a id="intervals"></a>
## 18. Intervals

> Note: Free Easy-tagged interval problems are rare, so the core interval patterns below are all Medium.

- **[56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)** — Medium — Merge all overlapping intervals.
- **[57. Insert Interval](https://leetcode.com/problems/insert-interval/)** — Medium — Insert a new interval into a sorted list and merge if needed.
- **[435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)** — Medium — Find the minimum number of intervals to remove so the rest do not overlap.
- **[986. Interval List Intersections](https://leetcode.com/problems/interval-list-intersections/)** — Medium — Compute the intersection of two lists of intervals.

<a id="backtracking"></a>
## 19. Backtracking

> Note: LeetCode has very few high-frequency Easy-tagged backtracking problems. The standard entry points are Medium.

#### Entry points
- **[78. Subsets](https://leetcode.com/problems/subsets/)** — Medium — Generate all subsets of a set.
- **[22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)** — Medium — Generate all combinations of well-formed parentheses.

#### High-frequency Medium
- **[46. Permutations](https://leetcode.com/problems/permutations/)** — Medium — Generate all permutations of a list of distinct numbers.
- **[39. Combination Sum](https://leetcode.com/problems/combination-sum/)** — Medium — Find all unique combinations that sum to a target.

<a id="trie"></a>
## 20. Trie

> Note: Most useful trie problems are Medium or Hard; Easy-tagged trie problems are uncommon.

- **[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)** — Medium — Implement `insert`, `search`, and `startsWith` for a trie.
- **[211. Design Add and Search Words Data Structure](https://leetcode.com/problems/design-add-and-search-words-data-structure/)** — Medium — Design a word dictionary supporting `add` and search with the `.` wildcard.
- **[648. Replace Words](https://leetcode.com/problems/replace-words/)** — Medium — Replace words with their shortest matching root in a dictionary.
- **[212. Word Search II](https://leetcode.com/problems/word-search-ii/)** — Hard — Find all dictionary words present in a 2D board (trie + backtracking).

<a id="union-find"></a>
## 21. Union-Find (Disjoint Set)

> Note: Union-Find problems are almost always Medium or Hard; no high-frequency Easy problems exist.

- **[684. Redundant Connection](https://leetcode.com/problems/redundant-connection/)** — Medium — Find the edge that creates a cycle in an undirected graph.
- **[547. Number of Provinces](https://leetcode.com/problems/number-of-provinces/)** — Medium — Count connected components among cities.
- **[721. Accounts Merge](https://leetcode.com/problems/accounts-merge/)** — Medium — Merge accounts that share common emails.
- **[130. Surrounded Regions](https://leetcode.com/problems/surrounded-regions/)** — Medium — Flip enclosed `O` regions surrounded by `X` (union-find or DFS/BFS).

<a id="bit-manipulation"></a>
## 22. Bit Manipulation

#### Easy
- **[136. Single Number](https://leetcode.com/problems/single-number/)** — Easy — Find the one number that appears once while every other number appears twice.
- **[191. Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)** — Easy — Count the number of set bits in an integer.

#### Medium
- **[371. Sum of Two Integers](https://leetcode.com/problems/sum-of-two-integers/)** — Medium — Add two integers without using `+` or `-`.
- **[201. Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/)** — Medium — Compute the bitwise AND of all numbers in a range.

---

<a id="hard-problems"></a>
## Well-Known Hard Problems
- **[4. Median of Two Sorted Arrays](https://leetcode.com/problems/median-of-two-sorted-arrays/)** — Hard — Find the median of two sorted arrays in `O(log(m+n))` time.
- **[23. Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)** — Hard — Merge k sorted linked lists into one (heap or divide and conquer).
- **[42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)** — Hard — Compute how much water can be trapped between bars.
- **[76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/)** — Hard — Find the minimum window in `s` that contains all characters of `t`.
- **[84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)** — Hard — Find the largest rectangle area in a histogram (monotonic stack).
- **[124. Binary Tree Maximum Path Sum](https://leetcode.com/problems/binary-tree-maximum-path-sum/)** — Hard — Find the maximum path sum between any two nodes in a binary tree.
- **[295. Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)** — Hard — Support dynamic median queries using two heaps.
- **[297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)** — Hard — Design serialization and deserialization for a binary tree.

---

<a id="bonus-practice"></a>
## Additional High-Frequency Problems Worth Noting
- [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/) — Medium — prefix sum + hash map
- [146. LRU Cache](https://leetcode.com/problems/lru-cache/) — Medium — hash map + doubly linked list
- [973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/) — Medium — heap
- [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/) — Easy — Floyd's cycle detection
- [105. Construct Binary Tree from Preorder and Inorder Traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/) — Medium — tree construction
