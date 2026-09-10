# -*- coding: utf-8 -*-
"""
Created on June 9, 2019
LeetCode problem 989
For a non-negative integer X, the array-form of X is an array of its digits in left to right order.  For example, if X = 1231, then the array form is [1,2,3,1].

Given the array-form A of a non-negative integer X, return the array-form of the integer X+K.

Example 1:
Input: A = [1,2,0,0], K = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: A = [2,7,4], K = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: A = [2,1,5], K = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Example 4:
Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
Output: [1,0,0,0,0,0,0,0,0,0,0]
Explanation: 9999999999 + 1 = 10000000000
 
Note：
1 <= A.length <= 10000
0 <= A[i] <= 9
0 <= K <= 10000
If A.length > 1, then A[0] != 0
@author: K Li
"""
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # use much less memory
        if K == 0:
            return A
        N = len(A)
        carry = K
        for n in range(N-1, -1, -1):
            carry, A[n] = divmod(A[n]+carry, 10)
        if carry:
            A = [int(n) for n in str(carry)] + A
        return A

    def addToArrayForm1(self, A: List[int], K: int) -> List[int]:
        if K == 0:
            return A
        # convert K into array form, reversed
        B = []
        while K > 0:
            B.append(K%10)
            K = K//10
        C = A[::-1]
        
        N, M = len(C), len(B)
        L = max(N, M)
        D = [0 for _ in range(L)]
        carry = 0
        curr = L-1
        for n in range(min(N, M)):
            sum = C[n] + B[n] + carry
            D[curr] = sum%10
            curr -= 1
            carry = sum//10

        if N > M:
            for n in range(M, N):
                sum = C[n] + carry
                D[curr] = sum%10
                curr -= 1
                carry = sum//10
        if N < M:
            for n in range(N, M):
                sum = B[n] + carry
                D[curr] = sum%10
                curr -= 1
                carry = sum//10
        if carry:
            return [1] + D
        else:
            return D
