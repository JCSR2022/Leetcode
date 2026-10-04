class Solution:
    def checkValidString(self, s: str) -> bool:


        low = 0
        high = 0

        for ch in s:

            if ch == '(':
                low += 1
                high += 1

            elif ch == ')':
                low -= 1
                high -= 1

            else:  # '*'
                low -= 1
                high += 1

            # No podemos tener menos de 0 '(' abiertos
            low = max(0, low)

            # Si incluso el máximo posible es negativo,
            # ya no podemos hacer válida la cadena
            if high < 0:
                return False

        return low == 0



#wildCard
#--------------------------------------------------
        # cnt_left = 0
        # cnt_joker = 0
        
        # for i,ch in enumerate(s):
        #     if ch  == '*':
        #         cnt_joker += 1

        #     elif ch  == '(':
        #         cnt_left +=1 

        #     else:
        #         if cnt_left > 0:
        #             cnt_left -= 1
        #             print(i,ch,cnt_left,cnt_joker)
        #             continue
        #         if cnt_joker > 0:
        #             cnt_joker -= 1
        #             print(i,ch,cnt_left,cnt_joker)
        #             continue
        #         return False
        #     print(i,ch,cnt_left,cnt_joker)
        
        # return True if cnt_left ==0  else cnt_left - cnt_joker  >= 0

        #Eres una maldita mierda imbecil!!!!!


#---------------------------------------------------------------


#no imbecil
        # @lru_cache
        # def dfs(indx,cnt_left,jokers):
        #     if indx == len(s):
        #         if cnt_left <= jokers:
        #             return True
        #         else:
        #             return False

        #     curr_ch = s[indx]

        #     if curr_ch == '*':
        #         return dfs(indx+1,cnt_left,jokers+1)

        #     elif curr_ch == '(':
        #         return dfs(indx+1,cnt_left+1,jokers)

        #     else:
        #         if cnt_left == 0:
        #             if  jokers == 0:
        #                 return False
        #             else:
        #                 return dfs(indx+1,cnt_left,jokers-1)   
        #         return dfs(indx+1,cnt_left-1,jokers)
            
        
        # return dfs(0,0,0)

#-------------------------------------------------------


#---------------------------------------------------------------

        #brute force

        # @lru_cache
        # def dfs(indx,cnt_left):
        #     if indx == len(s):
        #         if cnt_left == 0:
        #             return True
        #         else:
        #             return False

        #     curr_ch = s[indx]

        #     if curr_ch == '*':
        #         opc_left  = dfs(indx+1,cnt_left+1)
        #         opc_right = dfs(indx+1,cnt_left-1) if cnt_left>0 else False 
        #         opc_none = dfs(indx+1,cnt_left)
        #         return opc_left or opc_right or opc_none

        #     elif curr_ch == ')':
        #         if cnt_left == 0:
        #             return False
        #         return dfs(indx+1,cnt_left-1)
            
        #     else:
        #         return dfs(indx+1,cnt_left+1)
            
        
        # return dfs(0,0)

#Time Limit Exceeded
#-------------------------------------------------------

        