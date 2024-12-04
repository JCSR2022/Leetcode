class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
        #two pointers hashtable
        
#         hash_table = {
#     'a': ['a', 'b'],
#     'b': ['b', 'c'],
#     'c': ['c', 'd'],
#     'd': ['d', 'e'],
#     'e': ['e', 'f'],
#     'f': ['f', 'g'],
#     'g': ['g', 'h'],
#     'h': ['h', 'i'],
#     'i': ['i', 'j'],
#     'j': ['j', 'k'],
#     'k': ['k', 'l'],
#     'l': ['l', 'm'],
#     'm': ['m', 'n'],
#     'n': ['n', 'o'],
#     'o': ['o', 'p'],
#     'p': ['p', 'q'],
#     'q': ['q', 'r'],
#     'r': ['r', 's'],
#     's': ['s', 't'],
#     't': ['t', 'u'],
#     'u': ['u', 'v'],
#     'v': ['v', 'w'],
#     'w': ['w', 'x'],
#     'x': ['x', 'y'],
#     'y': ['y', 'z'],
#     'z': ['z', 'a']
# }

        
        
#         p2 = 0
#         for p1 in str1:
#             if str2[p2] in hash_table[p1]:
#                 p2 += 1
#                 if p2 == len(str2):
#                     return True
        
#         return False

#--------------------------------------------------

        i, j = 0, 0  # Pointers for str1 and str2

        while i < len(str1) and j < len(str2):
            # Check if current character matches or if incrementing matches
            if str1[i] == str2[j] or chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
                j += 1  # Move to the next character in str2 if matched
            i += 1  # Always move to the next character in str1

        # If we have matched all characters of str2, return True
        return j == len(str2)

        
        
        
        
        
        