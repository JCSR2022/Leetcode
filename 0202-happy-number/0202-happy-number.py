class Solution:
    def isHappy(self, n: int) -> bool:

        result = [n]
        while True:
            n = sum([ int(i)**2 for i in str(n)])
            if n == 1:
                return True
            if n in result:
                return False
            else:
                result.append(n)
   
                
            
  