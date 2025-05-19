class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # d = {}
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         k = -(nums[i] + nums[j])
        #         if k in d:
        #             a = sorted([nums[i], nums[j], k ])
        #             if a not in res:
        #                 res.append(a)
        #         else:
        #             if nums[j] not in d:
        #                 d[nums[j]] = True
        #     d = {}

        # return res
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n-1):
            if i>0 and nums[i] == nums[i-1]:
                continue
            else:
                j = i+1
                k = n-1
                while j<k:
                    add = nums[i] + nums[j] + nums[k]
                    a = [nums[i],nums[j],nums[k]]
                    if add == 0:
                        res.append(a)
                        j += 1
                        k -= 1
                        while j<k and (nums[j]==nums[j-1]):
                            j += 1
                        while j<k and (nums[k]==nums[k+1]):
                            k -= 1
                    elif add < 0:
                        j += 1
                    else:
                        k -= 1
        return res


            

        