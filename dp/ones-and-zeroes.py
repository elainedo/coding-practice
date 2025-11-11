from typing import List, Tuple

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        def count_zeros_ones(s: str) -> Tuple[int, int]:
            zeros = s.count('0')
            ones = len(s) - zeros
            return zeros, ones

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            z, o = count_zeros_ones(s)
            # iterate backwards to ensure 0/1 choice
            for i in range(m, z - 1, -1):
                for j in range(n, o - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - z][j - o] + 1)

        return dp[m][n]