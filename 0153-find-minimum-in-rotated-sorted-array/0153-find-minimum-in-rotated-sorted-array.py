class Solution:
    def findMin(self, nums: List[int]) -> int:
        # return min(nums)
        mini = inf
        n = len(nums)
        low, high = 0, n-1
        while low<= high:
            mid = (low+high)//2
            # mini = min(mini, nums[mid])

            if nums[low] <= nums[mid]: #left sorted
                mini = min(mini,nums[low])
                low = mid + 1
            else: #right sorted
                mini = min(nums[mid],mini)
                high = mid - 1
        return mini

        