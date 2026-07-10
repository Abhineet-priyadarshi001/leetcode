class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        average = 0
        max_average = 0
        for i in range(k):
            average += nums[i]/k
        max_average = average
        for j in range(k,n):
            average += (nums[j] - nums[j-k])/k
            max_average = max(average,max_average)
        return max_average
        