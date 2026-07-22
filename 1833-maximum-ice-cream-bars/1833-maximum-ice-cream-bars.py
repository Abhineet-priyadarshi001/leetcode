class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        count = 0
        costs.sort()
        s = 0
        for i in range(len(costs)):
            count += costs[i]
            if count <= coins:
                s += 1
        return s
        # s = max(costs)
        # arr = [0] *(s+1)
        # for i in range(len(costs)):
        #     arr[costs[i]] += 1
        # for j in range(len(arr)):
        #     while arr[j] >0 and coins >= j:
        #         count+= 1
        #         arr[j] -= 1
        #         coins -= j
        # return count