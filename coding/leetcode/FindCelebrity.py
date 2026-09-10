# -*- coding: utf-8 -*-
"""
Created on June 3rd, 2017
LeetCode problem 277
Suppose you are at a party with n people (labeled from 0 to n - 1) and among them, there may exist one celebrity. The definition of a celebrity is that all the other n - 1 people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one. The only thing you are allowed to do is to ask questions like: "Hi, A. Do you know B?" to get information of whether A knows B. You need to find out the celebrity (or verify there is not one) by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you whether A
knows B. Implement a function int findCelebrity(n), your function should
minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party. Return
the celebrity's label if there is a celebrity in the party. If there is no
celebrity, return -1.
@author: K Li
"""

# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):
def knows(a, b):
    global test
    if test[a][b] == 1:
        return True
    else:
        return False

class Solution(object): 

    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        Diagonal approach O(n) complexity
        Check for persons for people he knows and people who knows him.
        The person who knows him will not be celebrity. And if he knows a
        person, he would not be celebrity. Put non celebrity in a disqualified
        set, skip checking disqualified person.
        probably O(nlogn)
        """
        curr, next = 0, 1
        # elinimation round
        while (next<n):
            while next<n:
                if knows(curr, next)==0 and knows(next, curr)==1:
                    next += 1   # this effectively disqualify next people
                else:
                    curr, next = next, next+1

        for i in range(n):
            if i!=curr:
                if knows(i, curr)!=1 or knows(curr, i)!=0:
                    return -1
        return curr
    
    def findCelebrity2(self, n):
        """Very concise solution
        The first loop is to exclude n - 1 labels that are not possible to be
        a celebrity. After the first loop, x is the only candidate.
        The second and third loop is to verify x is actually a celebrity by
        definition. The key part is the first loop. To understand this you
        can think the knows(a,b) as a a < b comparison, if a knows b then
        a < b, if a does not know b, a > b. Then if there is a celebrity,
        he/she must be the "maximum" of the n people.
        However, the "maximum" may not be the celebrity in the case of no
        celebrity at all. Thus we need the second and third loop to check
        if x is actually celebrity by definition.
        The total calls of knows is thus 3n at most. One small improvement
        is that in the second loop we only need to check i in the range [0, x).
        You can figure that out yourself easily.
        """
        x = 0
        for i in range(n):
            if knows(x, i):
                x = i
        if any(knows(x, i) for i in range(x) if x!=i):
            return -1
        if any(not knows(i, x) for i in range(n) if x!=i):
            return -1
        return x

    def findCelebrity0(self, n):
        """
        :type n: int
        :rtype: int
        Straightforward approach with disqualification
        Check for persons for people he knows and people who knows him.
        The person who knows him will not be celebrity. And if he knows a
        person, he would not be celebrity. Put non celebrity in a disqualified
        set, skip checking disqualified person.
        probably O(nlogn)
        """
        falseSet = set()    # people who are not celebrity
        celebrity = -1
        for i in range(n):
            if i not in falseSet:
                # i not been disqualidied
                knowPeople, beingKnown = 0, 0
                for j in range(n):
                    if i==j:
                        continue

                    if knows(j,i):
                        # j knows i, j is not celebrity
                        falseSet.add(j)
                        beingKnown += 1
                    else:
                        # j does not know i, i is not celebrity
                        falseSet.add(i)
                        break
                if beingKnown != (n-1):
                    continue
                for j in range(n):
                    if i==j:
                        continue
                    if knows(i,j):
                        # i knows j, i is not celebrity
                        falseSet.add(i)
                        knowPeople += 1
                        break
                    else:
                        # i does not know j, j is no celebrity
                        falseSet.add(j)
                if (knowPeople == 0) and (beingKnown==(n-1)):
                    return i
        return celebrity

    def findCelebrity1(self, n):  
        """ 
        :type n: int 
        :rtype: int 
        """  
        i = 0  
        while i < n:  
            j = i + 1  
            while j < n and not knows(i, j):  
                j += 1  
            if j == n:  
                break  
            i = j  
              
        for k in range(n):  
            if k == i:  
                continue  
            if not knows(k, i) or knows(i, k):  
                return -1  
        return i  

if __name__ == '__main__':
	# test case to generate ListNode and run test function
    from numpy.random import randint
    testVector = [[[1]],[[0]],
                  [[1,0,0],[0,1,0],[0,0,1]],    #-1
                  [[1,0,1],[1,0,1],[0,0,0]],    #2
                  [[1,1,1],[1,1,1],[0,1,1]]]
    a = Solution()
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('The celebrity is ',a.findCelebrity(len(test)))
        print('The celebrity is ',a.findCelebrity2(len(test)))

    test = (randint(0,2,(100,100)))
    #