class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # d = {}
        # temp = False
        # for i in nums:
        #     if i not in d:
        #         d[i] = 1
        #     else:
        #         d[i] =d.get(i)+1
        # for key,value in d.items():
        #     if value > 1:
        #         return True
        # return temp
        seen = set()
        for i in nums:
            if i in seen:
                return True
                
            seen.add(i)
        return False
