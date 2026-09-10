# -*- coding: utf-8 -*-
"""
Created on May 28, 2017
LeetCode problem 599
Suppose Andy and Doris want to choose a restaurant for dinner, and they both
have a list of favorite restaurants represented by strings. You need to help
them find out their common interest with the least list index sum. If there
is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
@author: K Li
"""

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        N, M = len(list1), len(list2)
        if (N==0) or (M==0):
            return []
        
        map1 = {ele:ind for ind, ele in enumerate(list1)}

        minSum = N+M        
        map2 = []
        for ind, ele in enumerate(list2):
            indexSum = ind+map1.get(ele,1000000000)
            if indexSum < minSum:
                minSum = indexSum
                map2 = [ele]
            elif indexSum == minSum:
                map2.append(ele)
        return map2

    def findRestaurant1(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        N, M = len(list1), len(list2)
        if (N==0) or (M==0):
            return []
        
        map1, map2 = {},[]
        for ind, ele in enumerate(list1):
            map1[ele] = ind
        minSum = N+M
        
        for ind, ele in enumerate(list2):
            if ele in map1:
                indexSum = ind+map1[ele]
                if indexSum < minSum:
                    minSum = indexSum
                    map2 = [ele]
                elif indexSum == minSum:
                    map2.append(ele)
        return map2
        
if __name__ == '__main__':
    a = Solution()
    testVector = [([],["a"]),([""],["a"]),
                  (["Shogun", "Tapioca Express", "Burger King", "KFC"],
                   ["KFC", "Shogun", "Burger King"]),
                  (["Shogun","Tapioca Express","Burger King","Piatti","KFC"],
                   ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"])]
    a = Solution()
    print("Minimal characters to delete")
    for test in testVector:
        print(test)
        print(a.findRestaurant(test[0],test[1]))
        print(a.findRestaurant1(test[0],test[1]))
