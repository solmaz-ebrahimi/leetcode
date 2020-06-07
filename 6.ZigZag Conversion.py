"""
  LeetCode 
  By Solmaz Ebrahimi
 
  ZigZag Conversion Problem
  https://leetcode.com/problems/zigzag-conversion
 
  Time Submitted | Status   | Runtime | Memory  | Language
  2020/06/07     | Accepted | 60 ms	| 13.7 MB | python3
"""




class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        data = ['' for x in range(numRows)]
        down = False
        i = 0
        
        for item in s:
            data[i] = data[i] + item
            if i == 0 or i == numRows-1:
                down = not down
            i = i + 1 if down else i-1
            
        out = ''
        for char in data:
            if char != '':
                out = out + char
        return out