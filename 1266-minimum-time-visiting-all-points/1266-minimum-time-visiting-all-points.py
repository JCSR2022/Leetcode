class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:


        #aproach , the min distance between 2 point will be x1,y1 and x2,y2 
        # d = max( abs(x1-x2),abs(y1-y2) )

        size = len(points)
        if size == 1:
            return 0

        ans = 0
        for i in range(1,size):
            ans += max( abs(points[i][0]-points[i-1][0]),abs(points[i][1]-points[i-1][1]))
        return ans

        