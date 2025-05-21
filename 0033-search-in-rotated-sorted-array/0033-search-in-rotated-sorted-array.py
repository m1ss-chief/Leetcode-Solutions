class Solution:
    def search(self, nums: List[int], target: int) -> int:
        min_index = nums.index(min(nums))
        nums.sort()
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                return (mid + min_index) % n
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid-1
        return -1
        