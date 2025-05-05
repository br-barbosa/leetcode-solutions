"""
Problem: Domino and Tromino Tiling
Link: https://leetcode.com/problems/domino-and-tromino-tiling/

Approach:
Compute the possibilities for the base cases n = 1, 2, 3.
Increase step by step the board and count possibilities.
There is a special case for the tromino, where you can add a piece on the left and another on the right, with the middle portion being unbalanced.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def numTilings(self, n: int) -> int:        
        mod = 10**9 + 7
        dp = [0] * (n+1)
        dp[0], dp[1], dp[2], dp[3] = 1, 1, 2, 5

        for i in range(4, n+1):
            dp[i] = (2 * dp[i-1] + dp[i-3]) % mod
        
        return dp[n]