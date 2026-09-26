class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        d1 = {}
        d2 = {}
        answer = []
        arr1 = []
        arr2 = []
        for i in nums1:
            if i not in d1:
                d1[i] = 1
            else:
                d1[i] += 1
        for j in nums2:
            if j not in d2:
                d2[j] = 1
            else:
                d2[j] += 1
        for index in d1.keys():
            if index not in d2.keys():
                arr1.append(index)
        answer.append(arr1)
        for index in d2.keys():
            if index not in d1.keys():
                arr2.append(index)
        answer.append(arr2)
        return answer