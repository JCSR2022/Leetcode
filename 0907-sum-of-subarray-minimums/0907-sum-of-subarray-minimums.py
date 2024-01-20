class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
      #  sum_arr_min = 0
      #  MOD = 10 ** 9 + 7
      #  size = len(arr)
      #  for i in range(size):
      #      minimo = arr[i]
      #      for j in range(i,size):
      #          minimo = min(minimo,arr[j])
      #          sum_arr_min += minimo       
      #  return sum_arr_min % MOD
        
        class elem_stack():
            def __init__(self,index,num):
                self.index = index
                self.num = num
        
        
        MOD = 10 ** 9 + 7 
        res = 0 
        stack = [] 
        
        for i,n in enumerate(arr):
            while stack and n < stack[-1].num:
                extracted = stack.pop()
                j = extracted.index
                m = extracted.num
                
                left = j - stack[-1].index if stack else j+1
                right  = i-j 
                res = (res + m * left * right) % MOD
                
            elem_stack_i = elem_stack(i,n)   
            stack.append(elem_stack_i)
            
        for i in range(len(stack)):
            j = stack[i].index
            n = stack[i].num
            
            left = j - stack[i-1].index if i > 0 else j + 1 
            right = len(arr) - j 
            
            res = (res + n * left * right ) % MOD
            
        return res
                
            
            
        