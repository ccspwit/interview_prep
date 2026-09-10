# -*- coding: utf-8 -*-
"""
Created on May 25, 2017
LeetCode problem 551, 552 combined
---#551
You are given a string representing an attendance record for a student. The
record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than
one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his
attendance record.

Example 1:
Input: "PPALLP"
Output: True
Example 2:
Input: "PPALLL"
Output: False

---#552
Given a positive integer n, return the number of all possible attendance
records with length n, which will be regarded as rewardable. The answer may
be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following
three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A'
(absent) or more than two continuous 'L' (late).

Example 1:
Input: n = 2
Output: 8 
Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.

@author: K Li
"""

class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        Dynamic Programming Solution
        Limit intermediate results to be within 1000000007 significantly reduce
        time.
        """
        if n<=0:
            return 1
        if n==1:
            return 3
        if n==2:
            return 8
        a_0l = 3
        a_1l = 1
        a_2l = 0
        noa_0l = 2
        noa_1l = 1
        noa_2l = 1
        for i in range(3,n+1):
            tmp1 = (noa_0l+noa_1l+noa_2l)%1000000007
            tmp2 = (a_0l+a_1l+a_2l)%1000000007
            a_0l, a_1l, a_2l = ((tmp1+tmp2), # add 'A' or 'P'
                                a_0l,   # add 'A' or 'L'
                                a_1l)   # add 'A' or 'L'
            noa_0l, noa_1l, noa_2l = ((tmp1), # add 'P'
                                      (noa_0l),    # add 'L'
                                      (noa_1l))   # add 'L'
            #print(a_0l,a_1l,a_2l,noa_0l,noa_1l,noa_2l)
        return (a_0l+a_1l+a_2l+noa_0l+noa_1l+noa_2l)%(1000000007)

    def checkRecord1(self, n):
        if n == 1:
            return 3
        if n == 0:
            return 0
        nums = [1, 1, 2]
        i = 2
        while i < n:
            nums.append((nums[i] + nums[i-1] + nums[i-2])% 1000000007)
            i += 1
        result = (nums[n] + nums[n-1] + nums[n-2]) % 1000000007
        for i in range(n):
            result += nums[i+1] * nums[n-i] % 1000000007
            result %= 1000000007
        return result
        
    def checkRecordI(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        if N<=1:
            return True

        s = s.upper()
        cntA = 0
        for ind, ch in enumerate(s):
            if ch=='A':
                cntA += 1
                if cntA>1:
                    return False
            elif (ch=='L') and (ind>=2):
                if ch==s[ind-1]==s[ind-2]:
                    return False
        return True

    def checkRecordI2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        if N<=1:
            return True

        s = s.upper()
        cntA = 0
        consecL = 0
        lastL = 0
        for n in range(N):
            if s[n]=='A':
                cntA += 1
                lastL = 0
                if cntA>1:
                    return False
            elif s[n]=='L':
                if lastL == 0:
                    consecL = 1
                    lastL = 1
                else:
                    consecL += 1
                if consecL>2:
                    return False
            else:
                lastL = 0

        return True

    def checkRecordI1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        N = len(s)
        if N<=1:
            return True

        s = s.upper()
        if s.count('A')>1:
            return False
        if 'LLL' in s:
            return False

        return True
    
if __name__ == '__main__':
    a = Solution()
    testVector = ["","Aa","PPALLP","PPALLPA","PPALLL","PPLLALL"]
    a = Solution()
    for test in testVector:
        print(test)
        print("%s -- %s"%(test, a.checkRecordI(test)))
        print("%s -- %s"%(test, a.checkRecordI1(test)))


    testVector = [0,1,2,3,4,99999]
    print("\nReverse string II")
    for test in testVector:
        print(test)
        print("# of rewardable attendance records is %d"%(a.checkRecord(test)))
        print("# of rewardable attendance records is %d"%(a.checkRecord1(test)))

