class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
  

        # use stack,greedy???

        # stack = []
        # points = 0
        # for ch in s:   
        #     stack.append(ch)
        #     print(stack, points)
        #     if len(stack) >= 2:
        #         if stack[-1]+stack[-2] == "ab":
        #             points += x
        #             stack.pop()    
        #             stack.pop() 
        #         elif stack[-1]+stack[-2] == "ba":
        #             points += y
        #             stack.pop()    
        #             stack.pop() 
        # return points 

#nooooooooooooooooooooooooooooooooooooooo
#---------------------------------------------------------------------------

        # def backtrack(i,stack,points):
        #     print(i,stack,points)

        #     if i == len(s):
        #         return points
 
        #     op1 = 0
        #     op2 = 0
        #     if len(stack) >2:
        #         #use x if can
        #         if stack[-1] + stack[-2] == "ab":
        #             ch1 = stack.pop()
        #             ch2 = stack.pop()
        #             op1 = backtrack(i,stack,points + x)
        #             stack.append(ch2)
        #             stack.append(ch1)
        #         #use y if can
        #         elif stack[-1] + stack[-2] == "ba":     
        #             ch1 = stack.pop()
        #             ch2 = stack.pop()
        #             op2 = backtrack(i,stack,points + y)
        #             stack.append(ch2)
        #             stack.append(ch1)
        #     #no use
        #     stack.append(s[i])
        #     op3 = backtrack(i+1,stack,points)

        #     return max(op1,op2,op3)


        # return backtrack(0,[],0)   

#Noooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#---------------------------------------------------------------        
  


  #----------------------------------------------------------------------------
        #ni entiendo esta @#%#@%#$$# solucion
        # a_count = 0
        # b_count = 0
        # lesser = min(x, y)
        # result = 0

        # for c in s:
        #     if c > 'b':
        #         result += min(a_count, b_count) * lesser
        #         a_count = 0
        #         b_count = 0
        #     elif c == 'a':
        #         if x < y and b_count > 0:
        #             b_count -= 1
        #             result += y
        #         else:
        #             a_count += 1
        #     elif c == 'b':
        #         if x > y and a_count > 0:
        #             a_count -= 1
        #             result += x
        #         else:
        #             b_count += 1

        # result += min(a_count, b_count) * lesser
        # return result

#---------------------------------------------------------------
        #correct greedy, first make the one with more value

        if x > y:
            first = x
            second = y
            str_first = "ab"
            str_second = "ba"
        else:
            first = y
            second = x
            str_first = "ba"
            str_second = "ab"

        result = 0

        stack = []
        for ch in s:
            stack.append(ch)
            if len(stack) >= 2 and stack[-2]+stack[-1] == str_first:
                result += first
                stack.pop()
                stack.pop()
            #print(stack,result)

        new_s = "".join(stack)

        stack = []
        for ch in new_s:
            stack.append(ch)
            if len(stack) >= 2 and stack[-2]+stack[-1] == str_second:
                result += second
                stack.pop()
                stack.pop()
            #print(stack,result)
        
        return result
        











#----------------------------------------------------------------------------------
#       Nunca entendi por que no funciona @#%#@%@#$%
#         #greedy with a pointer and a stack
        
#         def check_substring(stack,var,substring):
#             cont = 0
#             i = 1
#             while i < len(stack):
#                 if stack[i-1]+stack[i] == substring:
#                     del stack[i-1]
#                     del stack[i-1]
#                     cont += var
#                     i -= 1
#                 else:
#                     i += 1
#             return cont, stack
                   
        
#         var_ab_xy = [[x,'ab'],[y,'ba']]
#         var_ab_xy.sort(reverse=True)
#         stack = list(s)
#         print(var_ab_xy)
        
#         ans = 0
#         for var,substring in var_ab_xy:
#             print(var,substring,ans,"".join(stack))
#             cont,stack =  check_substring(stack,var,substring)
#             ans += cont
#         print(ans,"".join(stack))          
#         return ans