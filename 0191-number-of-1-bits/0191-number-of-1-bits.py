class Solution:
    def hammingWeight(self, n: int) -> int:
        new_str = ""
        while n > 0:
            if n%2 == 1:
                new_str +="1"
            else:
                new_str += "0"
            n //=2
        count = 0
        for i in new_str:
            if i == "1":
                count += 1
        return count