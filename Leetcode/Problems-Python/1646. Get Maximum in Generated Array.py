class Solution:
    def getMaximumGenerated(self, n: int) -> int:

        nums = [0 for _ in range(n+1)]
        nums[0] = 0
        nums[1] = 1

        for i in range(2, n+1):

            if i % 2 == 0:

                nums[i] = nums[i // 2]

            if i % 2 != 0:

                nums[i] = nums[i // 2 ] + nums[i // 2 + 1]   

        return max(nums)
    

print(Solution.getMaximumGenerated(self=Solution, n = 7))

'''
Runtime = 40 ms
Memory = 16.34mb

'''