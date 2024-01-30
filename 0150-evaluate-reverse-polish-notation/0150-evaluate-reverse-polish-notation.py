class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operaciones = ['+', '-', '*', '/']
        
        if len(tokens) == 1:
            return int(tokens[0])
        
        def eval_op(str_num1, str_num2, str_operator):
            num1 = int(str_num1)
            num2 = int(str_num2)
            eval_operaciones = {'+': lambda x, y: x + y, 
                           '-': lambda x, y: x - y, 
                           '*': lambda x, y: x * y, 
                           '/': lambda x, y: x / y}
            return eval_operaciones[str_operator](num1, num2)

        i = -1 
        while len(tokens) > 2 :
            i += 1
            if tokens[i] in operaciones:
                ans = eval_op(tokens[i-2] , tokens[i-1] ,tokens[i] )
                tokens[i] = ans
                del tokens[i-2]
                i -=1
                del tokens[i-1]
                i -=1
        return int(tokens[0])
            
        
        