class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # construir un decision tree , dfs.
        
        res = []
        
        def dfs(i,cur,total):
            print(i,cur,total)
            if total == target:
                res.append(cur.copy())
                return 
            
            if i >= len(candidates) or total > target:
                return
            
            cur.append(candidates[i])
            dfs(i, cur, total+candidates[i])
            cur.pop()
            dfs(i+1, cur, total)
            
            
        candidates.sort()    
        dfs(0,[],0)
        
        return res
            
            
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #aproch:
        # sort the candidates and try if target//candidates[0] == 0 
        # then try target// ((target//candidates[0] - 1)+candidates[1]) ==0
        
#         candidates.sort()
#         print(candidates)
        
#         for i in range(len(candidates)):
#             print(i,candidates[i], target//candidates[i],target%candidates[i])
        
#         return [[1]]
        