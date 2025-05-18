# Input: m = 1, n = 1
# Output: 3
# Explanation: The three possible colorings are shown in the image above.
class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        from itertools import product

        # Generate all valid column patterns
        def is_valid(col):
            return all(col[i] != col[i+1] for i in range(len(col) - 1))

        colors = [0, 1, 2]  # 0 = red, 1 = green, 2 = blue
        all_patterns = [p for p in product(colors, repeat=m) if is_valid(p)]

        # Precompute which patterns are compatible
        neighbors = {}
        for p1 in all_patterns:
            neighbors[p1] = []
            for p2 in all_patterns:
                if all(x != y for x, y in zip(p1, p2)):
                    neighbors[p1].append(p2)

        # DP initialization
        dp = {p: 1 for p in all_patterns}

        for _ in range(n - 1):
            new_dp = {p: 0 for p in all_patterns}
            for p in all_patterns:
                for nei in neighbors[p]:
                    new_dp[nei] = (new_dp[nei] + dp[p]) % MOD
            dp = new_dp

        return sum(dp.values()) % MOD