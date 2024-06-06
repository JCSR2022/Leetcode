class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #brute brute force:
        
        
        
        def isConsecutive(group):
            #print('group',group)
            
            if len(group) <= 1:
                return True
    
            for i in range(1,len(group)):
                if group[i] != group[i-1] + 1:
                    return False
            return True
                
        #print(len(hand),groupSize,len(hand)%groupSize)
        
        if len(hand)%groupSize != 0:
            return False
        
        
        hand.sort()
        #print(hand)
        
        group_sortHand = [ [] for _ in range(len(hand)//groupSize) ]
        
        for card in hand:
            for group in group_sortHand:
                if card not in group and len(group)<groupSize:
                    group.append(card)
                    break
        
        #print(group_sortHand)
        
        
        for group in group_sortHand:
            if len(group) != groupSize:
                return False
            if not isConsecutive(group):
                return False

        return True
    
    
    
    
    
    
    
    