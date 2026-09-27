
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # nums = [2,2,1,1,1,2,2]
        d = Counter(nums)
        n = len(nums)//2
        for key , value in d.items():
            if value > n:
                return key
