class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # check if on adjacent list there is only one node with no dependences
        # BFC
        
#         adjance_list = {i:[] for i in range(n+1)}
        
#         for org,dest in edges:
#             if org in adjance_list:
#                 adjance_list[org] += [dest]
    
#         print(adjance_list)
#no need
#-------------------------------------------------------------------------
#me!!
#         teams = set(range(n))
#         for _,weak in edges:
 
#             if weak in teams:
#                 teams.remove(weak) 
                
        
#         if len(teams) == 1:
#             return list(teams)[0]
#         else:
#             return -1
        
#---------------------------------------------------------------------

        isUndefeated = [True] * n
        
        for winner, loser in edges:
            isUndefeated[loser] = False
            
        champion = -1
        championCount = 0
        
        for team in range(n):
            if isUndefeated[team]:
                champion = team
                championCount += 1
                
        if championCount == 1:
            return champion
            
        return -1
        