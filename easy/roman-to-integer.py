"""
Problem: Palindrome Number
Link: https://leetcode.com/problems/roman-to-integer/

Approach:
First solution that came to mind, simply compare from left to right.
When the a smaller number appears before a bigger one, add their difference
to the total, otherwise add the value.
Last value treated separately at the end.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        answer = 0
        n = len(s)
        i = 0
        while i < n-1:
            current = roman[s[i]]
            upcoming = roman[s[i+1]]
            if current >= upcoming:
                answer += current
                i += 1
            else:
                answer += upcoming - current
                i += 2
        
        if i < n:
            answer += roman[s[n-1]]

        return answer