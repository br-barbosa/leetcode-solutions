"""
Problem: Longest Unequal Adjacent Groups Subsequence I
Link: https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

Approach:
Since elements in the subsequence don't have to be consecutive, we start with the first element in the list, and search for the next word in the other group. Once found, we have the next word for the subsequence, and the process repeats.

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        output = [words[0]]
        current_group = groups[0]
        for i in range(1,len(words)):
            new_group = groups[i]
            if new_group != current_group:
                current_group = new_group
                output.append(words[i])
        
        return output
