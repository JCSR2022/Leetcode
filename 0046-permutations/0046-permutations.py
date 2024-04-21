class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #return list(itertools.permutations(nums))
        
        
        
        def calc_new_perm(ans,n):
            new_ans = []
            for i in range(len(ans)+1):
                temp_ans = ans.copy() 
                temp_ans.insert(i,n)
                new_ans.append(temp_ans) 
            return new_ans
    
        def calc_all_perm(values,n):
            ans = []
            for val in values:
                ans += calc_new_perm(val,n)
            return ans
        
        
        i = 0
        values =[ [nums[0]]]
        while  i < len(nums)-1:
            #print(values)
            i +=1 
            values = calc_all_perm(values,nums[i])
        
        return  values
        
#         [1,2]
#         [2,1]
        
#         123
#         132
#         312
        
#         213
#         231
#         321
        
# 1234
# 1243
# 1423
# 4123

# 1324
# 1342
# 1432
# 4132
# ....        
        
        
        
        
        
        
        
        
        
        
        