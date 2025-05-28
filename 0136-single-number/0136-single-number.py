class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        for x in d:
            if d[x] == 1:
                return x


        