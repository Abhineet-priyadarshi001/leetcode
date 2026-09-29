class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums2  = []
        for i in range(len(nums1)):
            nums2.append(nums1[i])
        for i in range(len(nums2)):
            if abs(nums2[i]) %2 == 0 or abs(nums2[i]) %2 != 0:
                return True
