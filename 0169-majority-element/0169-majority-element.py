class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # d = {}
        # n = len(nums)
        # for i in range(n):
        #     if nums[i] not in d:
        #         d[nums[i]] = 1
        #     else:
        #         d[nums[i]] += 1
        # max = (n / 2)
        # for x in d:
        #     if d[x] > max:
        #         max = d[x]
        #     if max == d[x]:
        #         return x
        candidate = None
        count = 0
        for x in nums:
            if count == 0:
                candidate = x
            if x == candidate:
                count += 1 
            else:
                count -= 1
        return candidate

        