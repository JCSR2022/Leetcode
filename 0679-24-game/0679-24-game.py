class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:

        #use dfs to reduce cards usign operators until find 

        def dfs(nums):
            
            N = len(nums)

            if  N == 1:
                if math.isclose(nums[0], 24.000, abs_tol=0.001):
                    return True 
                else:
                    return False

            for i in range(N):
                for j in range(i+1,N):
                    card_1 = nums[i]
                    card_2 = nums[j]
                    new_cards = []
                    new_cards.append(card_1+card_2)
                    new_cards.append(card_1-card_2)
                    new_cards.append(card_2-card_1)
                    new_cards.append(card_1*card_2)
                    if card_2 != 0 : new_cards.append(card_1/card_2)
                    if card_1 != 0 : new_cards.append(card_2/card_1)
                    
                    next_nums =[ card for k,card in enumerate(nums) if k !=i and k !=j ]
                    for card in new_cards:        
                        next_nums.append(card)
                        if dfs(next_nums):
                            return True
                        next_nums.pop()
                    
            return False

        return dfs(cards)
            
