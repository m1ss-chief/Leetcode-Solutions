class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        nums.sort()
        low = 0
        high = n-1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid-1
        return False
        