class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cont = 0
        for passanger_info in details:
            if int(passanger_info[-4:-2]) > 60:
                cont +=1
        return cont
                    
                
                    