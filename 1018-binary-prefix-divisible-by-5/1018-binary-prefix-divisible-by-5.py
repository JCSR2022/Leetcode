class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:


        val = 0
        ans = []
        for n in nums:
            val = val*2 + n
            ans.append(val)
            #print(ans)
        return [ val%5 == 0 for val in ans  ]



        #Mas rapido es:
        
        # val = 0
        # for i in range(len(nums)):
        #     val = ((val << 1) + nums[i]) % 5
        #     nums[i] = val == 0
        # return nums




#---------------------------------------------------------------
        # ans = []
        # for i in range(len(nums)):
        #     curr_num = 0
        #     for j,k in enumerate(range(i,-1,-1)):
        #         curr_num += nums[k]*(2**j)
        #     ans.append(curr_num%5 == 0)

        # return ans

#Time Limit Exceeded as expected 


#--------------------------------------------------------------------------

        # size = len(nums)
        # print("size:",size,"range:",list(range(size-2,-1,-1)))
        # curr_num = sum([ n*(2**i) for i,n in enumerate(nums[::-1])] )
        # print(curr_num)
        # ans = [False]*size
        # ans[-1] = curr_num%5 == 0 
        # print("ans:",ans)
        # for i in range(size-2,-1,-1):
        #     print(i,nums[i+1], (2**i),nums[i+1]*(2**i))
        #     #print(f"{curr_num}-{nums[i+1]*(2**(i+1))} ={curr_num-nums[i+1]*(2**(i+1))}" )
        #     # curr_num -= nums[i+1]*(2**(i+1))
        #     # ans[i] = curr_num%5 == 0
        #     # print("ans:",ans)
            

        # return ans

#que basura que eres , no puedes ni con uno facil!!! Imbecil!!!!!!
#muerete, muerete mil veces, no sirves para nada, nunca serviras para una mierda, suicidate imbecil!!!!
#-----------------------------------------------------------------
        # curr_num = 0
        # ans = []
        # for i,n in  enumerate(nums):
        #     curr_num += n*(2**i)
        #     ans.append(curr_num%5==0)
        #     print((i,n,n*(2**i)),curr_num,ans)

        # return ans













        # curr_num = 0
        # ans = []
        # for i,n in  enumerate(nums):
        #     curr_num += n*(2**i)
        #     ans.append(curr_num%5==0)
        #     print((i,n,n*(2**i)),curr_num,ans)

        # return ans

