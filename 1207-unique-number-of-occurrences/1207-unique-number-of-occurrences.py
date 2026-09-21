class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        d = {}
        seen  = set()
        for i in arr:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d.values():
            if i in seen:
                return False
            seen.add(i)
        return True