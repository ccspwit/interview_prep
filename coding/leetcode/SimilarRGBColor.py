# -*- coding: utf-8 -*-
"""
Created on Jan 28, 2020
LeetCode problem 800
In the following, every capital letter represents some hexadecimal digit from 0 to f.
The red-green-blue color "#AABBCC" can be written as "#ABC" in shorthand.  For example, "#15c" is shorthand for the color "#1155cc".
Now, say the similarity between two colors "#ABCDEF" and "#UVWXYZ" is -(AB - UV)^2 - (CD - WX)^2 - (EF - YZ)^2.
Given the color "#ABCDEF", return a 7 character color that is most similar to #ABCDEF, and has a shorthand (that is, it can be represented as some "#XYZ"

Example 1:
Input: color = "#09f166"
Output: "#11ee66"
Explanation:  
The similarity is -(0x09 - 0x11)^2 -(0xf1 - 0xee)^2 - (0x66 - 0x66)^2 = -64 -9 -0 = -73.
This is the highest among any shorthand color.

Note:
color is a string of length 7.
color is a valid RGB color: for i > 0, color[i] is a hexadecimal digit from 0 to f
Any answer which has the same (highest) similarity as the best answer will be accepted.
All inputs and outputs should use lowercase letters, and the output is 7 characters.
@author: K Li
"""
class Solution:
    def similarRGB(self, color):
        def f(comp):
            q, r = divmod(int(comp, 16), 17)
            if r > 8: q += 1
            return '{:02x}'.format(17 * q)

        return '#' + f(color[1:3]) + f(color[3:5]) + f(color[5:])

    def similarRGB1(self, color: str) -> str:
        # find nearest neighbor by brute force
        def nearest_hex(hex2):
            if hex2[0]==hex2[1]:
                return hex2
            elif hex2[0]<hex2[1]:
                # 09 - 00, 11
                low = hex2[0] * 2
                next_hex = "{:x}".format((int(hex2[0], 16)+1) % 16)
                high = next_hex*2
                if (int(high, 16)-int(hex2, 16)) > (int(hex2, 16) - int(low, 16)):
                    return low
                else:
                    return high
            else:
                # 91 - 99, 88
                high = hex2[0] * 2
                prev_hex = "{:x}".format((int(hex2[0], 16)+15) % 16)
                low = prev_hex*2
                if (int(high, 16)-int(hex2, 16)) > (int(hex2, 16) - int(low, 16)):
                    return low
                else:
                    return high
        res = []
        for n in range(3):
            hex_2 = color[n*2+1:n*2+3]
            res.append(nearest_hex(hex_2))
        # print(res)
        return '#'+''.join(res)
        