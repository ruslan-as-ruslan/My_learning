class Solution(object):
    def maxProfit(self, prices):
        
        min = prices[0]
        profit = 0

        for i in prices:
            if i < min:
                min = i
            elif (i - min) > profit:
                profit = i - min

        return profit

'''
Submissions:

Runtime = 965 ms
Memory = 27.3 MB

'''

