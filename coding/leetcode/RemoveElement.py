# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 2017
LeetCode problem 27

Given an array and a value, remove all instances of that value in place and
return the new length. Do not allocate extra space for another array,
you must do this in place with constant memory.
The order of elements can be changed. It doesn't matter what you leave beyond
the new length.

Example:
Given input array nums = [3,2,2,3], val = 3
Your should return length = 2, with the first two elements of nums being 2.

@author: K Li
"""

# Definition for singly-linked list.
class Solution(object):
    def removeElement(self, nums, val):
        # REALLY NEAT reference solution, way much concise than my solution.
        # Two pointers, left pointer scans for matches, when found,
        # replace with value of right pointer
        # until left pointer pass right pointer.
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start +=1
        return start

    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        My solution, left point scans for match while right pointer
        scans for nonmatch. If leftPointer <= rightPointer, matched element
        will be replaced with unmatched element. Update both pointer by one
        in opposite direction.
        """
        
        if not nums:
            return 0
        N = len(nums)
        
        matchInd, nonmatchInd = 0, N-1
        
        while (matchInd <= nonmatchInd):
            while (matchInd<=nonmatchInd):
                if (nums[matchInd]==val):
                    #matchFound = True
                    break
                else:
                    matchInd += 1
                    
            while (nonmatchInd>=matchInd):
                if(nums[nonmatchInd]!=val):
                    #nonmatchFound = True
                    break;
                else:
                    nonmatchInd -= 1
            #print(matchInd, nonmatchInd)
            if(matchInd<nonmatchInd):
                nums[matchInd] = nums[nonmatchInd]
                matchInd += 1
                nonmatchInd -= 1
            else:
                break

        return nonmatchInd+1

    def removeElement0(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        My solution, left point scans for match while right pointer
        scans for nonmatch. left value was replaced by right value.
        """
        
        if not nums:
            return 0
        N = len(nums)
        
        matchInd, nonmatchInd = 0, N-1
        
        matchFound, nonmatchFound = False, False
        
        while (matchInd<N) & (nonmatchInd>=0):
            while (matchInd<N):
                if (nums[matchInd]==val):
                    matchFound = True
                    break
                else:
                    matchInd += 1
                    
            while (nonmatchInd>=0):
                if(nums[nonmatchInd]!=val):
                    nonmatchFound = True
                    break;
                else:
                    nonmatchInd -= 1
            #print(matchInd, nonmatchInd)
            #break
            if not matchFound or not nonmatchFound:
                continue
            if(matchInd<nonmatchInd):
                nums[matchInd] = nums[nonmatchInd]
                matchInd += 1
                nonmatchInd -= 1
            else:
                break

        return nonmatchInd+1

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    import numpy.random as random
    testVector = [([0,0,1,0,2,0],0),
                  ([0,0,0,1,2,0,3,4,5],0),
                  ([0,0,0,0,1,2],0),
                  ([1,2,3,4,5],0),
                  ([0,0,0],0),
                  ([],3)]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        test0 = test[0].copy()
        n = a.removeElement(test[0], test[1])
        print(test[0][:n])
        n = a.removeElement1(test0, test[1])
        print(test0[:n])
    test = sorted(random.randint(0,100,1000))
    test0 = test.copy()
