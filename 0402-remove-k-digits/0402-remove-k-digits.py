class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        # APROACH MONOTONIC STACK
        stack = []
    
        for c in num:
            #print(0,c,stack,k)
            while k > 0 and stack and stack[-1] > c:
                #print(1,c,stack,k)
                k-=1
                stack.pop()
            #print(2,c,stack,k)
            stack.append(c)
        #print(3,c,stack)    
        #if all in incresing order
        stack = stack[:len(stack)-k]
        #print(4,c,stack)
        res = "".join(stack)
        
        if not res:
            return '0'
        
        for i,c in enumerate(res):
            if c != '0':
                return res[i:]
        
        return '0'
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #APROACH :
        # MOVIN FROM THE LEFT IF NEXT DIGIT IS BIGER DROP NEXT ELSE DROP ACTUAL UNTIL K =0
        
#         def del_num_i(i,num):
#             num = num[:i]+num[i+1:]
#             if len(num) == 0:
#                 return '0'
#             else:
#                 return num
        
#         i = 1
#         while k > 0 and len(num) > 0:
#             if len(num) == 1:
#                 num ="0"
#                 break
#             if int(num)==0:
#                 num ='0'
#                 break
#             print(num,len(num),i,num[i-1],num[i],num[i-1] > num[i])
#             if num[i-1] > num[i]:
#                 num = del_num_i(i-1,num)
#                 k -=1
#             elif num[i-1] < num[i]:
#                 num = del_num_i(i,num)
#                 k -=1
#             else:
#                 j = i
#                 while j < len(num):
#                     if num[j-1] > num[j]:
#                         num = del_num_i(j-1,num)
#                         k -=1
#                         break
#                     elif num[j-1] < num[j]:
#                         num = del_num_i(j,num)
#                         k -=1
#                         break
#                     else:
#                         j +=1
#                         if j == len(num):
#                             num = del_num_i(i-1,num)
#                             k -=1
#                 i +=1      
                        
#         return str(int(num))
#  2 TIME NO WORK $&%$%/$/"#$%/(/&(&))"
            
            
    
        
#         # Especial case
#         if k == 1 and len(num) ==1:
#             return '0'
        
        
#         def del_num_i(i,num):
#             if i < len(num):
#                 return num[:i]+num[i+1:]
#             else:
#                 return ''
        
        
#         i = 1
#         while k > 0 and  i < len(num):
#             print(i,num[i-1],num[i],num[i-1] > num[i], num, k)
#             if num[i-1] > num[i]:
#                 num = del_num_i(i-1,num)
#                 k -=1       
#             elif num[i-1] > num[i]:
#                 num = del_num_i(i,num)
#                 k -=1
#                 i +=1
#             elif num[i-1] == num[i]:
#                 i +=1
                
#         return str(int(num))
# NO WORK


            