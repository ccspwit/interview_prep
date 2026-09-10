# -*- coding: utf-8 -*-
"""
Created on May 30, 2017
LeetCode problem 243, 244, 245 combined
---#243
Given a list of words, write a method that takes two words and returns
the shotest between those two words.
For example,
list of words:
    ['the','quick','fox','brown','fox','quick']
    distance("fox","the") is 3
    distance("quick", "fox") is 1

---#244

---#245
This is a follow up of Shortest Word Distance. The only difference is now
word1 could be the same as word2.

Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

word1 and word2 may be the same and they represent two individual words in
the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Given word1 = “makes”, word2 = “coding”, return 1.
Given word1 = "makes", word2 = "makes", return 3.
@author: K Li
"""

class Solution(object):
    def shortestDistance(self, l, w1, w2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        Return the minimal distance between two words in the list
        """
        #What if does not find the word?
        N = len(l)
        pos1, pos2 = -1, -1
        minDist = N
        for ind, ele in enumerate(l):
            if ele == w1:
                pos1 = ind
                if pos2 != -1:
                    minDist = min((pos1-pos2), minDist)
            if ele == w2:
                pos2 = ind
                if pos1 != -1:
                    minDist = min((pos2-pos1), minDist)                
        return minDist

    def shortestWordDistance(self, words, w1, w2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        w1 and w2 could be identical
        Tackle both cases of w1==w2 and w1!=w2
        """
        N = len(words)
        prev, dist = -1, N

        for curr, word in enumerate(words):
            if word in (w1, w2):
                if prev != -1 and (w1 == w2 or w1 != w2 and word != words[prev]):
                    dist = min(dist, curr-prev)# or curr-prev
                prev = curr

        return dist if dist<N else -1
        
    def shortestWordDistance1(self, words, w1, w2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        w1 and w2 could be identical
        Consider two separate cases for w1!=w2 and w1==s2. Easier to understand
        """
        N = len(words)
        minDist = N
        if w1 != w2:
            p1, p2 = -1, -1
            for ind, ele in enumerate(words):
                if ele==w1:
                    p1 = ind
                    if p2!=-1:
                        minDist = min(minDist, ind-p2)
                if ele==w2:
                    p2 = ind
                    if p1!=-1:
                        minDist = min(minDist, ind-p1)
        else:
            lastPos = -1
            for ind, ele in enumerate(words):
                if (ele==w1):
                    if lastPos!=-1:
                        minDist = min(minDist, ind-lastPos)
                    lastPos = ind
        
        return minDist if minDist<N else -1

class WordDistance(object):
    def __init__(self, words):
        """
        :type words: List[str]
        Use hash map to store position of occurances for each words
        """
        self.posMap = {}
        for i, w in enumerate(words):
            if w not in self.posMap:
                self.posMap[w] = [i]
            else:
                self.posMap[w].append(i)
        #print(self.posMap)
        return
    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if word1==word2:
            return 0
        minDist = 2147483647
        pos1 = self.posMap.get(word1, [])
        pos2 = self.posMap.get(word2, [])
        if (not pos1) or (not pos2):
            return minDist
        N1, N2 = len(pos1), len(pos2)
        p1, p2 = 0, 0
        while (p1<N1) and (p2<N2):
            if pos1[p1]<pos2[p2]:
                minDist = min(minDist, pos2[p2]-pos1[p1])
                p1 += 1
            else:   #pos1[p1]>pos2[p2]
                minDist = min(minDist, pos1[p1]-pos2[p2])
                p2 += 1
            #print(p1,p2,N1,N2)
            if minDist==1:
                break
        return minDist
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [(['the','quick','brown','fox','quick'],"fox","the"),
                  (['the','quick','brown','fox','quick'],"quick","fox"),
                  (["practice","makes","perfect","coding","makes"],"coding","practice")]
    a = Solution()
    print("Shortest word distance I")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Minimal distance is %d.'%(a.shortestDistance(test[0], test[1], test[2])))

    testVector = [(["a","c","a","a"],"a","a"),
                  (["the","quick","brown","fox","quick"],"fox","the"),
                  (["the","quick","brown","fox","quick"],"fox","fox"),
                  (["practice","makes","perfect","coding","makes"],"coding","practice"),
                  (["practice","makes","perfect","coding","makes"],"makes","makes")]
    print("\nShortest word distance III")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        print('Minimal distance is %d.'%(a.shortestWordDistance(test[0], test[1], test[2])))
        print('Minimal distance is %d.'%(a.shortestWordDistance1(test[0], test[1], test[2])))

    print("\nShortest word distance II")
    testVector = [(["a","c","a","a"],"a","a"),
                  (["the","quick","brown","fox","quick"],"fox","the"),
                  (["the","quick","brown","fox","quick"],"fox","quick"),
                  (["practice","makes","perfect","coding","makes"],"coding","practice"),
                  (["practice","makes","perfect","coding","makes"],"makes","coding")]
    print("\nShortest word distance III")
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(test)
        b = WordDistance(test[0])
        print('Minimal distance is %d.'%(b.shortest(test[1], test[2])))