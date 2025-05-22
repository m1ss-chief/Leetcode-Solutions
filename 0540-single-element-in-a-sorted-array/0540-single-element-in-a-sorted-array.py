class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)         #Time Complexity: O(N) Brute force
        if n == 1:
            return nums[0]
        # for i in range(n):
        #     if i == 0:
        #         if nums[i] != nums[i+1]:
        #             ans = nums[i]
        #     elif i == n-1:
        #         if nums[i] != nums[i-1]:
        #             ans = nums[n-1]
        #     else:
        #         if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
        #             ans = nums[i]
        # return ans
        if nums[0] != nums[1]:
            return nums[0]
        if nums[-1] != nums[-2]:
            return nums[-1]
        low, high = 1, n-2
        while low <= high:
            mid = (low+high)//2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif mid % 2 == 0:
                if nums[mid] == nums[mid+1]: #single element in right half
                    low = mid + 1
                else:
                    high = mid - 1  #single element on left half
            else:
                if  nums[mid] == nums[mid-1]:    #single element on right half
                    low = mid + 1
                else:
                    high = mid - 1  #single element on left half
        return -1



        