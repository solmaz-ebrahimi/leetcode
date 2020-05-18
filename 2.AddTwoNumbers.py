
"""
  LeetCode 
  By Solmaz Ebrahimi
 
  Add Two Numbers Problem
  https://leetcode.com/problems/add-two-numbers
 
  Time Submitted | Status   | Runtime | Memory | Language
  2020/03/29     | Accepted | 80 ms	| 13.9 MB | python3

"""


"""
 Definition for singly-linked list.
 class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None
"""


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        num_1 = ""
        num_2 = ""
        while (l1 != None):
            num_1 += str(l1.val)
            l1 = l1.next

        while (l2 != None):
            num_2 += str(l2.val)
            l2 = l2.next

        num_1 = int(num_1[::-1])
        num_2 = int(num_2[::-1])

        sum = str(num_1 + num_2)[::-1]

        res = []
        for i in range(len(sum)):
            res.append(ListNode(int(sum[i])))

        for i in range(len(res) - 1):
            res[i].next = res[i+1]

        return res[0]
       