class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        #Aproach: O(n)+klog(k)
        N = len(nums)
        ans = set()

        for i in range(N):
            if nums[i] == key:
                for j in range(max(i-k,0),min(i+k+1,N)): 
                    ans.add(j)
        return sorted(list(ans))

#----------------------------------------------------------------
        # #Aproach: 2*O(n)+klog(k)
        # N = len(nums)
        # ans = set()

        # #Left_right
        # cur_k = 0
        # for i in range(N):
        #     if nums[i] == key:
        #         cur_k = k+1
        #     if  cur_k > 0:
        #         cur_k -=1
        #         ans.add(i)
           
        # #right_left
        # cur_k = 0
        # for i in range(N-1,-1,-1):
        #     if nums[i] == key:
        #         cur_k = k+1
        #     if  cur_k > 0:
        #         cur_k -=1
        #         ans.add(i)
        
        # return sorted(list(ans))


#---------------------------------------------------------------
        # #Aproach: 3*O(n)
        # N = len(nums)
        # flags = [0]*N

        # #Left_right
        # cur_k = 0
        # for i in range(N):
        #     if nums[i] == key:
        #         cur_k = k+1
        #     if  cur_k > 0:
        #         cur_k -=1
        #         flags[i] = 1
           
        # #right_left
        # cur_k = 0
        # for i in range(N-1,-1,-1):
        #     if nums[i] == key:
        #         cur_k = k+1
        #     if  cur_k > 0:
        #         cur_k -=1
        #         flags[i] = 1
        
        # return [ i for i,f in enumerate(flags) if f]


        
        