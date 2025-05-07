"""
Problem: Longest Common Prefix
Link: https://leetcode.com/problems/longest-common-prefix/

Approach:
Start assuming the first word as the prefix.
Trim it down as needed after comparing with each next word.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1,len(strs)):
            str_len = len(strs[i])
            for j, char in enumerate(prefix):
                if j >= str_len or strs[i][j] != char:
                    prefix = prefix[:j]
                    break
        
        return prefix