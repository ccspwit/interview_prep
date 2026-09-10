# -*- coding: utf-8 -*-
"""
Created on May 17th, 2017
LeetCode problem 401
A binary watch has 4 LEDs on the top which represent the hours (0-11), and
the 6 LEDs on the bottom represent the minutes (0-59).
Each LED represents a zero or one, with the least significant bit on the right.

For example, the above binary watch reads "3:25".
Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.

Example:
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08",
"0:16", "0:32"]

Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid,
it should be "1:00".
The minute must be consist of two digits and may contain a leading zero,
for example "10:2" is not valid, it should be "10:02".
@author: K Li
"""

class Solution(object):
    def genMapping(self):
        # Create map of 
        hourMap = {}
        minMap = {}
        for n in range(12):
            nOnes = bin(n).count('1')
            if nOnes not in hourMap:
                hourMap[nOnes] = [str(n)]
            else:
                hourMap[nOnes].append(str(n))
        print("hourMap={")
        for key, val in hourMap.items():
            print(key, ':', val, ',')
        print("}")

        for n in range(60):
            nOnes = bin(n).count('1')
            if nOnes not in minMap:
                minMap[nOnes] = [str(n).zfill(2)]
            else:
                minMap[nOnes].append(str(n).zfill(2))
        print("minMap={")
        for key, val in minMap.items():
            print(key, ':', val, ',')
        print("}")
        
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        1. Given n, compute the combination of nHour, nMin satisfying
        nHour+nMin == n
        2. Give nHour or nMin, compute the possible values of hour or minute
        3. Use table lookup
        """
        hourMap={
        0 : ['0'] ,
        1 : ['1', '2', '4', '8'] ,
        2 : ['3', '5', '6', '9', '10'] ,
        3 : ['7', '11'] ,
        }
        minMap={
        0 : ['00'] ,
        1 : ['01', '02', '04', '08', '16', '32'] ,
        2 : ['03', '05', '06', '09', '10', '12', '17', '18', '20', '24', '33', '34', '36', '40', '48'] ,
        3 : ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50', '52', '56'] ,
        4 : ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'] ,
        5 : ['31', '47', '55', '59'] ,
        }
        times = []
        # maximal number of leds on for hour and min
        hourMax, minMax = max(hourMap.keys()), max(minMap.keys())
        for i in range(min(hourMax+1,num+1)):
            j = min(num-i, minMax)
            if (i+j)==num:
                for hr in hourMap[i]:
                    for mn in minMap[j]:
                        times.append(str(hr)+":"+str(mn))
            else:
                continue
        return times
    
if __name__ == '__main__':
	# test case to generate ListNode and run test function
    testVector = [0,1,2,3,4,5,6,7,8,9]
    a = Solution()
    print('Contains duplicate I')
    for i, test in enumerate(testVector):
        print('Test case %d-----------'%i)
        print(a.readBinaryWatch(test))

