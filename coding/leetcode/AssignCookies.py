# -*- coding: utf-8 -*-
"""
Created on May 19, 2017
LeetCode problem 455
Assume you are an awesome parent and want to give your children some cookies.
But, you should give each child at most one cookie. Each child i has a greed
factor gi, which is the minimum size of a cookie that the child will be
content with; and each cookie j has a size sj. If sj >= gi, we can assign the
cookie j to the child i, and the child i will be content. Your goal is to
maximize the number of your content children and output the maximum number.

Note:
You may assume the greed factor is always positive. 
You cannot assign more than one cookie to one child.

Example 1:
Input: [1,2,3], [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3
children are 1, 2, 3. And even though you have 2 cookies, since their size
is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: [1,2], [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2
children are 1, 2. You have 3 cookies and their sizes are big enough to
gratify all of the children, You need to output 2.
@author: K Li
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        """N, M = len(g), len(s)
        if (N==0) | (M==0):
            return 0"""

        g.sort()
        s.sort()
        gi, N = 0, len(g)
        count = 0
        for e in s:
            if gi>=N:
                break
            else:
                if (e>=g[gi]):
                    count += 1
                    gi += 1
                    
        return count

    def findContentChildren1(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        N, M = len(g), len(s)
        if (N==0) | (M==0):
            return 0

        g.sort()
        s.sort()
        ghi, shi = N-1, M-1
        count = 0
        while (ghi>=0) & (shi>=0):
            if g[ghi]>s[shi]:
                ghi -= 1
            else:
                count += 1
                ghi -= 1
                shi -= 1
        return count
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([],[1,2,3]),([1,2,3],[1,1]),([1,2],[1,2,3]),
                  ([1,1,3,3],[2,2,4,4]),([2,2],[1,2,1,2,3]),
                  ([3,4,2,2,2],[1,2,3,4]),
                  ([1,2,3,4,5,2],[2,2,2,2,2])]
    a = Solution()
    for test in testVector:
        print(test)
        print("Number of content children is ", a.findContentChildren(test[0],test[1]))
        print("Number of content children is ", a.findContentChildren1(test[0],test[1]))
