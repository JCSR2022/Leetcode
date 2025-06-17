class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        
        #brute force: O(2**n) will not work but just to visualize
        #backtrack all posible combinations

        MOD = 10**9 + 7


        my_memory = {}
        def backtrack(i,prev_num,pairs_k):
            if (i,prev_num,pairs_k) in my_memory:
                return my_memory[(i,prev_num,pairs_k)]
            
            if i == n:
                if pairs_k == k:
                    return 1
                else:
                    return 0
            ans = 0
            for j in range(1,m+1):
                curr_k_add = 1 if prev_num == j else 0 
                cur_pairs_k = pairs_k+curr_k_add 
                if cur_pairs_k <= k:
                    ans += backtrack(i+1,j,pairs_k+curr_k_add)

            my_memory[(i,prev_num,pairs_k)] = ans%MOD
            return my_memory[(i,prev_num,pairs_k)]

        return backtrack(0,-1,0)


























#--------------------------------------------------------------------
        # all_arr = []
        # def backtrack(i,prev_num,pairs_k,curr_arr):
        #     if i == n:
        #         if pairs_k == k:
        #             all_arr.append(curr_arr)
        #             return 1
        #         else:
        #             return 0


        #     ans = 0
        #     for j in range(1,m+1):
        #         curr_k_add = 1 if prev_num == j else 0 
        #         cur_pairs_k = pairs_k+curr_k_add 
        #         if cur_pairs_k <= k:
        #             ans += backtrack(i+1,j,pairs_k+curr_k_add,curr_arr+[j])

        #     return ans

        # ans = backtrack(0,-1,0,[])
        
        # print(all_arr)
        # return ans