class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        #aproach, there are 9 areas where thr center of the circle can be:


        # def dist2d(x1,y1,x2,y2):
        #     return math.sqrt( (x2-x1)**2 + (y2-y1)**2 )

        # def dist1d(a,b):
        #     return abs(a-b)

        # if xCenter < x1 and yCenter < y1:
        #     return dist2d(x1,y1,xCenter,yCenter) >= radius 

        # if xCenter < x1 and y2 >= yCenter >= y1:
        #     return dist1d(xCenter,x1) >= radius

        # if xCenter < x1 and y2 < yCenter:
        #     return dist2d(x1,y2,xCenter,yCenter) >= radius 

        # if x2 >= xCenter >= x1 and y2 < yCenter:
        #     return dist1d(yCenter,y2) >= radius

        # if x2 < xCenter and y2 < yCenter:
        #     return dist2d(x2,y2,xCenter,yCenter) >= radius

        # if x2 < xCenter and y2 >= yCenter >= y1:
        #     return dist1d(xCenter,x2) >= radius
        
        # if x2 < xCenter and yCenter < y1:
        #     return dist2d(x2,y1,xCenter,yCenter) >= radius

        # if x2 >= xCenter >= x1 and yCenter < y1:
        #     return dist1d(yCenter,y1) >= radius

        # return True
        

#-------------------------------------------------------------------

        # Find the closest point in the rectangle
        # to the center of the circle.
        closestX = max(x1, min(xCenter, x2))
        closestY = max(y1, min(yCenter, y2))

        # Calculate squared distance.
        dx = xCenter - closestX
        dy = yCenter - closestY

        distance2 = dx * dx + dy * dy

        # Overlap occurs when the closest point
        # is inside or exactly on the circle.
        return distance2 <= radius * radius
    
        