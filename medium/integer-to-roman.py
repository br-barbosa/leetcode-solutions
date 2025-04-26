"""
Problem: Palindrome Number
Link: https://leetcode.com/problems/integer-to-roman/

Approach:
Create hash table including subtractive forms.
From bigger to smaller, check how many times each number fits
into the number, then decrease it by that much. 

Time Complexity: O(1)
Space Complexity: O(1)
"""

class Solution:
    def intToRoman(self, num: int) -> str:
        val_to_roman = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]
        
        result = []
        
        for value, symbol in val_to_roman:
            count = num // value
            result.append(symbol * count)
            num -= value * count
        
        return ''.join(result)