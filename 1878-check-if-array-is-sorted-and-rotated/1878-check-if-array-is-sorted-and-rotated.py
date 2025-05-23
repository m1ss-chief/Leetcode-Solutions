class Solution:
    def check(self, nums: List[int]) -> bool:
        s_nums = sorted(nums)
        for i in range(len(nums)):
            if nums == s_nums:
                return True
            else:
                x = nums.pop(0)
                nums.append(x)
        return False       