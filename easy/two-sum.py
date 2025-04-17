"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/

Approach:
Create a sorted list to make for a faster search.
Search target from beginning and end of sorted list.
Find position in the initial list, avoiding returning [x,x].

Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        a = 0
        b = len(nums)-1
        while True:
            value_1 = nums_sorted[a]
            value_2 = nums_sorted[b]
            sum = value_1 + value_2
            if sum == target:
                break
            elif sum > target:
                b -= 1
            else:
                a += 1
        
        x = nums.index(value_1)
        if value_1 != value_2:
            y = nums.index(value_2)
        else:
            y = nums[x+1:].index(value_2)+x+1

        return [x,y]