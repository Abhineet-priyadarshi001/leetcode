class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        lenth = len(num)
        first_val = 0
        for i in range(lenth):
            first_val = first_val + num[i] * 10 ** (lenth - i-1)

        final_value = first_val + k

        fin_val = []
        
        value = True

        while (value):
            reminder = final_value % 10
            final_value = final_value // 10
            fin_val.append(reminder)
            
            if final_value < 10 :
                value = False
                if final_value !=0:
                   fin_val.append(final_value)
                break
            
        return fin_val[::-1]

        # c = ''.join(map(str,num))
        # d = int(c)
        # e = d+k
        # i = list(map(int , str(final_value)))
        # return i