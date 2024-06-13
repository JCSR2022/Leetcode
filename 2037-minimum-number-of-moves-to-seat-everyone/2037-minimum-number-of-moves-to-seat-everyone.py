class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        # brute force sort and diff
        
        seats.sort()
        students.sort()
        
        return sum( [abs(se-st) for se,st in zip(seats,students) ] )
        
#         moves = 0
#         for se,st in zip(seats,students):
#             moves += abs(se-st)
        
#         return moves