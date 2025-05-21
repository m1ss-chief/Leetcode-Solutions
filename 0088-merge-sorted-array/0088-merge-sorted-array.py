class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            if nums1[i+m] == 0:
                nums1[i+m] = nums2[i]
        nums1.sort()
        return nums1
        