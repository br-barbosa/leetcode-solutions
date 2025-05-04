"""
Problem: Number of Equivalent Domino Pairs
Link: https://leetcode.com/problems/number-of-equivalent-domino-pairs/

Approach:
Count frequency of dominoes in a dictionary.
For each piece, count the number of possible pairs, by computing k choose 2.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = dict()
        for piece in dominoes:
            domino = "".join([str(x) for x in sorted(piece)])
            if domino in count:
                count[domino] += 1
            else:
                count[domino] = 1
        
        pairs = 0
        for value in count.values():
            pairs += (value * (value - 1)) // 2
        
        return pairs