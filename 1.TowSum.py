
"""
  LeetCode 
  By Solmaz Ebrahimi
 
  Two Sum Problem
  https://leetcode.com/problems/two-sum
 
  Time Submitted | Status   | Runtime | Memory | Language
  2020/03/22     | Accepted | 7068 ms	| 14 MB | python3

"""




class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-i):
                if nums[i] + nums[j+i] == target:
                    if i != j+i:
                        return [i,j+i]
                    
                    
