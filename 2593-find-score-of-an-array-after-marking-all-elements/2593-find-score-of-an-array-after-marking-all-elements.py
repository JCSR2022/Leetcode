class Solution:
    def findScore(self, nums: List[int]) -> int:
        #brute force
        
#         my_nums = nums.copy()
        
#         score = 0
#         while my_nums:
#             ac_min = min(my_nums)
#             score += ac_min
            
#             i = my_nums.index(ac_min)
            
#             if i == 0:
#                 my_nums[:] = my_nums[2:]
#             elif i == len(my_nums) - 1:
#                 my_nums[:] = my_nums[:-2]
#             else:
#                 my_nums[:] = my_nums[:i-1]+my_nums[i+2:]
            
#             print(score,(i,ac_min),my_nums)
#         #         return score 
    
#no funciona porque te piden marcar no eliminar los valores, asi los vecinos no cambian, en tu solucion si cambian
#---------------------------------------------------------------
        print()
#heap
        heap = [ (n,i) for i,n in enumerate(nums)]
        heapq.heapify(heap)
        
        score = 0
        visited = set()
        
        while heap:
            n,i = heapq.heappop(heap)
            if i not in visited:
                score += n
                visited.add(i)
                visited.add(i-1)
                visited.add(i+1)
                #print(score,(i,n))
        return score
            
                
            
            