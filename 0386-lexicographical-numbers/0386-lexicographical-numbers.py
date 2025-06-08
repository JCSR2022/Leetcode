class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        #jun 07 2025

        # ans = []
        # def recursive(i:str):
        #     if int(i) <= n:
        #         ans.append(int(i))
        #         for j in ['0','1','2','3','4','5','6','7','8','9']:
        #             cur_num = int(i+j) 
        #             recursive(i+j)
        # for i in ['1','2','3','4','5','6','7','8','9']:
        #     recursive(i)
        # return ans     

#--------------------------------------------------


             
        ans = [ str(x) for x in range(1,n+1)]
        ans.sort()
        return [int(x) for x in ans]
    
    
    #---------------------------------------------------
    
    
        #1 always comes first, and we fill in all the ones that exist,
        #if it gets greater than n, then we finish
        # ans = []
        
        # def recursive(value):
        #     print(value,ans)
        #     if len(ans) >= n:
        #         return
        #     ans.append(value)
        #     if (value * 10) <= n:
        #         recursive(value * 10)
        #     if value + 1 <= n and int(str(value)[-1]) < 9:
        #         recursive(value + 1)
                
        # recursive(1)

        # return ans