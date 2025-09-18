class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        #initialize diags
        for i in range(n):
            dp[i][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                if s[i] != s[j]:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                
        return dp[0][-1]
