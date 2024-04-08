class Solution:
    def checkValidString(self, s: str) -> bool:
#         # aproach:
#         #   pointer to go through s 
#         #   list  as stack for "(" and ')' 
#         #      if a '(' append
#         #      if a '*' wild_card append
#         #      if ')'  check if last is '(' or wild_card 
        
#         stack = []
        
#         for i in range(len(s)):
#             print(i, stack,s[:i])
#             if s[i] == '(' or s[i] == '*':
#                 stack.append(s[i])
#             else:
#                 found = False
#                 j = len(stack)-1
#                 while j >= 0:
#                     if stack[j] == '(':
#                         del stack[j]
#                         found = True
#                         break
#                     j -=1
                
#                 j = len(stack)-1
#                 while j >= 0 and not found:
#                     if stack[j] == '*':
#                         del stack[j]
#                         found = True
#                         break
#                     j -=1    
                    
#                 if not found:
#                     return False
                
            
#         if len(stack) == 0 or set(stack) == {'*'}:
#             return True
#         else:
#             return False

#  NUNCA LOGRE QUE FUNCIONARA!!!! #@$%@#%#$^#@$$#%@$%^#$^$e

        leftMin, leftMax = 0,0
        
        for c in s:
            if c == '(':
                leftMin,leftMax = leftMin + 1 ,leftMax + 1
            elif c == ')':
                leftMin,leftMax = leftMin - 1 ,leftMax - 1
            else:
                leftMin,leftMax = leftMin - 1 ,leftMax + 1
            if leftMax < 0:
                return False
            leftMin = max(leftMin,0)
            
        return leftMin == 0
            
                
                
                

        
    
    
    
    


            