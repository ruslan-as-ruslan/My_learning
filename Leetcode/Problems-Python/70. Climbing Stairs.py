class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3: return n

        temp, step1, step2 = 0, 1, 1
          
        for i in range(n-1):
            temp = step1
            step1 = step1 + step2
            step2 = temp
        return step1


if __name__ == "__main__":
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
