class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        new_s = s+s
        
        return len(s) == len(goal) and  goal in new_s
        
        