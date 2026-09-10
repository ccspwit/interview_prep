# -*- coding: utf-8 -*-
"""
Created on June 1 2019
LeetCode problem 93
Given a string containing only digits, restore it by returning
all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
@author: K Li
"""
class Solution(object):
    def restoreIpAddresses_pos(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid_length(N, k):
            return (N>=k) and (N<=3*k)

        N = len(s)
        if not valid_length(N, 4):
            return []
        results = []
        segment = 0
        len_comb = []
        stack = [(0, [])]
        
        # compute possible valid combination of 4 position
        while stack:
            k, comb = stack.pop()
            if k==4:
                pos = [0]+comb
                ip = []
                for n in range(k):
                    seg = s[pos[n]:pos[n+1]]
                    if (int(seg)<=255) and (seg[0]!='0' or (seg[0]=='0' and len(seg)==1)):
                        ip.append(seg)
                    else:
                        continue
                if len(ip)==4:
                    results.append('.'.join(ip))
            # ip field length 1/2/3
            for l in range(1,4):
                if k==0:
                    if valid_length(N-l, 4-k-1):
                        #print(N-l, 4-k-1)
                        stack.append((k+1, [l]))
                else:
                    if valid_length(N-comb[-1]-l, 4-k-1):
                        #print(N-comb[-1]-l, 4-k-1)
                        stack.append((k+1, comb+[comb[-1]+l]))

        return results
    
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def valid(segment):
            """
            Check if the current segment is valid :
            1. less or equal to 255      
            2. the first character could be '0' 
               only if the segment is equal to '0'
            """
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1
            
        def update_output(curr_pos):
            """
            Append the current list of segments 
            to the list of solutions
            """
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()    
            
        def backtrack(prev_pos = -1, dots = 3):
            """
            prev_pos : the position of the previously placed dot
            dots : number of dots to place
            """
            # The current dot curr_pos could be placed 
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed 
            # after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot
        
        n = len(s)
        output, segments = [], []
        backtrack()
        return output
