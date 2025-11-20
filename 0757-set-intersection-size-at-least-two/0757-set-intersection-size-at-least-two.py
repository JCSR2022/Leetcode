class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        #https://www.youtube.com/watch?v=la4OkK3pY7o
        #hoy no tengo cerebro
        res = 0
        intervals.sort(key = lambda x:(x[1],-x[0]))
        p1,p2 = -1,-1
        ans = []

        for left,right in intervals:
            if p2 < left:
                ans.append(right-1)
                ans.append(right)
                res +=2
                p1,p2, =right-1,right
            elif p1 < left:
                ans.append(right)
                res += 1
                p1,p2, =p2,right 

        print(ans)
        return  res