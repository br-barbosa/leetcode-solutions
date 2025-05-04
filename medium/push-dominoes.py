"""
Problem: Push Dominoes
Link: https://leetcode.com/problems/push-dominoes

Approach:
Two-pass approach, where we check the influence of "R"
dominoes from left to right, which propagates over "."
and stops at "L". Then, repeat from the other side for "L".
After the fact, it is a matter of balancing the two forces.

Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        force = 0

        for i in range(n):
            if dominoes[i] == 'R':
                force = n
            elif dominoes[i] == 'L':
                force = 0
            else:
                force = max(force - 1, 0)

            forces[i] += force

        for i in reversed(range(n)):
            if dominoes[i] == 'L':
                force = n
            elif dominoes[i] == 'R':
                force = 0
            else:
                force = max(force - 1, 0)

            forces[i] -= force

        result = []
        for f in forces:
            if f > 0:
                result.append('R')
            elif f < 0:
                result.append('L')
            else:
                result.append('.')

        return "".join(result)
