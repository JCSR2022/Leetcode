from itertools import combinations

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        #https://www.youtube.com/watch?v=FOyRpNUSFeA
        
        res = [] 
        
        candidates.sort()
        
        def dfs(i, cur, total):
            
            if total == target:
                res.append(cur.copy())
                return
            
            if total > target or i == len(candidates):
                return
            
            #include candidates[i]
            cur.append(candidates[i])
            dfs(i+1,cur, total + candidates[i])            
            cur.pop()
            
            #skip candidates[i]
            while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1,cur, total)     
            
            
        dfs(0,[],0)
            
        return res
    
    
    
    
    
    
    
    
    #brute force, try all combinations 
#         N = len(candidates)
        
#         ans = set()
#         for i in range(N):
#             comb = list(combinations(candidates, i))
#             print(comb)
#             for elem in comb:
#                 if sum(elem) == target:
#                     ans.add(list(elem))
                
#         return list(ans)






                
        