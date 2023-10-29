class Solution:
    def tribonacci(self, n: int) -> int:

        if n == 0:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1        
        

        T = [0, 1, 1]
        Tn = 0

        for i in range(3, n):

            Tn = T[0] + T[1] + T[2]

            T[0], T[1], T[2] = T[1], T[2], Tn

        return T[0]+ T[1] + T[2]

    # Solution via recursion

    def tribonacci2(self, n: int) -> int:
        memo={}
        def dfs(n):
            if n in memo: return memo[n]
            if n<=0: return 0
            if n==1 or n==2: return 1
            memo[n]=res=dfs(n-1)+dfs(n-2)+dfs(n-3)
            return res
        return dfs(n)