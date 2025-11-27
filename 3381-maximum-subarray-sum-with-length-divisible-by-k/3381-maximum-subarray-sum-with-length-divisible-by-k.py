class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        
        """
        nums = [-5,1,2,-3,4,-1,5], k =3
        3 1 0 [-5, 1, 2] -2
        4 1 1 [1, 2, -3] 0
        5 1 2 [2, -3, 4] 3
        6 2 0 [-3, 4, -1] 0
        7 2 1 [4, -1, 5] 8
        {0: [-2, 0], 1: [0, 8], 2: [3]}
        """

        k_sum = defaultdict(list)
        curr_sum = sum(nums[:k])
        k_sum[0].append(curr_sum)

        for i in range(1,len(nums)-k+1):
            curr_sum -= nums[i-1]
            curr_sum += nums[i+k-1]
            k_sum[i%k].append(curr_sum)

        #print(dict(k_sum))

        max_sum = k_sum[0][0]
        
        for arr in k_sum.values():
            curr_sum = arr[0]
            max_sum = max(max_sum,curr_sum)
            for i in range(1,len(arr)):
                curr_sum += arr[i]
                if  curr_sum < arr[i]:
                    curr_sum = arr[i]
                max_sum = max(max_sum,curr_sum)
            

        return max_sum



        # k_sum = defaultdict(list)
        # curr_sum = sum(nums[:k])

        # for i in range(k,len(nums)):
        #    k_sum[i%k].append(curr_sum)
        #    curr_sum += nums[i]
        #    curr_sum -= nums[i-k]
        #    print(i,i//k,i%k,nums[i-k:i],sum(nums[i-k:i])) 
        # k_sum[i%k].append(curr_sum)   
            
        # print(dict(k_sum))



        # k_sum = defaultdict(list)
        # for i in range(k,len(nums)+1):
        #    k_sum[i%k].append(sum(nums[i-k:i]))
        #    print(i,i//k,i%k,nums[i-k:i],sum(nums[i-k:i])) 
        # print(dict(k_sum))


#-------------------------------------------------------------------------
        #brute force


        # curr_k = k
        # max_sum = float("-inf")

        # while curr_k <= len(nums):
        #     curr_sum = sum(nums[:curr_k])
        #     max_sum = max(max_sum,curr_sum)

        #     for i in range(curr_k,len(nums)):
        #         curr_sum += nums[i]
        #         curr_sum -= nums[i-curr_k]
        #         max_sum = max(max_sum,curr_sum)
            
        #     curr_k += k

        # return max_sum

#Time Limit Exceeded, imbecil!!!
#--------------------------------------------------------





        






        # if k == 1:
        #     curr_sum = nums[0]
        #     max_sum = curr_sum 
        #     for i in range(1,len(nums)):
        #         curr_sum += nums[i]
        #         if curr_sum < nums[i]:
        #             curr_sum = nums[i]
        #         max_sum = max(max_sum,curr_sum)
        #     return max_sum
        
        # else:
        #     size = k*(len(nums)//k)
        #     max_sum = sum(nums[:size])
        #     curr_sum = max_sum 

        #     for i in range(size,len(nums)):
        #         print(i,curr_sum,max_sum)
        #         curr_sum -= nums[i-size]
        #         curr_sum += nums[i]
        #         max_sum = max(max_sum,curr_sum)
        #     print(curr_sum,max_sum)

        #     return max_sum
        