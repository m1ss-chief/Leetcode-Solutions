class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # for j in range(k):
        #     last = nums[-1]
        #     for i in range(1,len(nums)):
        #         nums[-i] = nums[-i-1]
        #     nums[0] = last
        # temp = []
        # k = k % len(nums)
        # for i in range(k):
        #     temp.append(nums[-k+i])
        # for i in range(len(nums)):
        #     nums[len(nums)-1-i] = nums[k-i]
        # for i in range(k):
        #     nums[i] = temp[i] 
        k = k % len(nums)
        temp = nums[-k:]  # Store last k elements
        for i in range(len(nums) - 1, k - 1, -1):
            nums[i] = nums[i - k]  # Shift elements right
        if k!=0:
            nums[:k] = temp
            

