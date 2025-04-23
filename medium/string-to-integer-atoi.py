class Solution:
    def myAtoi(self, s: str) -> int:
        # Step 1
        s = s.strip()
        if not s:
            return 0

        min_int = -2**31
        max_int = 2**31 - 1

        # Step 2
        sign = 1
        pos = 0
        if s[0] == '-':
            sign = -1
            pos += 1
        elif s[0] == '+':
            pos += 1

        # Step 3
        answer = 0
        while pos < len(s) and s[pos].isdigit():
            digit = int(s[pos])

            # Check if next step would overflow
            if answer > (max_int - digit) // 10:
                return max_int if sign > 0 else min_int

            answer = answer * 10 + digit
            pos += 1

        return sign * answer
