class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        
        # #hash_nums will be unique and already sort    
        # hash_nums = defaultdict(list)
        # for i,n in enumerate(nums):
        #     hash_nums[n].append(i)

        # size = len(nums)

        # ans = [-1]*len(queries)
        # for i,q in enumerate(queries):
        #     if len(hash_nums[nums[q]]) > 1:
        #         indx =  hash_nums[nums[q]].index(q)
        #         if indx == 0:
        #             ans[i] = min(hash_nums[nums[q]][1],size-hash_nums[nums[q]][-1])

        #         elif indx == len(hash_nums[nums[q]])-1:
        #             ans[i] = min(hash_nums[nums[q]][-1]-hash_nums[nums[q]][-2],abs(size-hash_nums[nums[q]][-1]-size-hash_nums[nums[q]][0]))
                
        #         else:
        #             ans[i] = min( hash_nums[nums[q]][indx]-hash_nums[nums[q]][indx-1],  hash_nums[nums[q]][indx+1]-hash_nums[nums[q]][indx]   )
        # return ans

#esto es una mierda!!! como tu!!!!!
#------------------------------------------


        # #hash_nums will be unique and already sort    
        # hash_nums = defaultdict(list)
        # for i,n in enumerate(nums):
        #     hash_nums[n].append(i)

        # size = len(nums)
        # ans = [-1]*len(queries)
        # for i,q in enumerate(queries):
        #     indices = hash_nums[nums[q]] 
        #     if len(indices) > 1:
        #         indices_indx = indices.index(q)

        #         if indices_indx == 0:
        #             l_dist = size - indices[-1] + q
        #         else:
        #             l_dist = indices[indices_indx]-indices[indices_indx - 1]

        #         if indices_indx == len(indices)-1:
        #             r_dist = size - indices[-1] +q
        #         else:
        #             r_dist = indices[indices_indx+1]-indices[indices_indx]

        #         ans[i] = min(l_dist,r_dist)
        
        # return ans




#-------------------------------------------------

        
        pos = defaultdict(list)
        for i, n in enumerate(nums):
            pos[n].append(i)

        n = len(nums)
        ans = []

        for q in queries:
            indices = pos[nums[q]]
            
            if len(indices) == 1:
                ans.append(-1)
                continue

            i = indices.index(q)

            prev_idx = indices[i - 1] if i > 0 else indices[-1]
            next_idx = indices[i + 1] if i < len(indices) - 1 else indices[0]

            dist_prev = min(abs(q - prev_idx), n - abs(q - prev_idx))
            dist_next = min(abs(q - next_idx), n - abs(q - next_idx))

            ans.append(min(dist_prev, dist_next))

        return ans
