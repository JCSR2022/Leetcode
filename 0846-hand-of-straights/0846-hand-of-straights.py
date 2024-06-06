class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        # https://www.youtube.com/watch?v=amnrMCVd2YI
        
        if len(hand) % groupSize:
            return False
        
        count = {}
        for n in hand:
            count[n] = 1 + count.get(n,0)
            
            
        minH = list(count.keys())
        heapq.heapify(minH)
        
        
        while minH:
            first = minH[0]
            
            for i in range( first,first+groupSize ):
                if i not in count:
                    return False
                count[i] -=1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
                    
        return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #brute brute force:   
#         def isConsecutive(group):
#             #print('group',group)
            
#             if len(group) <= 1:
#                 return True
    
#             for i in range(1,len(group)):
#                 if group[i] != group[i-1] + 1:
#                     return False
#             return True
                
#         #print(len(hand),groupSize,len(hand)%groupSize)
        
#         if len(hand)%groupSize != 0:
#             return False
        
        
#         hand.sort()
#         #print(hand)
        
#         group_sortHand = [ [] for _ in range(len(hand)//groupSize) ]
        
#         for card in hand:
#             for group in group_sortHand:
#                 if card not in group and len(group)<groupSize:
#                     group.append(card)
#                     break
        
#         #print(group_sortHand)
        
        
#         for group in group_sortHand:
#             if len(group) != groupSize:
#                 return False
#             if not isConsecutive(group):
#                 return False

#         return True
    
    
    
    
    
    
    
    