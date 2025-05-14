"""
Problem: Total Characters in String After Transformations I
Link: https://leetcode.com/problems/total-characters-in-string-after-transformations-ii/

Approach:
Building of from Problem 3335, we build a transformation matrix to keep track of the specific transformations for each letter. Multiplying this matrix with the count vector is equivalent to 1 transformation applied to all letters. Since we have to apply this t times, it is better to complete the exponential for the matrix first, then transform directly to the final state. To avoid overflow, mods are applied at each stage and arrays are set as object.

Time Complexity: O(log t)
Space Complexity: O(1)
"""

import numpy as np

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10**9 + 7

        count = np.zeros(26, dtype=object)
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        trans_mat = np.zeros((26, 26), dtype=object)
        for j in range(26):
            for i in range(nums[j]):
                trans_mat[(i + j + 1) % 26, j] = 1

        def matrix_power_mod(mat, power, mod):
            res = np.eye(26, dtype=object)
            while power > 0:
                if power % 2 == 1:
                    res = (res @ mat) % mod
                mat = (mat @ mat) % mod
                power //= 2
            return res

        pow_mat = matrix_power_mod(trans_mat, t, MOD)
        final_count = (pow_mat @ count) % MOD
        return int(sum(final_count) % MOD)
