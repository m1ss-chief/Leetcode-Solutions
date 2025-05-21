class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n-1
        found = False
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                found = True
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low 