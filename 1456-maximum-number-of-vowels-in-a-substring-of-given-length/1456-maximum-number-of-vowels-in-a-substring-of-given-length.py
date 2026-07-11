class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        n = len(s)
        count_vowel = 0 
        vowels = {'a', 'e', 'i', 'o', 'u'}
        for i in range(k):
            if s[i] in vowels:
                count_vowel += 1
        max_vowel = count_vowel
        for j in range(k,n):
            if s[j] in vowels:
                count_vowel += 1
            if s[j-k] in vowels:
                count_vowel -= 1
            max_vowel = max(max_vowel,count_vowel)
        return max_vowel
