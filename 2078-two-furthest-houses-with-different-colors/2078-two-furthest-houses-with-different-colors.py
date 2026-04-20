class Solution:
    def maxDistance(self, colors: List[int]) -> int:

        #O n**2, fuck#@$@
        #aproach save indx first apperance color and last

        left = defaultdict(int)
        right = defaultdict(int)

        for i,color in enumerate(colors):
            if color not in left:
                left[color] = i
            else:
                right[color] = i

        if len(right) == 0:
            return len(colors)-1

        ans = 1
        for colorL,indxL in  left.items():
            for colorR,indxR in right.items():
                if colorR != colorL:
                    ans = max(ans,abs(indxR-indxL))

        return ans

        

        


        