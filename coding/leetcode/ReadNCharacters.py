# -*- coding: utf-8 -*-
"""
Created on May 31, 2017
LeetCode problem 157
The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read. For example, it
returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n)
that reads n characters from the file.

Note:
The read function will only be called once for each test case.
@author: K Li
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
buf = [""]*1024

string=""*1024
size = len(string)
ptr = 0

def read4(block):
    global string, size, ptr
    rem = size - ptr
    if(rem>=4):
        block[:] = string[ptr:ptr+4]
        ptr+=4
        return 4
    else:
        block[:] = string[ptr:ptr+rem]
        ptr+=rem
        return rem            

#read4 = Buffer.read4
class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        index = 0
        block = [""]*4
        while n>0:
            size = read4(block)
            toRead = min(n,4)
            if (toRead==4)&(size==4):
                for i in range(size):
                    buf[index] = block[i]
                    index += 1
                n -= 4
            else:
                #print(size, toRead)
                M = min(toRead, size)
                for i in range(M):
                    buf[index] = block[i]
                    index += 1
                    n -= M
                break
            #print(index, n)
                
        return index            

if __name__ == '__main__':
    a = Solution()
    testVector = [("0",1),("2",2),("123",1),
                  ("abcde",5),("1234567890",12)]
    a = Solution()
    print("Multiply strings...")
    for test in testVector:
        print(test)
        string=test[0]
        size = len(string)
        ptr = 0
        n=a.read(buf,test[1])
        print(n, '---',buf[:n])
