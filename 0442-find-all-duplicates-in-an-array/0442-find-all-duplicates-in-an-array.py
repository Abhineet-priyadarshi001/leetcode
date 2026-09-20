class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        d = {}
        arr = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for key, value in d.items():
            if value >1 :
                arr.append(key)
        return arr