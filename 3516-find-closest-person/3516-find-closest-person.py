class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:

        relative = abs(x-z) - abs(y-z) 
        if relative < 0 :
            return 1
        elif relative == 0:
            return 0
        else:
            return 2
        