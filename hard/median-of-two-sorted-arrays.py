"""
Problem: Median of Two Sorted Arrays
Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

Approach:
Binary search over smaller list to partition lists.
The partition should be such that the left contains basically half the elements,
for the combined lists and everything on the left is smaller or equal to the
elements on the right.

Time Complexity: O(log(m + n))
Space Complexity: O(1)
"""

# First attempt
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        merged_array = sorted(nums1)
        size = len(merged_array)
        if size % 2 == 1:
            return merged_array[size//2]
        else:
            return (merged_array[size//2] + merged_array[size//2 - 1])/2

# Final attempt attending the running time requirements
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            left1  = nums1[i - 1] if i > 0 else float("-inf")
            right1 = nums1[i]     if i < m else float("inf")
            left2  = nums2[j - 1] if j > 0 else float("-inf")
            right2 = nums2[j]     if j < n else float("inf")

            if left1 <= right2 and left2 <= right1:
                if (m + n) % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                high = i - 1
            else:
                low = i + 1
