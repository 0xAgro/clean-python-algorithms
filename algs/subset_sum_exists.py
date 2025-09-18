class Solution:
    def canPartition(self, A: List[int]) -> bool:
        if sum(A) % 2:
            return False

        dp = [[0]*(len(A) + 1) for _ in range(sum(A) + 1)]
        for j in range(len(dp[0])):
            dp[0][j] = 1
        
        for j in range(1, len(dp[0])):
            for i in range(1, len(dp)):
                if i >= A[j - 1]:
                    dp[i][j] = dp[i - A[j - 1]][j - 1]
                if not dp[i][j]:
                    dp[i][j] = dp[i][j - 1]

        return bool(dp[sum(A) // 2][-1])
