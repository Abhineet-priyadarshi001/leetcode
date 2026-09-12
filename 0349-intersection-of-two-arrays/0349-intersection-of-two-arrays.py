class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # s = set()
        # for i in nums1:
        #     if i in nums2:
        #         s.add(i)
        # arr = list(s)
        # return arr
        return list(set(nums1) & set(nums2))