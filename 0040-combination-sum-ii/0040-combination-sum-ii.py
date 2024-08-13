#from itertools import combinations
#from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
       
        #aproach, make a dfs find al posible combinations
        ans = []
        
        candidates.sort()

        def dfs(i,cur,total):
            
            if total == target:
                ans.append(cur.copy())
                return

            if i == len(candidates) or total > target:
                return

            #include element
            cur.append(candidates[i])
            dfs(i+1,cur,total+candidates[i])
            cur.pop()

            #not include element:
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i +=1
            dfs(i+1,cur,total)


        dfs(0,[],0)

        return ans
    
    
    
    
    
    
#         #aproach, make a dfs find al posible combinations
#         ans = []
# #        record = {}
#         def dfs(i,cur,total):
# #             if i in record:
# #                 record[i].append([cur.copy(),total])
# #             else:
# #                 record[i] = [cur.copy(),total]
            
            
#             if total == target:
#                 #print(cur,total,ans)
#                 for prev in ans:
#                     if Counter(prev) == Counter(cur):
#                         return
#                 ans.append(cur.copy())
#                 return

#             if i == len(candidates) or total > target:
#                 return

#             #include element
#             cur.append(candidates[i])
#             dfs(i+1,cur,total+candidates[i])
#             cur.pop()

#             #not include element:
#             dfs(i+1,cur,total)


#         dfs(0,[],0)
        
#         # for k,v in record.items():
#         #     if k == 10:
#         #         for elem in v:
#         #             print(elem)
        
        
#         return ans
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#         #https://www.youtube.com/watch?v=FOyRpNUSFeA
        
#         res = [] 
        
#         candidates.sort()
#         print(candidates)
#         tree = {}
#         def dfs(i, cur, total):
#             if i in tree:
#                 tree[i].append(cur.copy())
#             else:
#                 tree[i] = [cur.copy()]
            
#             #print(i, cur,total)
            
#             if total == target:
#                 res.append(cur.copy())
#                 return
            
#             if total > target or i == len(candidates):
#                 return
            
#             #include candidates[i]
#             cur.append(candidates[i])
#             dfs(i+1,cur, total + candidates[i])            
#             cur.pop()
            
#             #skip candidates[i]
#             while i +1 < len(candidates) and candidates[i] == candidates[i+1]:
#                 i += 1
#             dfs(i+1,cur, total)     
            
            
#         dfs(0,[],0)
        
#         for k,v in tree.items():
#             print(k,v)
        
#         return res
    
    
    
    
    
    
    
    
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






                
        