class Solution:
    def finalPrices(self, prices: list[int]) -> list[int]:
        stk = []
        for i in range(len(prices)):
            for j in range(1,len(prices)):
                if j > i and prices[i]>= prices[j]:
                    stk.append(prices[i]-prices[j])
                    break
            else:
                stk.append(prices[i])
        return stk