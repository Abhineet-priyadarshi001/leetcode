class Solution:
    def mySqrt(self, x: int) -> int:
        left , right = 0,x
        count = 0 
        while left <= right:
            mid = (left+right)//2
            if(mid*mid) == x:
                return mid
            elif (mid*mid) < x:
                left = mid+1
                count = mid
            else:
                right = mid-1
        return count