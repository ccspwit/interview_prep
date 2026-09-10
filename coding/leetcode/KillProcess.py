# -*- coding: utf-8 -*-
"""
Created on May 27, 2017
LeetCode problem 582
Given n processes, each process has a unique PID (process id) and its PPID
(parent process id).

Each process only has one parent process, but may have one or more children
processes. This is just like a tree structure. Only one process has PPID
that is 0, which means this process has no parent process. All the PIDs will
be distinct positive integers.

We use two list of integers to represent a list of processes, where the first
list contains PID for each process and the second list contains the
corresponding PPID.

Now given the two lists, and a PID representing a process you want to kill,
return a list of PIDs of processes that will be killed in the end. You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.

Example 1:
Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.
Note:
The given kill id is guaranteed to be one of the given PIDs.
n >= 1.
@author: K Li
"""

class Solution(object):
    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        # create parent:child mapping
        p2cMap = {}
        for child, parent in zip(pid,ppid):
            if parent not in p2cMap:
                p2cMap[parent] = [child]
            else:
                p2cMap[parent].append(child)
        #print(p2cMap)
        result = []
        if kill in pid:
            stack = [kill]
        else:
            raise KeyError('Invalid processID %d to kill'%kill)
        
        while stack:
            p = stack.pop()
            result.append(p)
            if p in p2cMap:
                stack.extend(p2cMap[p])
        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([1],[0],1),([1,2,3],[0,1,1],1),
                  ([1,3,10,5],[3,0,5,3],5),
                  ([1,3,10,5,6,7],[3,0,5,3,10,5],5)]
    a = Solution()
    for test in testVector:
        print(test)
        print("Minimal radius is ", a.killProcess(test[0],test[1],test[2]))
        #print("Minimal radius is ", a.findRadius2(test[0],test[1]))
