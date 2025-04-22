"""
Problem: Reverse Integer
Link: https://leetcode.com/problems/reverse-integer/

Approach:
Store sign and work with absolute value of integer.
Manually define and check bounds for safety.
Reverse and return signed answer.

Time Complexity: O(log(n))
Space Complexity: O(1)
"""
class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x = x*sign
            
        min_int = (-2)**31
        max_int = (-1)*(min_int + 1)
        answer = 0
        while x > 0:
            digit = x % 10
            if not (min_int <= sign * (answer * 10 + digit) <= max_int):
                return 0
            answer = answer * 10 + digit
            x //= 10
        
        return sign*answer
        