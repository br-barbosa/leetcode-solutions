"""
Problem: Count Subarrays Where Max Element Appears at Least K Times
Link: https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

Approach:


Time Complexity: O(n)
Space Complexity: O(1)
"""

# First Attempt with a lot of focus on optimization
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        answer = 0
        if k > n:
            return answer

        m = max(nums)
        start = nums.index(m)
        end = start
        count = 1
        while count < k and end < n-1:
            end += 1
            if nums[end] == m:
                count += 1
        
        if count < k:
            return answer
        else:
            answer += (start)*(n - end)

        while (n - start  >= k) and (end < n):
            if count < k:
                end += 1
                if end == n:
                    break
                if nums[end] == m:
                    count += 1
            else:
                while nums[start] != m:
                    answer += (n - end)
                    start += 1
                start += 1
                answer += (n - end)
                count -= 1

        return answer
