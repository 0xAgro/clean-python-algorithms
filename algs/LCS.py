def longestCommonSubsequence(self, T1, T2):
  dp = [[0]*(len(T1) + 1) for _ in range(len(T2) + 1)]

  for i in range(1, len(dp)):
    for j in range(1, len(dp[0])):
      if T1[j - 1] == T2[i - 1]:
        dp[i][j] = dp[i - 1][j - 1] + 1
      else:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

  return dp[-1][-1]
