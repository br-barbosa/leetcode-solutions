"""
Problem: Finding 3-Digit Even Numbers
Link: https://leetcode.com/problems/finding-3-digit-even-numbers/

Approach:
Count the frequency of digits in the list, then check all 3-digit numbers to see which could be written with the digits available in the list, given their frequency.

Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 != 0:
                continue

            c = Counter(str(num))
            if all(count[int(d)] >= c[d] for d in c):
                result.append(num)

        return result


# Initial Process

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        hash_table = [0]*10
        for digit in digits:
            hash_table[digit] += 1

        digits.sort()
        output = []
        
        for units in [0,2,4,6,8]:
            if hash_table[units] > 0:
                u_index = digits.index(units)

                for h_index, hunds in enumerate(digits):
                    if h_index == u_index or hunds == 0:
                        continue
                    for t_index, tens in enumerate(digits):
                        if t_index == h_index or t_index == u_index:
                            continue
                        combination = hunds * 100 + tens * 10 + units
                        if combination not in output:
                            output.append(combination)
        
        return sorted(output)