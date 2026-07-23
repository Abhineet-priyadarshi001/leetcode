class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        arr = []
        j = 0
        for i in range(len(pushed)):
            arr.append(pushed[i])
            while arr and arr[-1] == popped[j] and j<len(pushed):
                arr.pop()
                j += 1
        if len(arr) == 0:
            return True
        else:
            return False