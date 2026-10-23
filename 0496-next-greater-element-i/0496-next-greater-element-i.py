class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        arr = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range (j+1,len(nums2)):
                        if nums1[i] < nums2[k]:
                            arr.append(nums2[k])
                            break
                    else:
                        arr.append(-1)
        return arr
