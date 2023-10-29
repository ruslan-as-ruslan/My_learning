class Solution:
    def divisorGame(self, n: int) -> bool:

        if n % 2 == 0:
            return True

        if n % 2 != 0:
            return False
        
'''
Memory= 16.23MB
Runtime= 37ms
'''     