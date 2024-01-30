class Solution:
    def isHappy(self, n: int) -> bool:
        
        def calc_happy(n):
            return  sum([ int(i)**2 for i in str(n)])
        
        cont = 0
        result = [n]
        while cont < 1000000:
            n = calc_happy(n)
            if n == 1:
                return True
            if n in result:
                return False
            else:
                result.append(n)
            cont +=1
                
            
  