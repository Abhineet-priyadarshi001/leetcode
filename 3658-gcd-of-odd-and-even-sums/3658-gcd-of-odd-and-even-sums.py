class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0
        for i in range(1,n*2+1):
            if i%2 == 0:
                sumOdd +=1
            else:
                sumEven += 1
        return self.GCD(sumOdd,sumEven)
    
    def GCD(self,sumOdd,sumEven):
        a = min(sumOdd,sumEven)
        count = 0
        for i in range(1,a+1):
            if sumOdd % i ==0 and sumEven % i == 0:
                count = i
        return count