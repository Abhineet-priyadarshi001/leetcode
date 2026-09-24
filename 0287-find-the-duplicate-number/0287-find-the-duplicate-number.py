class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # d = {}
        # for i in nums:
        #     if i not in d:
        #         d[i] =1
        #     else:
        #         d[i] += 1
        # for key ,value in d.items():
        #     if value > 1:
        #         return key

        s = set()
        for i in nums:
            if i in s:
                return i
            s.add(i)