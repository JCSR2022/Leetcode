class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:


        MOD = 10**9+7
        m = r - l + 1
        dp = [1] * m

        for i in range(2, n + 1):
            dp = dp[::-1]
            res = 0
            for j in range(m):
                dp[j], res = res, (res + dp[j]) % MOD

        return (sum(dp) % MOD << 1) % MOD