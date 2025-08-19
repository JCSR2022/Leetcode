class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        #2*O(n)


        
        cnt_ceros =[]
        curr_cnt = 0
        for n in nums:
            if n == 0 :
                curr_cnt += 1
                continue
            else:
                if curr_cnt != 0:
                   cnt_ceros.append(curr_cnt) 
                   curr_cnt = 0
        if curr_cnt != 0: cnt_ceros.append(curr_cnt)             
        
        ans = 0
        for size_ceros in cnt_ceros:
            ans += size_ceros*(size_ceros+1)//2


        return ans

      

