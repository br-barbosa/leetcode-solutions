"""
Problem: Count Subarrays of Length Three With a Condition
Link: count-subarrays-of-length-three-with-a-condition

Approach:
Run simple check for all elements except first and last.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)-1):
            if nums[i] == 2*(nums[i-1] + nums[i+1]):
                count += 1
        
        return count
        