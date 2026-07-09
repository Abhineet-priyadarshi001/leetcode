class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_arr = []
        for i in nums:
            new_arr.append(i**2)
        new_arr.sort()
        return new_arr
        # n = len(new_arr)
        # for k in range(n):
        #     for j in range(0,n-k-1):
        #         if new_arr[j] > new_arr[j+1]:
        #             new_arr[j],new_arr[j+1] = new_arr[j+1],new_arr[j]
        # return new_arr