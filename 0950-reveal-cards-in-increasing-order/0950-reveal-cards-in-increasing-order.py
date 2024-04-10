class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
#         def rotate(arr):
#             if len(arr)>0:
#                 arr[:] = [arr[-1]] + arr[:-1]

#         deck.sort(reverse=True)    

#         arr = []
#         for card in deck:
#             rotate(arr)
#             arr = [card]+arr

#         return arr

        deck.sort(reverse=True)   
        arr = deque()
        for card in deck:
            arr.rotate(1) 
            arr.appendleft(card)
            
        return list(arr)