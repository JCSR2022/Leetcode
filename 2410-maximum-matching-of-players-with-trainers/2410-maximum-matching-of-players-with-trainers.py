class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        #aproach, sort and two pointers: nlog(n) do to sort

        players.sort(reverse=True)
        trainers.sort(reverse = True)


        count = 0
        p = 0
        t = 0
        while t < len(trainers) and p < len(players):
            if trainers[t] >= players[p]:
                count +=1
                p += 1
                t += 1
            else:
                p += 1


        return count 
