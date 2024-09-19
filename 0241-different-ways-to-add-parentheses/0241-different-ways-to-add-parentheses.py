class Solution:
    
    def eval_ecu(self,left_val,right_val,op):
        if op == "+": return int(left_val) + int(right_val)
        if op == "-": return int(left_val) - int(right_val)
        return int(left_val) * int(right_val)
        
    
    def diffWaysToCompute(self, expression: str) -> List[int]:
        computed = []
        
        for i, operator in enumerate(expression):
            if operator in "+-*":
                left_compute = self.diffWaysToCompute(expression[:i])
                right_compute = self.diffWaysToCompute(expression[i+1:])
                
                
                for left_val in left_compute:
                    for right_val in right_compute:
                        #print(left_val,right_val,operator)
                        computed.append(self.eval_ecu(left_val,right_val,operator))    
        
        if not computed: return [int(expression)]
        
        return computed
    
    
    