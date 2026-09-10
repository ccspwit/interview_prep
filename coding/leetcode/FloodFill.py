# -*- coding: utf-8 -*-
"""
Created on June 6, 2019
LeetCode problem 733
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: 
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535]
@author: K Li
"""
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        # recursive method is more effective
        # be careful of case color=newColor
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r-1, c)
                if r+1 < R: dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < C: dfs(r, c+1)

        dfs(sr, sc)
        return image

    def floodFillLoop(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        N, M = len(image), len(image[0])
        if N==1 and M==1:
            image[0][0] = newColor
            return image
        # no need to check out of range
        fill_val = -1-image[sr][sc]
        image[sr][sc] = fill_val
        # fill Q1
        for row in range(sr, -1, -1):
            for col in range(sc, M, 1):
                last_row = min(row+1, sr)
                next_row = max(row-1, 0)
                last_col = max(col-1, sc)
                next_col = min(col+1, M-1)
                # print((last_row, col), (next_row, col), (row, last_col), (row, next_col))
                if image[row][col] == fill_val:
                    if (image[last_row][col]==-1-fill_val):
                        image[last_row][col] = fill_val
                    if (image[next_row][col]==-1-fill_val):
                        image[next_row][col] = fill_val
                    if (image[row][last_col]==-1-fill_val):
                        image[row][last_col] = fill_val
                    if (image[row][next_col]==-1-fill_val):
                        image[row][next_col] = fill_val
        # fill Q2
        for row in range(sr, -1, -1):
            for col in range(sc, -1, -1):
                last_row = min(row+1, sr)
                next_row = max(row-1, 0)
                last_col = min(col+1, sc)
                next_col = max(col-1, 0)
                if image[row][col] == fill_val:
                    if (image[last_row][col]==-1-fill_val):
                        image[last_row][col] = fill_val
                    if (image[next_row][col]==-1-fill_val):
                        image[next_row][col] = fill_val
                    if (image[row][last_col]==-1-fill_val):
                        image[row][last_col] = fill_val
                    if (image[row][next_col]==-1-fill_val):
                        image[row][next_col] = fill_val
        # fill Q3
        for row in range(sr, N, 1):
            for col in range(sc, -1, -1):
                last_row = max(row-1, sr)
                next_row = min(row+1, N-1)
                last_col = min(col+1, sc)
                next_col = max(col-1, 0)
                if image[row][col] == fill_val:
                    if (image[last_row][col]==-1-fill_val):
                        image[last_row][col] = fill_val
                    if (image[next_row][col]==-1-fill_val):
                        image[next_row][col] = fill_val
                    if (image[row][last_col]==-1-fill_val):
                        image[row][last_col] = fill_val
                    if (image[row][next_col]==-1-fill_val):
                        image[row][next_col] = fill_val
        # fill Q4
        for row in range(sr, N):
            for col in range(sc, M):
                last_row = max(row-1, sr)
                next_row = min(row+1, N-1)
                last_col = max(col-1, sc)
                next_col = min(col+1, M-1)
                if image[row][col] == fill_val:
                    if (image[last_row][col]==-1-fill_val):
                        image[last_row][col] = fill_val
                    if (image[next_row][col]==-1-fill_val):
                        image[next_row][col] = fill_val
                    if (image[row][last_col]==-1-fill_val):
                        image[row][last_col] = fill_val
                    if (image[row][next_col]==-1-fill_val):
                        image[row][next_col] = fill_val

        # fill newColor
        for r in range(N):
            for c in range(M):
                if image[r][c] == fill_val:
                    image[r][c] = newColor
        return image
