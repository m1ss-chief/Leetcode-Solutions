class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = 1
        suffix= 1
        max_prod = -inf
            
        for i in range(n):
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix = prefix*nums[i]
            suffix = suffix*nums[n-i-1]
            max_prod = max(max_prod, prefix, suffix)
        return max_prod


        