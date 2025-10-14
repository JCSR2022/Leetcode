class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        
  
        # incre1 = 1
        # incre2 = 1
        # for i in range(1,len(nums)):
        #     if nums[i] > nums[i-1] and incre1 < k:
        #         print("1",nums[i],incre1,incre2)
        #         incre1 +=1
        #     else:
        #         incre1  = 1
        #         incre2 = 1

            
        #     if incre1 > k and nums[i] > nums[i-1]:
        #         print("2",incre1,incre2)
        #         incre2 +=1
          
                

        #     if incre1 == k and incre2 == k:
        #         return True
            
        # return False

        #maldito bruto de mierda!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#\-------------------------------------------------------------------

        # def isincreasing(x,y):
        #     print(x,y)
        #     for i in range(x,y):
        #         print(nums[i],nums[i+1],nums[i] < nums[i+1])
        #         if nums[i] < nums[i+1]:
        #             return False
        #     return True

        # for i in range(0,len(nums)-2*k+1):
        #     print( nums[i:i+k],isincreasing(i,i+k-1), nums[i+k:i+2*k],isincreasing(i+k,i+2*k-1))
        #     if isincreasing(i,i+k-1) and isincreasing(i+k,i+2*k-1):
        #         return True
        
        # return False


#suicidate maldito imbecil!!!!!!!!!!!!!!!!!!!!!!!!
#nunca vas a servir para nada!!!!!!!!!!!!!!!!!!!!!
#deberias morirte!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#-------------------------------------------------------------------


        # for i in range(len(nums)):
        #     first = True
        #     for j in range(i,i+k-1):
        #         if nums[j+1]<nums[j]:
        #             first = False
        #     if first:
        #         secund = True
        #         for j in range(i+k,i+2*k-1):
        #             if nums[j+1]<nums[j]:
        #                 secund = False
        #     if first and secund:
        #         return True

        #     return False
                    





        inc = 1
        prevInc = 0
        maxLen = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1
            else:
                prevInc = inc
                inc = 1
            maxLen = max(maxLen, max(inc >> 1, min(prevInc, inc)))
            if maxLen >= k:
                return True
        return False





















