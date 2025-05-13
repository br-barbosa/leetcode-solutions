"""
Problem: Total Characters in String After Transformations I
Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-i/

Approach:
Store frequency of each letter in a list of size 26, so if there are 2 b's we assign at index 1. Then, we loop through the transitions, progressing the states according to the problem, including the transition of all z's into ab's. The length of the string is equal to the sum of all frequencies.

Time Complexity: O(n+t)
Space Complexity: O(1)
"""

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            new_count = [0] * 26
            for i in range(25):
                new_count[i + 1] = (new_count[i + 1] + count[i]) % MOD

            new_count[0] = (new_count[0] + count[25]) % MOD
            new_count[1] = (new_count[1] + count[25]) % MOD
            count = new_count

        return sum(count) % MOD
    