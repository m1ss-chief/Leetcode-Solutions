class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()
        # for a in range(n):
        #     for b in range(a+1,n):
        #         for c in range(b+1,n):
        #             for d in range(c+1,n):
        #                 if nums[a] + nums[b] + nums[c] + nums[d] == target:
        #                     x = [nums[a],nums[b],nums[c],nums[d]]
        #                     if x not in res:
        #                         res.append(x)
        # return res
        for i in range(n):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            for j in range(i+1,n):
                if (j > i+1 and nums[j] == nums[j-1]):
                    continue
                k = j+1
                l = n-1
                while k<l:
                    add = nums[i] + nums[j] + nums[k] + nums[l]
                    if add < target:
                        k += 1
                    elif add > target:
                        l -= 1
                    else:
                        res.append([nums[i],nums[j],nums[k],nums[l]])
                        k += 1
                        l -= 1
                        while (k<l and nums[k] == nums[k-1]):
                            k += 1
                        while (k<l and nums[l] == nums[l+1]):
                            l -= 1
        return res

                
                    




        