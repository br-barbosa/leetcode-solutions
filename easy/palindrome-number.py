"""
Problem: Palindrome Number
Link: https://leetcode.com/problems/palindrome-number/

Approach:
Remove edge case of negative numbers.
Create a list with each digit.
Check left and right corresponding digits for equality.

Time Complexity: O(log(n))
Space Complexity: O(log(n))
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            # From Example 2, negative numbers are not palindromes
            return False

        # Store digits in a list
        digits = []
        while x > 0:
            digits.append(x % 10)
            x //= 10
        
        # Check left and right corresponding digits
        left = 0
        right = len(digits)-1
        while left <= right:
            if digits[left] != digits[right]:
                return False
            left += 1
            right -= 1
        return True

# Second Approach avoiding lists
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Extra edge case added
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = 10*reversed_half + x % 10
            x //= 10
        
        # Checking match for even and odd number of digits
        return x == reversed_half or x == reversed_half // 10
