class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d = {}
        arr = []
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        sorted_d = dict(sorted(d.items() , key = lambda x : x[1] , reverse =True))
        for i in sorted_d.keys():
            arr.append(i)
        return arr[:k]