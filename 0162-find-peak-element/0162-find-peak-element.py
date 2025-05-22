class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums)
        # maxi = -inf
        # n = len(nums)
        # low, high = 0, n-1
        # while low<= high:
        #     mid = (low+high)//2

        #     if nums[low] <= nums[mid]: #left sorted
        #         maxi = max(maxi,nums[mid])
        #         low = mid + 1
        #     else: #right sorted
        #         maxi = max(nums[high],maxi)
        #         high = mid - 1
        # return mid
        n = len(nums)
        for i in range(n):
            if (i==0 or nums[i-1] < nums[i]) and (i == n-1 or nums[i] > nums[i+1]):
                return i 
        