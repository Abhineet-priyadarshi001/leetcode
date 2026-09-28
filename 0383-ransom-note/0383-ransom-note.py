class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d_ransom = {}
        d_maganize = {}
        for i in ransomNote:
            if i not in d_ransom:
                d_ransom[i] = 1
            else:
                d_ransom[i] += 1
        for j in magazine:
            if j not in d_maganize:
                d_maganize[j] = 1
            else:
                d_maganize[j] += 1
        for key , value in d_maganize.items():
            if key in d_ransom.keys():
                d_ransom[key] -= value
        for key , value in d_ransom.items():
            if value > 0:
                return False
        return True