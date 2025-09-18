def isPalindrome(self, s):
        n = len(s)
        dp = [[0]*n for _ in range(n)]

        #initialize diags
        for i in range(n):
            dp[i][i] = 1
            if i != n - 1:
                dp[i + 1][i] = 1

        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = int((s[i] == s[j]) and dp[i+1][j-1])

        return dp
