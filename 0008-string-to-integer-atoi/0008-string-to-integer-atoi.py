class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        # 32-bit integer limits
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1

        # 1. Ignore leading spaces
        while i < n and s[i] == ' ':
            i += 1

        # 2. Check sign
        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        # 3. Convert digits manually
        number = 0

        while i < n and '0' <= s[i] <= '9':
            digit = ord(s[i]) - ord('0')
            number = number * 10 + digit

            # 4. Check overflow
            if sign * number < INT_MIN:
                return INT_MIN

            if sign * number > INT_MAX:
                return INT_MAX

            i += 1

        return sign * number