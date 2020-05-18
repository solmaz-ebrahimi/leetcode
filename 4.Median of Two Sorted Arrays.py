
"""
  LeetCode 
  By Solmaz Ebrahimi
 
  Median of Two Sorted Arrays Problem
  https://leetcode.com/problems/median-of-two-sorted-arrays/submissions
 
  Time Submitted | Status   | Runtime | Memory | Language
  2020/05/18     | Accepted | 184 ms	| 13.8 MB | python3
"""



class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums = sorted(nums1 + nums2)
        length = len(nums)
    
        if (length % 2 != 0):
            mid = nums[int(length - 1) // 2]
            return mid

        else:
            mid =float( (nums[length // 2] + nums[(length // 2) - 1]) / 2)
            return mid

