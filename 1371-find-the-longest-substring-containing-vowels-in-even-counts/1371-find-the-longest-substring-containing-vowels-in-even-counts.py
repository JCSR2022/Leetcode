class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
#         #brute realy brute force:
#         def haveEvenVowels(sub_s):
#             vowels = "aeiou"       
#             for vowel in vowels:
#                 if sub_s.count(vowel)%2 != 0:
#                     return False
#             return True
           
#         max_vowels = 0
#         for i in range(len(s)):
#             for j in range(i+1,len(s)+1):
#                 #print(s[i:j],haveEvenVowels(s[i:j]))
#                 if haveEvenVowels(s[i:j]):
#                     max_vowels = max(max_vowels,len(s[i:j])) 
#         return max_vowels
    
    
        # Two pointers l , r (sliding window) 
        # do not work 
        
        
        
        
	    # user0517qU
        # Vowels with their respective bitmask values
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        
        # Dictionary to store the first occurrence of each bitmask
        # We start with bitmask 0 at index -1, to handle the case when the entire string is valid
        first_occurrence = {0: -1}
        
        # Current bitmask and result variable
        mask = 0
        max_len = 0
        
        # Traverse the string
        for i, c in enumerate(s):
            # If the character is a vowel, update the bitmask
            if c in vowels:
                mask ^= vowels[c]
            
            # If the bitmask has been seen before, calculate the length of the substring
            if mask in first_occurrence:
                max_len = max(max_len, i - first_occurrence[mask])
            else:
                # If this is the first time we've seen this bitmask, store the index
                first_occurrence[mask] = i
        
        return max_len