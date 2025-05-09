"""
Problem: Remove Element
Link: https://leetcode.com/problems/remove-element/

Approach:
Change nums in-place by removing from the list all entries equal to val.
The variable n accounts for the length of nums, which is updated when an element from the list is removed. Otherwise, we keep searching until the end of the list.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                n -= 1
            else:
                i += 1
        
        return n