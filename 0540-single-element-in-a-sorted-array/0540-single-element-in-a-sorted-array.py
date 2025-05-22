class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        for i in range(n):
            if i == 0:
                if nums[i] != nums[i+1]:
                    ans = nums[i]
            elif i == n-1:
                if nums[i] != nums[i-1]:
                    ans = nums[n-1]
            else:
                if nums[i] != nums[i+1] and nums[i] != nums[i-1]:
                    ans = nums[i]
        return ans


        