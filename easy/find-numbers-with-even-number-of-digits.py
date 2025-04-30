"""
Problem: Find Numbers with Even Number of Digits
Link: https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

Approach:
Changing each integer into a string and check for even length.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for x in nums:
            if len(str(x)) % 2 == 0:
                count += 1
        
        return count