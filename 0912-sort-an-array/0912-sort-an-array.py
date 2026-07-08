class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        mid = len(nums) //2
        l_half = nums[:mid]
        r_half = nums[mid:]
# splitted to individual pieces and in next function we will compare and merge it together
        l_half = self.sortArray(l_half)
        r_half = self.sortArray(r_half) 

        return self.merge(l_half,r_half)

    def merge(self,left,right):
        new_arr = []
        i,j = 0,0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                new_arr.append(left[i])
                i += 1
            else:
                new_arr.append(right[j])
                j += 1
        new_arr.extend(left[i:])
        new_arr.extend(right[j:])
        return new_arr