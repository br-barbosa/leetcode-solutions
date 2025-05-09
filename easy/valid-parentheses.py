"""
Problem: Remove Element
Link: https://leetcode.com/problems/valid-parentheses/

Approach:
Stack new parenthesis on a list, and remove then as corresponding closing ones come up. In case of a closing parentheses showing up out of turn return False. If the stack is empty at the end return True.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in brackets.values():
                stack.append(char)
            elif len(stack) > 0 and stack[-1] == brackets[char]:
                stack.pop()
            else:
                return False
        
        return len(stack) == 0