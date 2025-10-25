class Solution:
    def totalMoney(self, n: int) -> int:

        saving = 0
        week = 0
        for day in range(n):
            if day%7 == 0:
                week = day//7 + 1
                saving += week 
            else:
                week +=1
                saving += week

        return saving
                



        