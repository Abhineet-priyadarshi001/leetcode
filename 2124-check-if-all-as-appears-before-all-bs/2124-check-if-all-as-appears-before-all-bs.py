class Solution:
    def checkString(self, s: str) -> bool:
        n = len(s)
        for i in range(n):
            if i+1 < n and (s[i] == 'b' and s[i + 1] == 'a'):
                return False
        return True