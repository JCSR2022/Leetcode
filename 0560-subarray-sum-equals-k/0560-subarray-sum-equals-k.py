class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:


        size = len(nums)  
        prefix = [0]*size
        prefix[0] = nums[0]
        for i in range(1,size):
            prefix[i] = prefix[i-1]+nums[i]
        
        count = 0
        for n in prefix:
            if n == k:
                count +=1 

        for i in range(size):
            for j in range(i+1,size):
                curr =  prefix[j] - prefix[i]
                if curr == k:
                    count +=1 

        return count

#-------------------------------------------------------------------
        # size = len(nums)
        # count  = 0
        # curr_sum = 0
        # previos_sum_record = defaultdict(int)
        
        # for i in range(size):
        #     curr_sum += nums[i]
        #     previos_sum_record[curr_sum] += 1
        #     previos_valid =  curr_sum - k 
        #     if previos_valid in previos_sum_record:
        #          count  = previos_sum_record[previos_valid]
        #     print(i,curr_sum,dict(previos_sum_record),previos_valid,count)     
        # return count


#noooooooo
#----------------------------------------------------------------
        #brute force as always, the only thing you can do

        # size = len(nums)
        # count  = 0
        # for i in range(size):
        #     for j in range(i+1,size+1):
        #         print(nums[i:j],sum(nums[i:j]))
        #         if sum(nums[i:j]) == k:
        #             count +=1
        # return count



        # size = len(nums)
        # count  = 0
        # for i in range(size):
        #     curr_sum = 0
        #     for j in range(i,size):
        #         curr_sum +=nums[j]
        #         if curr_sum == k:
        #             count +=1
        # return count





#--------------------------------------------------------------
        # record_sums = defaultdict(int)        

        # for n in nums:

        #     new_records = defaultdict(int)
        #     for record in record_sums.keys():
        #         new_records[record+n] +=1
        #     for record in new_records:
        #         record_sums[record] += new_records[record]
            
        #     record_sums[n] += 1

        #     print(dict(record_sums)) 

        # return record_sums[k]

#no imbecil!!!!!!!!!
#------------------------------------------------------------------------------------

















#------------------------------------------------------------------------

        # #https://www.youtube.com/watch?v=fFVZt-6sgyo
        
        # res = 0
        # curSum = 0
        # prefixSums = {0:1}
        
        # for n in nums:
        #     curSum += n
        #     diff = curSum - k
            
        #     res += prefixSums.get(diff,0)
        #     prefixSums[curSum] = 1 + prefixSums.get(curSum,0)
            
        # return res
        
        
        
#         #print(nums,k)
#         suma = [0]
#         acum = 0
#         cont = 0
#         for elem in nums:
#             if elem == k : cont +=1
#             acum += elem
#             suma.append(acum)
#         print(suma)
#         for i,elem in enumerate(suma):
#             diff = elem - k
#             print(i,elem,diff, suma[:i],diff in suma[:i])
#             if diff in suma[:i]:
#                 cont +=1
            
#         return cont



