class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        cnt_R = moves.count('R')
        cnt_L = moves.count('L')
        print(cnt_L,cnt_R)

        if cnt_R >= cnt_L:
            return len(moves) - 2*cnt_L 
        else:
            return len(moves) - 2*cnt_R
