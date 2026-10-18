
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = n - 1 - i

            for j in range(i, n):
                if s[i] == s[j] and (
                    j - i <= 2 or pal[i + 1][j - 1]
                ):
                    pal[i][j] = True

                    if j == n - 1:
                        dp[i] = 0
                    else:
                        dp[i] = min(dp[i], 1 + dp[j + 1])

        return dp[0]
