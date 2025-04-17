"""
Problem: Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/

Approach:
Read through linked lists with recursion.
Manipulate between str and int for efficiency.
Return the result in linked list format.

Time Complexity: O(n + m)
Space Complexity: O(n + m)
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def getInt(self, node: Optional[ListNode]) -> int:
        power = 0
        total = 0
        while node:
            total += node.val*(10**power)
            node = node.next
            power += 1
        return total

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = self.getInt(l1) + self.getInt(l2)

        dummy = ListNode(0)
        curr = dummy

        if result == 0:
            return dummy

        while result > 0:
            curr.next = ListNode(result % 10)
            curr = curr.next
            result //= 10

        return dummy.next
