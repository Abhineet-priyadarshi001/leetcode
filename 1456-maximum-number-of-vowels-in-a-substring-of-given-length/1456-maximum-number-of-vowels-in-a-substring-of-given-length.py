class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        count_vowel = 0 
        for i in range(k):
            if s[i] == "a" or s[i] =="e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
                count_vowel += 1
        max_vowel = count_vowel
        for j in range(k,n):
            if s[j] == "a" or s[j] == "e" or s[j] == "i" or s[j] == "o" or s[j]== "u":
                count_vowel += 1
            if s[j-k] == "a" or s[j-k] =="e" or s[j-k] == "i" or s[j-k] == "o" or s[j-k] =="u":
                count_vowel -= 1
            max_vowel = max(max_vowel,count_vowel)
        return max_vowel
