# -*- coding: utf-8 -*-
"""
Created on June 14, 2019
LeetCode problem 1041
On an infinite plane, a robot initially stands at (0, 0) and faces north.  The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degress to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

Example 1:
Input: "GGLLGG"
Output: true
Explanation: 
The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.

Example 2:
Input: "GG"
Output: false
Explanation: 
The robot moves north indefinitely.

Example 3:
Input: "GL"
Output: true
Explanation: 
The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 
Note:
1 <= instructions.length <= 100
instructions[i] is in {'G', 'L', 'R'}
@author: K Li
"""
import math
class Solution(object):
    def isRobotBounded(self, instructions):
        """
        :type instructions: str
        :rtype: bool
        """
        x, y, angle = 0, 0, 90
        for i in instructions:
            if i == 'G':
                x += round(math.cos(angle*math.pi/180))
                y += round(math.sin(angle*math.pi/180))
            if i == 'L':
                angle = (angle + 90) % 360
            if i == 'R':
                angle = (angle - 90) % 360
        
        # print(x, y, angle)
        return (x==0 and y==0) or (angle != 90)
