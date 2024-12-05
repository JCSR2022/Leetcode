class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        #two pointers: O(n*m)
        # target_pointer if L and 0 R conunt L move start_pointer until find L (count L -1) if find R return False
        # target_pointer if R and 0 L, count R move start_pointer until find R (count R -1) if find L return False
        
#         s_p = 0
#         cont_R = 0
#         for t_p in range(len(target)):
#             if target[t_p] == 'L':
#                 while start[s_p] != 'L':
#                     s_p += 1
#                     if s_p > len(start)-1  or start[s_p]== 'R' : return False                         
           
        
        
#             if target[t_p] == 'R':
#                 if cont_R > 0:
#                     cont_R -= 1
#                 while s_p < t_p:
#                     print('t_p: ',t_p,'s_p:',s_p,target[t_p], start[s_p])
#                     if s_p > len(start)-1  or start[s_p]== 'L' : 
#                         return False     
#                     elif start[s_p] == 'R':
#                         cont_R += 1   
#                     s_p += 1
                    
                        
                        
#         print('t_p: ',t_p,'s_p:',s_p,target[t_p], start[s_p])
#         print(cont_R)
            
        
#         return True



#-----------------------------------------------------------

#         s = 0
#         count_R = 0
        
#         # if target.count('R') != start.count('R'):
#         #     return False
#         # if target.count('L') != start.count('L'):
#         #     return False
        
#         for t in range(len(target)):
            
#             if target[t] == 'L':
#                 while s < t :
#                     if start[s] == 'R':
#                         return False
#                     s +=1
#                 while True: 
#                     if s > len(start)-1 or start[s] == 'R':
#                         return False
#                     elif start[s] == 'L':
#                         s += 1
#                         break
#                     else:
#                         s += 1
                
                    
#             if target[t] == 'R':
#                 if count_R == 0:
#                     while s < t:
#                         if s > len(start)-1 or start[s] == 'L':
#                             return False
#                         elif start[s] == 'R':
#                             count_R += 1
#                         s += 1
#                     if count_R == 0:
#                         return False

#                 else:
#                     count_R -= 1
        
#         while s < len(start):
#             if start[s] != '_':
#                 return False
#             s += 1
        
        
#         return True
            
                
#----------------------------------------------------------------


        n=len(start)
        start +='_'
        target +='_'
        i , j = 0 , 0
        while i<n or j<n:
            while i<n and start[i]=='_': i+=1
            while j<n and target[j]=='_': j+=1
            c = start[i]
            if c != target[j]: return False
            if c == 'L' and i<j: return False
            if c == 'R' and i>j: return False
            i += 1
            j += 1
        return True
        
        
    

