"""
Problem: Longest Substring Without Repeating Characters
Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

Approach:
Store last occurrence for any seen characters.
When a repetition is found, and is within the running streak,
we log the count if higher than previous and adjust the count.

Time Complexity: O(n)
Space Complexity: O(n + m)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = {}
        highest = 0
        curr = 0
        for i, x in enumerate(s):
            if x not in hash:
                curr += 1
            else:
                if i - hash[x] > curr:
                    curr += 1
                else:
                    if curr > highest:
                        highest = curr
                    curr = i - hash[x]
            hash[x] = i
        return max(curr, highest)