class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # min_index = nums.index(min(nums))
        # nums.sort()
        # n = len(nums)
        # low = 0
        # high = n-1
        # while low <= high:
        #     mid = (high + low)//2
        #     if nums[mid] == target:
        #         return (mid + min_index) % n
        #     elif nums[mid] < target:
        #         low = mid + 1
        #     else:
        #         high = mid-1
        # return -1
        n = len(nums)
        low = 0
        high = n-1
        while low <= high:
            mid = (high + low)//2
            if nums[mid] == target:
                return mid
            if nums[low] <= nums[mid]: #left sorted
                if nums[low] <= target and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else: # right sorted
                if target <= nums[high] and target > nums[mid]:
                    low = mid+1
                else:
                    high = mid - 1
        return -1
