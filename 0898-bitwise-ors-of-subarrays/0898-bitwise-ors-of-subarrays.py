class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        #brute force n**2
        # n = len(arr)
        # ans = set()
        # for i in range(n):
        #     currBitOr = arr[i]
        #     for j in range(i,n):
        #         currBitOr |= arr[j]
        #         ans.add(currBitOr)
        # return len(ans)         

#Time Limit Exceeded
#--------------------------------------------------------
     #2d aproach instead of making n**2 will be n*(ans)


        # n = len(arr)
        # prev_ans = set()
        # for currBitOr in arr:
        #     curr_ans = set([currBitOr])
        #     for prev in prev_ans :
        #         print("#### ",currBitOr,prev, currBitOr | prev )
        #         curr_ans.add(currBitOr | prev)
        #     prev_ans = prev_ans | curr_ans
        #     print(currBitOr,prev_ans)

        # return len(prev_ans)      

#NOOOOOOOOOOOOOOOOOOOOOOOOo
# ------------------------------------------------        
   
        result_ors = set()
        current_ors = set()
   
        for x in arr:
   
            next_ors = {x | y for y in current_ors}
            next_ors.add(x) 
            result_ors.update(next_ors)
            current_ors = next_ors
            
        return len(result_ors)

