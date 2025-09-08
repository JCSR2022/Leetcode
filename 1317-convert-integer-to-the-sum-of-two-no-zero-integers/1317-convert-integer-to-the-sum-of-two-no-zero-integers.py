class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:

        # #just for fun
        # a = random.randint(1,n-1)
        # return [a,n-a]
        
        a = n-1
        while str(a).count("0") > 0  or str(n-a).count("0") > 0 :
            a -=1

        return   [a,n-a]
        