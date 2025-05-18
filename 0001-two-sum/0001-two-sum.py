class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]] = i
        print (d)
        for i in range(len(nums)):
            c = (target - nums[i])
            if c in d and d[c] != i:
                return [i, d[c]]
            
        