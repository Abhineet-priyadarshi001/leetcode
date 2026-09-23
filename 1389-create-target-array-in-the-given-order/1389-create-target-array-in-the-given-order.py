class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        arr = []
        # i = 0
        # while i < len(nums):
        #     arr.insert(index[i] , nums[i])
        #     i += 0
        # return arr

        for i in range(len(index)):
            arr.insert(index[i],nums[i])
        return arr