class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        # if the first position is not the smallest there 
        #    is no way to turn on all the computers
        # and the answer is the permute of al possible combinations:
        #   example:
        #       [0,1,2]..[0,1,2], [0,2,1] =>2 (2!)
        #       [0,*,$,%]..[0,*,$,%],[0,*,%,$],[0,$,*,%],[0,$,%,*],[0,%,*,$],[0,%,$,*] =>6 (3!)
        #      

        MOD = 10**9+7
        def fact_Mod(n):
            if n==1:
                return 1
            return (n*fact_Mod(n-1))%MOD

        def first_only_min(arr):
            target = arr[0]
            cnt_min =0 
            min_val = float("inf")
            for val in arr:
                if  val < min_val:
                    min_val = val
                    cnt_min = 1
                elif  val == min_val:
                    cnt_min += 1

            return ( (min_val == target) and (cnt_min ==1) )



        if first_only_min(complexity):
            return fact_Mod(len(complexity)-1)
        else: 
            return 0
