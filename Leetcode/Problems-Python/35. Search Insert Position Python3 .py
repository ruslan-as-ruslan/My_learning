class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        
        
        low = 0
        high = len(nums)-1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            if target > nums[mid]:
                low = mid+1
            elif target < nums[mid]:
                high = mid-1
        return high+1 


'''
Runtime: 55 ms, faster than 89.38% of Python3 online submissions for Search Insert Position.
Memory Usage: 14.7 MB, less than 82.73% of Python3 online submissions for Search Insert Position.
'''