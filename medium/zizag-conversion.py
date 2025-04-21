"""
Problem: Zigzag Conversion
Link: https://leetcode.com/problems/zigzag-conversion/

Approach:
Using a list, distribute characters among rows according to the
zigzag pattern using modulo.
Merge all characters into a string.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        char = [ [] for _ in range(numRows)]
        if numRows == 1 or numRows >= len(s):
            return s
        for i, c in enumerate(s):
            row = i % (2*(numRows-1))
            if row >= numRows:
                row = (2*(numRows-1)) - row
            char[row].append(c)
        return ''.join([item for sublist in char for item in sublist])