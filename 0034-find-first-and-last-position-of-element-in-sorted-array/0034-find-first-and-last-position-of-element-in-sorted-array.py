class Solution:
    # def searchRange(self, nums: List[int], target: int) -> List[int]:
    #     n = len(nums)
    #     low = 0
    #     high = n-1
    #     res = []
    #     if n == 1 and target == nums[0]:
    #         return [0,0]

    #     while low <= high:
    #         mid = (high + low)//2
    #         if nums[mid] == target:
    #             if nums[mid] == nums[mid+1]:
    #                 return [mid,mid+1]
    #             if nums[mid] == nums[mid-1]:
    #                 return [mid-1,mid]
    #         elif nums[mid] < target:
    #             low = mid + 1
    #         else:
    #             high = mid-1
    #     return [-1,-1]
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums, target):
            low, high = 0, len(nums) - 1
            left_idx = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    left_idx = mid
                    high = mid - 1  # keep searching to the left
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return left_idx
        
        def findRight(nums, target):
            low, high = 0, len(nums) - 1
            right_idx = -1
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] == target:
                    right_idx = mid
                    low = mid + 1  # keep searching to the right
                elif nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return right_idx

        left = findLeft(nums, target)
        if left == -1:
            return [-1, -1]  # target not found
        right = findRight(nums, target)
        return [left, right]
