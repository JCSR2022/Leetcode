class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        #brute force, try all combinations

        maxArea = 0

        for p1 in points:
            for p2 in points:
                for p3 in points:
                    if p2 != p1 and p3 !=p1 and p3 !=p2:
                        x1, y1 = p1
                        x2, y2 = p2
                        x3, y3 = p3
                        area = abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2
                        maxArea = max(maxArea,area)

        return maxArea