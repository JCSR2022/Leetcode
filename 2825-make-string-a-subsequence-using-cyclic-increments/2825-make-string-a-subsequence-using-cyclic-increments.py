class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        
#         #two pointers hashtable
        
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

#         hash_table = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a']
       
        
#         p2 = 0
#         for p1 in str1:
#             if str2[p2] == p1 or str2[p2] ==  hash_table[(ord(p1)-97)]:
#                 p2 += 1
#                 if p2 == len(str2):
#                     return True
        
#         return False
        
#--------------------------------------------------

       
        p2 = 0
        for p1 in str1:
            #print(p2,str2[p2],ord(str2[p2]), p1,ord(p1)+1,chr(ord(p1)+1) )
            #change_char = ord(p1) + 1 if ord(p1) + 1 <= 122 else 97
            if str2[p2] == p1 or ord(str2[p2]) == ord(p1) + 1 if ord(p1) + 1 <= 122 else 97:
                p2 += 1
                if p2 == len(str2):
                    return True
        
        return False


        
        