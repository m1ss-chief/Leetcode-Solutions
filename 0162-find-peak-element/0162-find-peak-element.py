class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # return nums.index(max(nums) # simplest way 

        n = len(nums)
        if len(nums) == 1:
            return 0
        if nums[0] > nums[1]:
            return 0
        if nums[n-1] > nums[n-2]:
            return n-1
        low, high = 1, n-2
        while low<= high:
            mid = (low+high)//2
            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            elif nums[mid] > nums[mid-1]:
                low = mid + 1
            else:
                high = mid - 1
        return -1

        # n = len(nums)           #O(N) Time Complexity
        # for i in range(n):       
        #     if (i==0 or nums[i-1] < nums[i]) and (i == n-1 or nums[i] > nums[i+1]):
        #         return i 
        