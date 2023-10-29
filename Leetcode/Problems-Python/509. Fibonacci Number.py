'''
Solution #1  
Runtime= 684ms
Memory= 16,35 MB
'''

class Solution:
    def fib(self, n: int) -> int:       
        if n == 0: return 0
        if n == 1: return 1

        else:
            return (Solution.fib(self=Solution, n = n-1) + Solution.fib(self=Solution, n = n-2))

'''
Solution #2  
Runtime= 44 ms
Memory= 16,35 MB
'''
class Solution:
    def fib2(self, n: int) -> int:
        memo = {}
        def rec(n):
            if n in memo: return memo[n]
            if n == 0: return 0
            if n == 1: return 1
            memo[n]=res= rec(n-1) + rec(n-2)
            return res
        return rec(n)    

'''
Solution #3 
Runtime= 33ms
Memory= 16,35 MB
'''

class Solution:
    def fib3(self, n: int) -> int:

        if n == 0: return 0 
        if n == 1: return 1

        F = [0 for i in range(n+1)]
        F[1] = 1

        for i in range(2, n+1):
            Fn = F[i-1] + F[i-2]
            F[i] = Fn

        return F[n]