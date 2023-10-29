from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)
        F = [float('inf') for _ in range(n+1)]
        F[0] = 0
        F[1] = 0

        for price in range(2, n+1):

            F[price] = min(
                cost[price - 1] + F[price - 1], 
                cost[price - 2] + F[price - 2]
            )

        return F[-1]



if __name__ == "__main__":
    assert Solution().minCostClimbingStairs(cost=[10,15,20]) == 15
    assert Solution().minCostClimbingStairs(cost=[1,100,1,1,1,100,1,1,100,1]) == 6
    assert Solution().minCostClimbingStairs(cost=[10, 15, 20, 30]) == 30

