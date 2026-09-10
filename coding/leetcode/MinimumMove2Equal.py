# -*- coding: utf-8 -*-
"""
Created on May 19, 2017
LeetCode problem 453, 462 combined
---#453
Given a non-empty integer array of size n, find the minimum number of moves
required to make all array elements equal, where a move is incrementing
n - 1 elements by 1.

Example:

Input:
[1,2,3]
Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

---#462
Given a non-empty integer array, find the minimum number of moves required
to make all array elements equal, where a move is incrementing a selected
element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.
Example:

Input:
[1,2,3]
Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one
element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
@author: K Li
"""

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Find median as mid point value. There are equal number of elements
        less than median value than elements larger than it.
        Assume m=N//2, and suppose mid = median+1, then to reach this new
        mid point, we add m+1 increment, and reduce m-1 decrease. At least
        two more moves. Same reasoning for mid smaller than median.
        """
        def median(nums):
            """
            O(nlogn) method: sort+indexing
            We might use quick select to find median. Average O(n) complexity,
            but worst case is O(n^2)
            """
            N = len(nums)
            if N == 0:
                return []
            nums.sort()
            if N&1:
                return nums[N//2]
            else:
                return (nums[N//2-1]+nums[N//2])/2.0

        N = len(nums)
        if N == 0:
            return 0
        mid = int(median(nums))
        return sum([abs(x-mid) for x in nums])
        """
        if N&1:
            mid = median(nums)
            return sum([abs(x-mid) for x in nums])
        else:
            mid = median(nums)
            mid1 = int(mid)
            mid2 = mid1+1
            print(mid,mid1,mid2)
            return (sum([abs(x-mid1) for x in nums]),sum([abs(x-mid2) for x in nums]))
        """

    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Mathematical solutions, there are two ways to look at it
        1. Add '1' to n-1 elements is equivalent to deduct '1' from 1 element.
        Then problem becomes how many times we need to do '-1' to make all
        elements equals to minimal value: m = sum(nums)-minimum*N
        2. Look at addition: add n-1 M times to reach equalibrium
            SUM + M(n-1) = xN, assume x = MIN+M
            we have SUM - M = MIN*N, which is M = SUM - MIN*N (same as above)
        """
        N = len(nums)
        if N<=1:
            return 0
        return sum(nums) - min(nums)*N
        
if __name__ == '__main__':
    import numps as np
	# test case to generate ListNode and run test function
    testVector = [[],[1],[1,1],[2,2],
                  [1,8,9,9],
                  [1,1,2,2]]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        test1 = test[:]
        print('The minimal number of move (1) is : ',a.minMoves(test))
        print('The minimal number of move (2) is : ',a.minMoves2(test))

    tc = np.random.randint(1,100,20)