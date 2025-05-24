class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:

        Q = len(queries)
        queries.sort(key=lambda x: (x[0], -(x[1] - x[0])))  # prioriza inicio bajo, rango largo

        q = 0
        in_use = []
        potential = []
        used_count = 0

        for i, need in enumerate(nums):
            # Agrega queries que comienzan en o antes de i
            while q < Q and queries[q][0] <= i:
                heapq.heappush(potential, -queries[q][1])  # max heap por final
                q += 1

            used_this_round = 0
            # Usa queries para cubrir posición i hasta que haya suficientes activas
            while len(in_use) < need and potential:
                end = -heapq.heappop(potential)
                if end >= i:
                    heapq.heappush(in_use, end)
                    used_this_round += 1

            if len(in_use) < need:
                return -1  # no hay suficientes queries para cubrir

            used_count += used_this_round

            # Limpia queries que ya no cubren más
            while in_use and in_use[0] <= i:
                heapq.heappop(in_use)

        return Q - used_count



#-----------------------------------------------------------------------------------
        # Q = len(queries)
        # q_sort = sorted(queries, key=lambda x: (x[0], -(x[1] - x[0])))
        # q = 0

        # heap_q_in_use  = []
        # heap_potential = []
        # count_q =  0

        # for i,n in enumerate(nums):
        #     #print("i,n:",i,n)
        #     #save queries can use begining in i
        #     while q < Q and q_sort[q][0] <= i:
        #           heapq.heappush(heap_potential ,-q_sort[q][1])
        #           q += 1
        #     #print("heap_potential:",heap_potential )

        #     #use necesary queries always take max right on potential queries
        #     curr_q_use = 0
        #     while heap_potential and n > len(heap_q_in_use): 
        #         most_right = -heapq.heappop(heap_potential)
        #         if most_right >= i:
        #             heapq.heappush(heap_q_in_use, most_right )
        #             curr_q_use +=1 
        #     #print("heap_q_in_use:",heap_q_in_use)    
            
        #     if n > len(heap_q_in_use):
        #         return -1
        #     else:
        #         #update max quantity of queries to use
        #         count_q += curr_q_use

        #         #remove queries no longer valids
        #         while heap_q_in_use and heap_q_in_use[0] <= i:
        #             heapq.heappop(heap_q_in_use)


        # return Q-count_q




#----------------------------------------------------------------------------

            #aproach ,  heap: heap_q_in_use
            # 1 sort queries, and create index q
            # create heap_q_in_use   
            # for i,n in  enumerate(nums), 
            #        while n < len(heap) and i>=  q_sort[q][0]
            #            heappush(q_sort[q][1]) ; q +=1

            # Q = len(queries)
            # q_sort = sorted(queries, key=lambda x: (x[0], -(x[1] - x[0])))
            # q = 0
            # #print(q_sort)

            # heap_q  = []
            # count_q =  0

            # for i,n in enumerate(nums):
            #     print("i,n,heap_q:",i,n,heap_q,n > len(heap_q),i >= q_sort[q][0])
            #     while n > len(heap_q) and i >= q_sort[q][0]:
            #         print("q:",q)
            #         heapq.heappush(heap_q,q_sort[q][1])
            #         if q < Q-1: 
            #             count_q += 1
            #             q +=1
            #         else:
            #             break
                    
            #     print("count_q,q,heap_q:",count_q,q,heap_q)

            #     if n > len(heap_q):
            #         return -1

            #     while heap_q and heap_q[0] == i:
            #         heapq.heappop(heap_q)
            #     print("heap_q:",heap_q)
                

            # return Q-count_q
        
#nooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
#-------------------------------------------------




        #https://www.youtube.com/watch?v=7jNS2hoM8Yw
        

        # queries = sorted(queries, key=lambda x: (x[0], -(x[1] - x[0])))
        # ops = r = 0
        # heap = []
        # delta = [0] * (len(nums) + 1)

        # for l, ele in enumerate(nums):
        #     ops += delta[l]

        #     while r < len(queries) and queries[r][0] == l:
        #         heapq.heappush(heap, -queries[r][1])
        #         r += 1

        #     while ops < ele:
        #         if not heap or -heap[0] < l:
        #             return -1
        #         delta[1 - heapq.heappop(heap)] -= 1
        #         ops += 1

        # return len(heap)


#---------------------------------------------------------------------

        # queries = sorted(queries, key=lambda x: (x[0], -(x[1] - x[0])))

        # print(queries)

        # return 1


#-----------------------------------------------------------------
        # N = len(nums)
        # Q = len(queries)

        # def apply_query(myquery: List[int], l: int, r: int):
        #     myquery[l] += 1
        #     if r + 1 < len(myquery):
        #         myquery[r + 1] -= 1

        # def check_zero(nums: List[int], diff: List[int]) -> bool:
        #     acc = 0
        #     for i in range(len(nums)):
        #         acc += diff[i]
        #         if nums[i] - acc > 0:
        #             return False
        #     return True

        
        # @lru_cache(None)
        # def dfs(i: int, cnt: int, state: tuple) -> int:
        #     if i == Q:
        #         diff = list(state)
        #         if check_zero(nums, diff):
        #             return Q - cnt
        #         return -1

        #     # Opción 1: usar esta consulta
        #     diff_use = list(state)
        #     apply_query(diff_use, queries[i][0], queries[i][1])
        #     res1 = dfs(i + 1, cnt + 1, tuple(diff_use))

        #     # Opción 2: no usar esta consulta
        #     res2 = dfs(i + 1, cnt, state)

        #     valid = [r for r in [res1, res2] if r != -1]
        #     return min(valid) if valid else -1

        # return dfs(0, 0, tuple([0] * (N + 1)))

#------------------------------------------------------------------------
        # #still brute force, recursion
        # N =len(nums)
        # Q = len(queries)

        # myquery = [0]*(N+1)
        

        # def recursion(i,myquery,cnt):
        #     reduct = 0
        #     ZeroArr = True
        #     for n,r in zip(nums,myquery):
        #         reduct += r
        #         if n-reduct > 0 :
        #             ZeroArr = False
        #             break

        #     print(i,myquery,cnt,ZeroArr)

        #     if ZeroArr:
        #         return Q-cnt

        #     else:
        #         if i < Q:
        #             #use query
        #             myquery[queries[i][0]]   +=1
        #             myquery[queries[i][1]+1] -=1
        #             op1 = recursion(i+1,myquery,cnt+1)
                    
        #             #no use query
        #             myquery[queries[i][0]]   -=1
        #             myquery[queries[i][1]+1] +=1
        #             op2 = recursion(i+1,myquery,cnt)
                    
        #             return min(op1,op2)

        #     return -1
                
        # return recursion(0,myquery,0)
     
#-------------------------------------------------


        #brute force:

        # cnt = 0
        # for li,ri in queries:
        #     change = False
        #     for i in range(li,ri+1):
        #         if nums[i] > 0: 
        #            nums[i] -= 1
        #            change = True 
        #     if not change:
        #         cnt += 1

        # if sum(nums) == 0:
        #     return cnt
        # else:
        #     return -1

    #not working , is incorrect
#--------------------------------------------------------------


        #greedy,sort take the max_len_q of query example queries = [[0,20],[1,5],[6,20],[6,10]...]
        #will not work neither!!!!!!!!!!!!!!!!!!!

#--------------------------------------------------------------

                    








