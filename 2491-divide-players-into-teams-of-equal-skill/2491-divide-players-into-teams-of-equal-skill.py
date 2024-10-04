class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        
#       Brute force nlog(n) - sort

        target = sum(skill)//(len(skill)//2)
        skill.sort()
        ans = 0
        for i in range(len(skill)//2):
            #print(i,skill[i],skill[len(skill)-i-1])
            if skill[i] + skill[len(skill)-i-1] != target:
                return -1
            ans +=  skill[i]*skill[len(skill)-i-1]
        return ans
        



        
        
#         #realy brute force aproach:
        
#         target = sum(skill)//(len(skill)//2)
        
#         teams = [[] for _ in range(len(skill)//2)]
        
#         for player in skill:
#             i = 0
#             while i < len(teams):
#                 if len(teams[i]) == 0:
#                     teams[i].append(player)
#                     break
#                 elif len(teams[i]) == 2:
#                     i += 1 
#                 else:
#                     if player+teams[i][0] ==  target:
#                         teams[i].append(player)
#                         break
#                     else:
#                         i +=1
                        
#             if i >= len(teams):
#                 return -1
                        
#         return sum( v[0]*v[1] for v in teams)