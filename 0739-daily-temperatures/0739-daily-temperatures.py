class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
#         ans = []
#         size_temperatures = len(temperatures)

#         for  pointer_1 in range(size_temperatures):
#             pointer_2 = pointer_1
#             while True:
#                 pointer_2 +=1
#                 if  pointer_2 >= size_temperatures:
#                     ans.append(0)
#                     break
#                 if temperatures[pointer_2] > temperatures[pointer_1]:
#                     ans.append(pointer_2-pointer_1)
#                     break
#         return ans

        ans = [0] * len(temperatures)
        stack = []
        
        for i,t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT , stackInd = stack.pop()
                ans[stackInd] = (i-stackInd)
            stack.append([t,i])
        return ans
                
        
    
    




            
            
            
            
            
        
        
        