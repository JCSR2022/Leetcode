class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # first order by  points[[X,]]
        # 2d merge if posible contiguos elements
        
        points.sort(key=lambda item:item[1])
        
        merge_points = []
        L = points[0][0]
        R = points[0][1]
        for i in range(1,len(points)):
            if R < points[i][0]:
                merge_points.append([L,R])
                L = points[i][0]
                R = points[i][1]

            elif R == points[i][0]:
                L = R

            elif R > points[i][0]:
                L = max(points[i][0],L)

        merge_points.append([L,R])  
        
        return len(merge_points)