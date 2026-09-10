# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 2017
LeetCode problem 12, 13
---#12
Given an integer, convert it to a roman numeral.
Input is guaranteed to be within the range from 1 to 3999.

---#13
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

@author: K Li
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        if (num<=0) | (num>3999):
            return ""
        roman = {1000:'M',
                 500:'D',
                 100:'C',
                 50:'L',
                 10:'X',
                 5:'V',
                 1:'I'}
        #TH = [k for k in roman]
        #Threshold
        TH = [1000, 500, 100, 50, 10, 5, 1]

        result = ""
        while num>=TH[0]:    #>=1000
            num -= TH[0]
            result += roman[TH[0]]
        for i in range(1,len(TH),2):
            thHigh = TH[i-1]    #10X
            thMid = TH[i]       #5X
            thLow = TH[i+1]     #1X
            if num>=(thHigh-thLow):
                # 9X < n < 10 X
                num -= (thHigh-thLow)
                result += (roman[TH[i+1]]+roman[TH[i-1]])
            else:
                # n < 9X
                if num >= thMid:
                    # n > 5X
                    num -= thMid
                    result += roman[TH[i]]
                    while num>=thLow:
                        num -= TH[i+1]
                        result += roman[TH[i+1]]
                elif num >= (thMid - thLow):
                    # n > 4X
                    num -= (thMid-thLow)
                    result += (roman[TH[i+1]]+roman[TH[i]])
                else:
                    # n < 4X
                    while num>=thLow:
                        num -= TH[i+1]
                        result += roman[TH[i+1]]
            #endif
        #end for loop
        return result

    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        Cleaner and more straightforward solution
        """
        roman = {'M':1000,
                 'D':500,
                 'C':100,
                 'L':50,
                 'X':10,
                 'V':5,
                 'I':1}

        num = 0
        for ind in range(len(s)-1):
            d1 = roman[s[ind]]
            d2 = roman[s[ind+1]]
            if(d1<d2):  # case of IV/IX/XL/XC/CD/CM
                num -= d1
            else:   # case of 
                num += d1        
        # process last digit if exist
        num += roman[s[-1]]
        return num

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        mapping = {'M':1000,
                    'D':500,
                    'C':100,
                    'L':50,
                    'X':10,
                    'V':5,
                    'I':1}
        N = len(s)

        retVal = 0
        ind = 0
        while ind < (N-1):
            d1 = mapping[s[ind]]
            d2 = mapping[s[ind+1]]
            if(d1<d2):  # case of IV/IX/XL/XC/CD/CM
                retVal += (d2-d1)
                ind += 2
            else:   # case of 
                retVal += d1
                ind += 1
        
        # process last digit if exist
        if ind <N:
            retVal += mapping[s[ind]]
        return retVal

if __name__ == '__main__':
    a = Solution()
    testVector = [('MMDCCC',2800), ('MCM',1900),
            ('XCIX',99), ('XCVIII',98),
            ('VIII',8), ('V',5), ('IV',4), ('I',1)]
    for test in testVector:
        x = test[0]
        y = a.romanToInt(test[0])
        z = a.intToRoman(y)
        
        print('Roman={}, int={}, roman={}'.format(test[0], y, z))

    for n in range(1,4000):
        x = a.intToRoman(n)
        y = a.romanToInt(x)
        if y!=n:
            print('Error, n={}, roman={}, back to int ={}'.format(n,x,y))