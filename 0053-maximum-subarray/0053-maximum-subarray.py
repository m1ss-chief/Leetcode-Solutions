class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        # add, ans= 0, -inf
        # for i in range(n):
        #     for j in range(i,n):
        #         add += nums[j]
        #         ans = max(add, ans)
        #     print(ans)
        #     add = 0 
        # return ans

        maxi = -inf
        sub_sum = 0
        for i in range(n):
            sub_sum += nums[i]
            maxi = max(sub_sum, maxi)
            if sub_sum<0:
                sub_sum = 0
        return maxi 


        