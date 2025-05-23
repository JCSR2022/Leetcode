class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:

        # #brute force, try all cahnges in deges n*edg**2 
        # N_edg = len(edges)

        # def recursion(i,curr_nums,ans):
    
        #     if i == N_edg:
        #         #print(ans,curr_nums,sum(curr_nums))
        #         return sum(curr_nums)
                
        #     #use
        #     u = edges[i][0]
        #     v = edges[i][1]
        #     previus_u = curr_nums[u]
        #     previus_v = curr_nums[v]
        #     curr_nums[u] =  curr_nums[u]^k
        #     curr_nums[v] =  curr_nums[v]^k
        #     ans.append(edges[i])
        #     op1 = recursion(i+1,curr_nums,ans)
        #     ans.pop()

        #     #not use
        #     curr_nums[u] =  previus_u
        #     curr_nums[v] =  previus_v
        #     op2 = recursion(i+1,curr_nums,ans)
            
        #     return max(op1,op2)

        # return recursion(0,nums,[])

#Time Limit Exceeded
#----------------------------------------------------------------

 
        # #https://www.youtube.com/watch?v=bnBp6_b4GCw
        
        delta = [ (n ^ k) - n for n in nums ]
        delta.sort(reverse = True)
        
        res = sum(nums)
        
        for i in range(0,len(nums),2):
            
            if i == len(nums)-1:
                break
            
            path_delta = delta[i] + delta[i+1]
            
            if path_delta <= 0:
                break
            
            res += path_delta
            
        
        return res