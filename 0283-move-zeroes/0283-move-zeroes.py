class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        temp = []
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            else:
                temp.append(nums[i])
        nums[:] = temp
        for i in range(count):
            nums.append(0)
        