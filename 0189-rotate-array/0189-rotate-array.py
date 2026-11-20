class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # for i in range(k+1):
        #     x = nums.pop(0)
        #     nums.append(x)
        # return nums
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
        return nums