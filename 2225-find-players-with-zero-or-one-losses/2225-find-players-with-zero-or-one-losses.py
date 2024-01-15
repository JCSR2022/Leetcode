class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # 1. Assemble a dicc with keys players and values a tuple (num_wins,num_loses)
        # 2. create vectors ans0 and ans1
        
#         def create_player_win_lost_dicc(matches):
#             dicc_out = {}
#             for match in matches: 
#                 salidas_inicio_i = [[1,0],[0,1]] 
#                 for i in range(2):          
#                     if match[i] not in dicc_out:
#                         dicc_out[match[i]] = salidas_inicio_i[i]
#                     elif match[i] in dicc_out:
#                         dicc_out[match[i]][i] +=1    
#             return dicc_out
        
#         def find_not_lost(player_win_lost_dicc):
#             ans = []
#             for key,val in player_win_lost_dicc.items():
#                 if val[1] == 0:
#                     ans = ans + [key]
#             ans.sort()
#             return ans
        
#         def find_lost_one(player_win_lost_dicc):
#             ans = []
#             for key,val in player_win_lost_dicc.items():
#                 if val[1] == 1:
#                     ans = ans + [key]
#             ans.sort()
#             return ans            
                
#         win_lost_dicc = create_player_win_lost_dicc(matches)
        
#         return [find_not_lost(win_lost_dicc),find_lost_one(win_lost_dicc)]


        #Segunda propuesta
#         no_lost = []
#         lost_1 = []
#         losers = []
#         for match in matches:
#             print (match, no_lost,lost_1,losers)
            
#             # insert in losers and list lost_1:
#             if (match[1] not in lost_1) and (match[1] not in losers):
#                 lost_1.append(match[1])
#                 losers.append(match[1])
#             elif (match[1] in lost_1) and (match[1] in losers):
#                 lost_1.pop(lost_1.index(match[1]))
                
#             # insert players that only win
#             if (match[0] not in no_lost) and (match[0] not in losers):
#                 no_lost.append(match[0])
#             # drop lossers
#             if match[1] in no_lost:
#                 no_lost.pop(no_lost.index(match[1]))
                
#             no_lost.sort()
#             lost_1.sort()
            
#         return no_lost, lost_1

    #tercera propuesta 
    
        winners = {}
        losers = {}

        players = set()

        answer = [[],[]]

        for winner, loser in matches:
            if winner not in players:
                players.add(winner)

            if loser not in players:
                players.add(loser)

            winners[winner] = winners.get(winner,0) + 1 
            losers[loser] = losers.get(loser,0)+1


        for player in players:
            if player not in losers:
                answer[0].append(player)
            elif losers.get(player,0) ==1:
                answer[1].append(player)

        return [sorted(answer[0]), sorted(answer[1])]




        
        
        
        
                
            
    
        
        
        
                