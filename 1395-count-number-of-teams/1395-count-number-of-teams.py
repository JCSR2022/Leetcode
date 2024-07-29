class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        #kartikdevsharmaa solution index binary tree??
        #i am not even trying today , i feel as a pice of @$#$@#$@#
        
        
        n = len(rating)
        if n < 3:
            return 0
        
        soldiers = sorted([(r, i) for i, r in enumerate(rating)])
        index_map = [0] * n
        for i, (_, idx) in enumerate(soldiers):
            index_map[idx] = i
        
        def count_teams(ascending: bool) -> int:
            bit = [0] * (n + 1)
            teams = 0
            
            for i in range(n):
                rank = index_map[i] + 1
                left = self.get_sum(bit, rank - 1) if ascending else self.get_sum(bit, n) - self.get_sum(bit, rank)
                right = n - rank - (self.get_sum(bit, n) - self.get_sum(bit, rank)) if ascending else rank - 1 - self.get_sum(bit, rank - 1)
                teams += left * right
                self.update(bit, rank, 1)
            
            return teams
        
        return count_teams(True) + count_teams(False)
    
    def update(self, bit: List[int], index: int, val: int) -> None:
        while index < len(bit):
            bit[index] += val
            index += index & (-index)
    
    def get_sum(self, bit: List[int], index: int) -> int:
        total = 0
        while index > 0:
            total += bit[index]
            index -= index & (-index)
        return total

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Dinamic programing//
        #??????????????
        
        
        
        
        
        # # do not work for time limit
        # #brute force, make every combination of 3 pointers review if comply whit req
        # size = len(rating)
        # ans = 0
        # for i in range(size):
        #     for j in range(i+1,size):
        #         for k in range(j+1,size):
        #             cond1 = rating[i] > rating[j] > rating[k]
        #             cond2 = rating[i] < rating[j] < rating[k]
        #             if cond1 or cond2:
        #                 ans +=1
        #                 #print(i,j,k,[rating[i],rating[j],rating[k]])
        # return ans