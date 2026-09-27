class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        d = {}
        n = len(nums)//2
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for key , value in d.items():
            if value > n:
                return key
