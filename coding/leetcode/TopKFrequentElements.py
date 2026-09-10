# -*- coding: utf-8 -*-
"""
Created on June 2nd, 2017
LeetCode problem 42
Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is
the array's size.

@author: K Li
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Use Counter method most_common
        """
        from collections import Counter
        return [x[0] for x in Counter(nums).most_common(k)]

    def topKFrequent1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        First save freq count into a hash map. Then use heapq.nlargest
        """
        import heapq
        
        freqMap = {}
        for n in nums:
            freqMap[n] = freqMap.get(n, 0)+1
        result = heapq.nlargest(k, list(freqMap.items()), key=lambda x:x[1])
        print(result)
        return [r[0] for r in result]

if __name__ == '__main__':
    a = Solution()
    testVector = [#([1,2,2],1),
                  ([0,1,0,2,1,0,1,3,2,1,2,1],3),
                  ([16,3,17,10,9,12,13,6,6,7,8,13,7,16,15,8,3,6,17,7],5)]
    a = Solution()
    for test in testVector:
        print(test)
        print("Top-K elements are",(a.topKFrequent(test[0],test[1])))
    
    #test = np.random.randint(0,20,20)