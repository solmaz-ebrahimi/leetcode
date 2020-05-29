"""
  LeetCode 
  By Solmaz Ebrahimi
 
  Longest Palindromic Substring Problem
  https://leetcode.com/problems/longest-palindromic-substring
 
  Time Submitted | Status   | Runtime | Memory | Language
  2020/05/29     | Accepted | 4372 ms	| 13.8 MB | python3
"""




class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        longest_sub = ''
        
        for i in range(len(s)):
            if (len(s) - i) < len(longest_sub):
                break
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    if len(sub) > len(longest_sub):
                        longest_sub = sub                        
        return longest_sub