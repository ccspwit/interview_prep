# -*- coding: utf-8 -*-
"""
Created on June 2nd, 2017
LeetCode problem 68
Given an array of words and a length L, format the text such that each line
has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words
as you can in each line. Pad extra spaces ' ' when necessary so that each
line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If
the number of spaces on a line do not divide evenly between words, the empty
slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space
is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Note: Each word is guaranteed not to exceed L in length.
@author: K Li
"""

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """Other's code, concise and clean
        How does it work? Well in the question statement, the sentence
        --Extra spaces between words should be distributed as evenly as
        --possible. If the number of spaces on a line do not divide evenly
        --between words, the empty slots on the left will be assigned more
        --spaces than the slots on the right.
        It was just a really long and awkward way to say round robin. The
        following line implements the round robin logic:
            for i in range(maxWidth - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
        """
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
    
    def fullJustify1(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        The code is working, a little long, and not very clean
        """
        def justifyLine(line, lineLen, L, lastLine = False):
            if not lastLine:
                nWords = len(line)
                if nWords==1:
                    word = line[0]
                    justified = word+" "*(L-len(word))
                else:
                    allExtraSpace = L-(lineLen-1)
                    addSpace = allExtraSpace//(nWords-1)
                    extraSpace = allExtraSpace % (nWords-1)
                    #print(line, lineLen, nWords, addSpace, extraSpace)
                    for n in range(nWords-1):
                        if n<extraSpace:
                            line[n] = line[n]+" "*addSpace+" "
                        else:
                            line[n] = line[n]+" "*addSpace
                    justified = " ".join(line)
            else:
                # last line
                justified = " ".join(line)
                justified = justified + (L-len(justified))*" "
            
            return justified
        
        N = len(words)
        L = maxWidth
        if N==0:
            return [" "*L]
        result = []
        line, lineLen = [], 0
        pos = 0
        while pos<N:
            word = words[pos]
            if (lineLen+len(word)) <= L:
                line.append(word)
                lineLen += len(word)+1
                pos += 1
                if pos == N:
                    result.append(justifyLine(line, lineLen, L, True))
            else:
                #justification for current line
                result.append(justifyLine(line, lineLen, L))
                line, lineLen = [], 0
                
        return result
    
if __name__ == '__main__':
    a = Solution()
    testVector = [([],0),([""],0),([],2),([""],2),(["",""],2),
                  (["This","is","an","example","of","text","justification."],16),
                  (["12345678901234", "This", "is", "an", "example", "of", "text", "justifi","cation."],16)]
    a = Solution()
    print("Palindrome permutation")
    for test in testVector:
        print(test)
        b = a.fullJustify(test[0],test[1])
        print(b)
        print([len(w) for w in b])
        c = a.fullJustify1(test[0],test[1])
        print(c)
        print([len(w) for w in c])