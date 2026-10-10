class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        
        if not s:
            return False

        seen_digit = False
        seen_dot = False
        seen_exponent = False

        for i, char in enumerate(s):
            if char.isdigit():
                seen_digit = True

            elif char == '.':
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True

            elif char in 'eE':
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False

            elif char in '+-':
                if i > 0 and s[i - 1] not in 'eE':
                    return False

            else:
                return False

        return seen_digit