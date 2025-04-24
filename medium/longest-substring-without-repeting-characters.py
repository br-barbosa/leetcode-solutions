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
    
# Afterward, I see that a more traditional application of 
# sliding window would be cleaner and make for a better code
# to work on if more was need to be developed on top of this project

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        start = 0
        max_len = 0

        for i, c in enumerate(s):
            if c in char_index and char_index[c] >= start:
                # Repeat found, move the start to the right of the last occurrence
                start = char_index[c] + 1
            # Update the last seen index of the character
            char_index[c] = i
            # Update max length if needed
            max_len = max(max_len, i - start + 1)

        return max_len