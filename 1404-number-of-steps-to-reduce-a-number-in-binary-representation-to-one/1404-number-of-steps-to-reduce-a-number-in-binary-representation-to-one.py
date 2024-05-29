class Solution:
    def numSteps(self, s: str) -> int:
        #aproach:
        #  in binary rep divide by 2 is to move 1 bit to the left 
        #  100  = 4    010 =  2   //   10011   +1 ->   10100      
        
        #brute force:
        
        def addOne(bin_num:str):
            bin_num = list(bin_num)
            for i in range(len(bin_num)-1,-1,-1):
                #print(i,bin_num)
                if bin_num[i] == '1': bin_num[i] = '0'
                elif bin_num[i] == '0': 
                    bin_num[i] = '1'
                    #print(1,i,bin_num)
                    return ''.join(bin_num)
            return '1'+ ''.join(bin_num)
        
        def divTwo(bin_num:str):
            return '0' + bin_num[:-1]
            
        
        ans = 0
        while True or ans<10000000:
            if s.count('1') == 1 and s[-1] == '1':
                return ans
            
            ans +=1
            
            if s[-1] == '0': 
                s = divTwo(s)
            else:
                s = addOne(s)
                
                
            
        
        
        