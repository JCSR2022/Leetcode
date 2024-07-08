class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        winner = 0  # Josephus problem is 0-indexed in calculation
        for i in range(1, n + 1):
            winner = (winner + k) % i
        return winner + 1
        
        
#         #simple non math way, brute, realy brute force  
#         arr = [i for i in range(1,n+1)]
#         #print(arr)
     
#         i = 0
#         while arr:
#             i = (i + k-1)%(len(arr))
#             ans = arr.pop(i)
#             #print(arr)

#         return ans
        