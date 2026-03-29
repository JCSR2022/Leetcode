class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:

        for i in range(2):
            if [s1[i],s1[i+2]] != [s2[i],s2[i+2]] and [s1[i],s1[i+2]] != [s2[i+2],s2[i]]:
                return False
        return True
        