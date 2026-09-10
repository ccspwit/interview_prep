# -*- coding: utf-8 -*-
"""
Created on May 30, 2017
LeetCode problem 49
Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[ ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]]
Note: All inputs will be in lower-case.
@author: K Li
"""
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        use an array of counts as key
        """
        groupMap = {}
        for s in strs:
            counts = [0] * 26 
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)
            if key not in groupMap:
                groupMap[key] = [s]
            else:
                groupMap[key].append(s)

        return groupMap.values()

    def groupAnagrams1(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        use sorted(string) as key
        """
        groupMap = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in groupMap:
                groupMap[key] = [s]
            else:
                groupMap[key].append(s)

        return [val for val in groupMap.values()]
    
if __name__ == '__main__':
    a = Solution()
    testVector = [[""],["","a"],
                  ["eat", "tea", "tan", "ate", "nat", "bat"]]
    a = Solution()
    print("Minimal characters to delete")
    for test in testVector:
        #print(test)
        print("%s = %s"%(test, a.groupAnagrams(test)))
