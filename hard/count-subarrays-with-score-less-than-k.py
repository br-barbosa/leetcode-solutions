"""
Problem: Count Subarrays With Score Less Than K
Link: https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

Approach:
Create a prefix sum.
Then for each starting point, binary search for first subsequent index
for which the score is invalid.
The count is updated for all the valid endpoints.

Time Complexity: O(nlog(n))
Space Complexity: O(n)
"""

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0] * (n+1)
        for i in range(n):
            pref[i+1] = pref[i] + nums[i]

        count = 0

        for i in range(n):
            low = i
            high = n

            while low < high:
                mid = (low + high) // 2
                total = pref[mid+1] - pref[i]
                length = mid - i + 1
                if total * length < k:
                    low = mid + 1
                else:
                    high = mid

            count += low - i

        return count


# Initial O(n**2) attempt
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pref = [0]*n
        pref[0] = nums[0]
        for i in range(1,n):
            pref[i] = pref[i-1] + nums[i]

        print(pref)
        count = 0
        for i in range(n-1):
            if nums[i] < k:
                count += 1                
            else:
                continue

            if i > 0:
                previous = pref[i-1]
            else:
                previous = 0

            j = i+1
            while j < n and (pref[j] - previous)*(j - i + 1) < k:
                count += 1
                j += 1

        if nums[-1] < k:
            count += 1

        return count
