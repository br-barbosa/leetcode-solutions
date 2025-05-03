"""
Problem: Minimum Domino Rotations For Equal Row
Link: https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

Approach:
The repeating number must be on the first domino, so there are two candidates.
For each candidate and each domino, we check if the number is there.
In the process, account for rotations necessary.
Return minimum number of rotations.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(candidate: int) -> int:
            rotations_top = rotations_bottom = 0
            for top, bottom in zip(tops, bottoms):
                if candidate not in {top, bottom}:
                    return -1
                elif top != candidate:
                    rotations_top += 1
                elif bottom != candidate:
                    rotations_bottom += 1
            return min(rotations_top, rotations_bottom)

        candidates = {tops[0], bottoms[0]}
        min_rotations = float('inf')
        for c in candidates:
            result = check(c)
            if result != -1:
                min_rotations = min(min_rotations, result)

        return min_rotations if min_rotations != float('inf') else -1
