class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointers
        left ,right = 0 , len(numbers) -1
        while left<= right:
            numbers_sum = numbers[left] +numbers[right] 
            if numbers_sum == target:
                return [left+1,right+1]
            elif numbers_sum > target:
                right -= 1
            else:
                left +=1

        
        