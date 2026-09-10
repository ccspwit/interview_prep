# Curated LeetCode Study List — Coding Interview Prep

2–3 classic, high-frequency problems per category. Difficulty noted as E (easy) / M (medium) / H (hard).

## 1. Arrays & Hashing
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 1 | Two Sum | E | Given an array of integers and a target, return indices of the two numbers that add up to the target. |
| 49 | Group Anagrams | M | Group strings that are anagrams of each other into lists. |
| 128 | Longest Consecutive Sequence | M | Find the length of the longest run of consecutive integers in an unsorted array (O(n) expected). |

## 2. Two Pointers
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 125 | Valid Palindrome | E | Check if a string is a palindrome considering only alphanumeric characters, ignoring case. |
| 15 | 3Sum | M | Find all unique triplets in the array that sum to zero. |
| 11 | Container With Most Water | M | Pick two lines to form a container that holds the most water. |

## 3. Sliding Window
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 121 | Best Time to Buy and Sell Stock | E | Maximize profit from one buy and one sell. |
| 3 | Longest Substring Without Repeating Characters | M | Find the length of the longest substring with all distinct characters. |
| 76 | Minimum Window Substring | M | Find the smallest window in string s containing all characters of string t. |

## 4. Stack
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 20 | Valid Parentheses | E | Check if a string of brackets `()[]{}` is well-formed. |
| 155 | Min Stack | M | Design a stack supporting push, pop, top, and retrieving the minimum element in O(1). |
| 739 | Daily Temperatures | M | For each day, find how many days until a warmer temperature (monotonic stack). |

## 5. Binary Search
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 704 | Binary Search | E | Standard binary search on a sorted array. |
| 33 | Search in Rotated Sorted Array | M | Search a target in a rotated-once sorted array in O(log n). |
| 153 | Find Minimum in Rotated Sorted Array | M | Find the minimum element in a rotated sorted array in O(log n). |

## 6. Linked List
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 206 | Reverse Linked List | E | Reverse a singly linked list iteratively and recursively. |
| 141 / 142 | Linked List Cycle I / II | E / M | Detect a cycle; then find the node where the cycle begins. |
| 21 / 23 | Merge Two Sorted Lists / Merge k Sorted Lists | E / H | Merge sorted lists using pointers; then with a heap. |

## 7. Trees (Binary Tree / BST)
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 226 | Invert Binary Tree | E | Swap every node's left and right children. |
| 102 | Binary Tree Level Order Traversal | M | BFS traversal returning values level by level. |
| 98 | Validate Binary Search Tree | M | Check whether a binary tree satisfies BST ordering constraints. |

## 8. Tries
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 208 | Implement Trie (Prefix Tree) | M | Implement insert, search, and startsWith for a trie. |
| 211 | Design Add and Search Words Data Structure | M | Trie with wildcard `.` matching. |
| 212 | Word Search II | H | Find all dictionary words on a letter board using a trie + backtracking. |

## 9. Heap / Priority Queue
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 703 | Kth Largest Element in a Stream | E | Maintain the kth largest value as numbers stream in. |
| 347 | Top K Frequent Elements | M | Return the k most frequent elements in an array. |
| 295 | Find Median from Data Stream | H | Support adding numbers and querying the running median (two heaps). |

## 10. Backtracking
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 78 | Subsets | M | Generate all subsets of a set of distinct integers. |
| 46 | Permutations | M | Generate all permutations of an array of distinct integers. |
| 79 | Word Search | M | Check if a word can be traced on a letter board moving adjacently. |

## 11. Graphs (BFS / DFS / Union-Find)
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 200 | Number of Islands | M | Count connected groups of `'1'`s in a 2D grid. |
| 133 | Clone Graph | M | Deep-copy an undirected graph given a starting node. |
| 207 | Course Schedule | M | Detect cycles in prerequisites (topological sort). |

## 12. Dynamic Programming (1-D)
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 70 | Climbing Stairs | E | Count distinct ways to climb n stairs taking 1 or 2 steps. |
| 198 | House Robber | M | Maximize loot without robbing adjacent houses. |
| 322 | Coin Change | M | Fewest coins summing to an amount (unbounded knapsack variant). |

## 13. Dynamic Programming (2-D)
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 62 | Unique Paths | M | Count paths in a grid moving only right/down. |
| 1143 | Longest Common Subsequence | M | Length of the longest subsequence shared by two strings. |
| 416 | Partition Equal Subset Sum | M | Decide whether the array splits into two equal-sum subsets (0/1 knapsack). |

## 14. Intervals
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 56 | Merge Intervals | M | Merge all overlapping intervals. |
| 57 | Insert Interval | M | Insert a new interval into a sorted, non-overlapping list. |
| 435 | Non-overlapping Intervals | M | Minimum removals to make intervals non-overlapping. |

## 15. Greedy
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 53 | Maximum Subarray | M | Kadane's algorithm — largest contiguous subarray sum. |
| 55 | Jump Game | M | Decide whether you can reach the last index by jumping. |
| 134 | Gas Station | M | Find the unique starting station to complete a circular route. |

## 16. Bit Manipulation
| # | Problem | Difficulty | Description |
|---|---------|------------|-------------|
| 136 | Single Number | E | Find the element appearing once where all others appear twice (XOR). |
| 191 | Number of 1 Bits | E | Count set bits in an integer. |
| 268 | Missing Number | E | Find the missing number in [0..n] using XOR or sum. |

## Suggested Order
1–3 warm-up fundamentals → 5–7 (core patterns) → 9–11 (graph/heap) → 12–13 (DP, hardest to internalize) → remaining categories interleaved as review.
