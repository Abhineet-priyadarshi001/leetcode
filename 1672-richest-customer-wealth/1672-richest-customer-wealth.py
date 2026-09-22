class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        arr = []
        for i in range(len(accounts)):
            sum = 0 
            for j in range(len(accounts[0])):
                sum += accounts[i][j]
            arr.append(sum)
        return max(arr)