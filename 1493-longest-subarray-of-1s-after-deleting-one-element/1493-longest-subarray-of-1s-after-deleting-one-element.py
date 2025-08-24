class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        #sliding window if cnt_cero >2 move mantain max cnt_ones



    
        prev_ones = 0
        curr_ones = 0 
        ans = 0
        for n in nums:
            if n:
                curr_ones +=1
                ans = max(ans, prev_ones + curr_ones )
            else:
                if curr_ones > 0 :
                    prev_ones = curr_ones 
                    curr_ones = 0
                else :
                    prev_ones = 0
                    curr_ones = 0 
            
        ans = max(ans,curr_ones-1)
        return ans if ans < len(nums) else ans-1








        #----------------------------------------
        # groupsOnes = []
        # cnt_ones = 0
        # for n in nums:
        #     if n:
        #         cnt_ones +=1
        #     else:
        #         if cnt_ones>0:
        #             groupsOnes.append(cnt_ones)
        #             cnt_ones = 0 
        
        # if cnt_ones>0:
        #     groupsOnes.append(cnt_ones)
        
        # print(groupsOnes)

        # if len(groupsOnes) == 0:
        #     return 0
        # elif len(groupsOnes) == 1:
        #     return max(0,groupsOnes[0]-1)
        # else:
        #     ans = 0
        #     for i in range(len(groupsOnes)):
        #         ans = max(ans,groupsOnes[i]+groupsOnes[i-1])    
        #     return ans
        #noooooooooo

        #----------------------
        # l = 0 
        # cnt_cero_1 = 0
        # cnt_cero_2 = 0
        
        # cnt_one_1 = 0
        # cnt_one_2 = 0
        # ans = 0
        # for r in range(len(nums)):
        #no
        #-----------------------
        