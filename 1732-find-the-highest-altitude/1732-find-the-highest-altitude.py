class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        prefix_sum = [0] * (len(gain)+1)
        prefix_sum[1] = gain[0]
        for i in range(1,len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + gain[i-1]
        return max(prefix_sum)