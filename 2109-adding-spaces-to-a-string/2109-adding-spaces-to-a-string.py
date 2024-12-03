class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        
#         new_str = ""
#         sp = 0
#         for i,ch in enumerate(s):
#             if i == spaces[sp]:
#                 new_str +=" " 
#                 if sp + 1 < len(spaces): sp += 1
                        
#             new_str +=ch
            
#         return new_str
    
# -----------------------------------------------

            arr = []
            arr.append(s[:spaces[0]])
            for i in range(1, len(spaces)):
                arr.append(s[spaces[i-1]:spaces[i]])
            arr.append(s[spaces[-1]:])
            return ' '.join(arr)
