class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        def rotate(arr):
            if len(arr)>0:
                arr[:] = [arr[-1]] + arr[:-1]

        deck.sort(reverse=True)    

        arr = []
        for card in deck:
            rotate(arr)
            arr = [card]+arr

        return arr