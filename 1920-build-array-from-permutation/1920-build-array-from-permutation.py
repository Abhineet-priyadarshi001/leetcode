class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        arr = []
        for i in range(len(nums)):
            s = nums[nums[i]]
            arr.append(s)
        return arr