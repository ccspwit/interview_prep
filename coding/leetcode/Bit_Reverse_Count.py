# -*- coding: utf-8 -*-
"""
Created on Sat May 6, 2017
LeetCode problem 190, 191 combined
---#190
Reverse bits of a given 32 bits unsigned integer.

For example, given input 43261596 (binary as 00000010100101000001111010011100)
return 964176192 (binary as 00111001011110000010100101000000).

Follow up:
If this function is called many times, how would you optimize it?

---#191
Write a function that takes an unsigned integer and returns the number
of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation
00000000000000000000000000001011, so the function should return 3.
@author: K Li
"""

class Solution(object):
    def __init__(self):
        self.eightBitTable=[
            0, 128, 64, 192, 32, 160, 96, 224, 
            16, 144, 80, 208, 48, 176, 112, 240, 
            8, 136, 72, 200, 40, 168, 104, 232, 
            24, 152, 88, 216, 56, 184, 120, 248, 
            4, 132, 68, 196, 36, 164, 100, 228, 
            20, 148, 84, 212, 52, 180, 116, 244, 
            12, 140, 76, 204, 44, 172, 108, 236, 
            28, 156, 92, 220, 60, 188, 124, 252, 
            2, 130, 66, 194, 34, 162, 98, 226, 
            18, 146, 82, 210, 50, 178, 114, 242, 
            10, 138, 74, 202, 42, 170, 106, 234, 
            26, 154, 90, 218, 58, 186, 122, 250, 
            6, 134, 70, 198, 38, 166, 102, 230, 
            22, 150, 86, 214, 54, 182, 118, 246, 
            14, 142, 78, 206, 46, 174, 110, 238, 
            30, 158, 94, 222, 62, 190, 126, 254, 
            1, 129, 65, 193, 33, 161, 97, 225, 
            17, 145, 81, 209, 49, 177, 113, 241, 
            9, 137, 73, 201, 41, 169, 105, 233, 
            25, 153, 89, 217, 57, 185, 121, 249, 
            5, 133, 69, 197, 37, 165, 101, 229, 
            21, 149, 85, 213, 53, 181, 117, 245, 
            13, 141, 77, 205, 45, 173, 109, 237, 
            29, 157, 93, 221, 61, 189, 125, 253, 
            3, 131, 67, 195, 35, 163, 99, 227, 
            19, 147, 83, 211, 51, 179, 115, 243, 
            11, 139, 75, 203, 43, 171, 107, 235, 
            27, 155, 91, 219, 59, 187, 123, 251, 
            7, 135, 71, 199, 39, 167, 103, 231, 
            23, 151, 87, 215, 55, 183, 119, 247, 
            15, 143, 79, 207, 47, 175, 111, 239, 
            31, 159, 95, 223, 63, 191, 127, 255]
        return

    def reverseBitsCalc(self, n):
        """
        @param n, an integer
        @return an integer
        """
        if n<0:
            return 0
        # try brute force
        num = n
        result = 0
        for i in range(32):
            curLSB = num&1
            num = num>>1
            result = result<<1
            result += curLSB
        return result

    def reverseBits(self, n):
        """
        @param n, an integer
        @return an integer
        Lookup 8-bit mapping table
        """
        if n<0:
            return 0
        # try brute force
        num = n
        result = 0
        for i in range(4):
            curLSB = num&255
            num = num>>8
            result = result<<8
            result += self.eightBitTable[curLSB]
        return result

    def reverseBitsTable(self):
        def reverseBits8(n):
            """
            @param n, an integer
            @return an integer
            """
            if n<0:
                return 0
            # try brute force
            num = n
            result = 0
            for i in range(8):
                curLSB = num&1
                num = num>>1
                result = result<<1
                result += curLSB
            return result
        for n in range(256):
            print('%d, '%(reverseBits8(n)), end='')
            if (n%8)==7:
                print()

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        Use the n&(n-1) to clear the least significant '1'
        """
        
        weight = 0
        while n!=0:
            weight += 1
            n &= (n-1)
        return weight

if __name__ == '__main__':
    a = Solution()
    testVector = [1,5,10,20,30,100,255,1000]
                  
    a = Solution()
    for tc, test in enumerate(testVector):
        print('-----Test case %d-----'%tc)
        #print(test)
        print("%d, bit reversed %d"%(test, a.reverseBits(test)))
        print("%d, bit reversed %d"%(test, a.reverseBitsCalc(test)))
        
        print('The number of bits for %d is %d'%(test, a.hammingWeight(test)))

    print('Generating table')
    #a.reverseBitsTable()