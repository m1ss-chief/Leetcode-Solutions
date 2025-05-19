class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        res =[]
        n = len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]] += 1
        
        for x in d:
            if d[x] > (n//3):
                res.append(x)
        return res 
        