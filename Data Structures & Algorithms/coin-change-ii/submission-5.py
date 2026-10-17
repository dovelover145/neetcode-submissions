class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        prev = [0] * (amount + 1)
        prev[0] = 1

        for i in range(len(coins) - 1, -1, -1):
            cur = [0] * (amount + 1)
            for a in range(amount + 1):
                cur[a] = prev[a]
                if a - coins[i] >= 0:
                    cur[a] += cur[a - coins[i]]
            prev = cur

        return cur[amount]
        