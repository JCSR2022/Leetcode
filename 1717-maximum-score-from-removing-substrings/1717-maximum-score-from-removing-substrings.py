class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
  
        a_count = 0
        b_count = 0
        lesser = min(x, y)
        result = 0

        for c in s:
            if c > 'b':
                result += min(a_count, b_count) * lesser
                a_count = 0
                b_count = 0
            elif c == 'a':
                if x < y and b_count > 0:
                    b_count -= 1
                    result += y
                else:
                    a_count += 1
            elif c == 'b':
                if x > y and a_count > 0:
                    a_count -= 1
                    result += x
                else:
                    b_count += 1

        result += min(a_count, b_count) * lesser
        return result









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