from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        words = set(wordDict)

        @lru_cache(None)
        def backtrack(start):
            if start == len(s):
                return [""]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in words:
                    for suffix in backtrack(end):
                        result.append(word + (" " + suffix if suffix else ""))

            return result

        return backtrack(0)