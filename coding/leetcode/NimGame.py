# -*- coding: utf-8 -*-
"""
Created on May 15th, 2017
LeetCode problem 292
You are playing the following Nim Game with your friend: There is a heap of
stones on the table, each time one of you take turns to remove 1 to 3 stones.
The one who removes the last stone will be the winner. You will take the
first turn to remove the stones.

Both of you are very clever and have optimal strategies for the game. Write
a function to determine whether you can win the game given the number of
stones in the heap.

For example, if there are 4 stones in the heap, then you will never win the
game: no matter 1, 2, or 3 stones you remove, the last stone will always be
removed by your friend.
@author: K Li
"""

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return (n%4)!=0
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [1,2,3,4,5,6,7,8,9,99,100]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print(test, 'Win' if a.canWinNim(test) else 'Lose')

