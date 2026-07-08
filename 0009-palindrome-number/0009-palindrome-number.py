class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        number_2 = x
        while number_2 > 0:
            digit = number_2 % 10
            rev = rev * 10 + digit
            number_2 = number_2 // 10

        if x < 0:
            return False
            
        return x== rev
