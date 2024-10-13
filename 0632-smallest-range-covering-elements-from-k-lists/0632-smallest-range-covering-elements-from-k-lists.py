class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
#
#         #brute force
#         # O(n), + nLog(n) 
#         # make a new arr with all nums and index = 1 for the begining of the list 0 in the middle , -1 at end//
#         # sort the new arr, go through the arr cont index, when index == len(nums) save in list  ans,  return [ans[0],ans[-1]]
        
        
#         arr = []  
#         for int_nums in nums:
#             arr.append((int_nums[0],1)) 
#             for num in int_nums[1:-1]:
#                 arr.append((num,0))
#             arr.append((int_nums[-1],-1)) 
#         arr.sort()
        
#         print(arr)
#         return [3,5]
# noooooooooooooooooooooooooooooooooooooooooooooooooo
# ----------------------------------------------------------------

        #multiple pointers aproach

#         pointers = [0]*len(nums)
#         nums_lens = [len(num_arr) for num_arr in nums]
#         min_arr_len = float("inf")
#         min_arr = []
        
#         no_end = True
#         while no_end :
#             arr =[arr_num[p] for arr_num,p in zip(nums,pointers) ] 
#             max_arr_v = max(arr)
#             min_arr_v = min(arr)

#             if max_arr_v-min_arr_v < min_arr_len:
#                 min_arr_len = max_arr_v-min_arr_v
#                 min_arr = [min(arr),max(arr)]

#             pointers[arr.index(min_arr_v)] +=1

#             for p,max_p in zip(pointers,nums_lens):
#                 if p >= max_p:
#                     no_end = False

#         return min_arr
# works but is no good:Time Limit Exceeded
# ------------------------------------------------------------------

# multiple pointers heap aproach

        
        
        #initialization:
        nums_lens = [len(num_arr) for num_arr in nums]
        
        min_heap = []
        max_arr_v = nums[0][0] # any value
        idx = 0
        for i,nun_arr in enumerate(nums):
            max_arr_v = max(max_arr_v,nun_arr[idx])          
            heapq.heappush(min_heap,(nun_arr[idx],i,idx))
            
        min_arr_v = min_heap[0][0]
        ans = [min_arr_v,max_arr_v]
    
        
        #loop:
        while True:
            n,i,idx =  heapq.heappop(min_heap)
        
            idx += 1
            if idx == nums_lens[i]:
                return ans
            
            next_val = nums[i][idx]
            heapq.heappush(min_heap,(next_val,i,idx))
            
            min_arr_v =  min_heap[0][0]
            max_arr_v = max(max_arr_v,next_val)
            
            if max_arr_v - min_arr_v < ans[1] - ans[0]:
                ans = [min_arr_v,max_arr_v]
            
            
        

    
        
        
    





