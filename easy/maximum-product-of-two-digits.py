"""
Problem: Maximum Product of Two Digits
Link: https://leetcode.com/problems/maximum-product-of-two-digits/

Approach:
Store each digit in a list. Sort the complete list. Multiply the last two numbers in the list.

Time Complexity: O(log(n))
Space Complexity: O(log(n))
"""

class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n > 0:
            digits.append(n % 10)
            n = n // 10
        
        digits.sort()
        return digits[-2]*digits[-1]
        