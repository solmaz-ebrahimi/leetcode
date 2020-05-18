
"""
  LeetCode 
  By Solmaz Ebrahimi
 
  Longest Substring Without Repeating Characters Problem
  https://leetcode.com/problems/longest-substring-without-repeating-characters/
 
  Time Submitted | Status   | Runtime | Memory | Language
  2020/05/13     | Accepted | 68 ms   | 14 MB  | python3

"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        word = []
        k = 0
        for char in s:
             if char in word:
                 s = word.index(char)
                 word = word[(s+1):]
             word.append(char)
             if len(word) > k:
                 k = len(word)
        return k