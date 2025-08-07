class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        

        #this was yesterday sol, O(n**2)
        # N = len(fruits)
        # ans = 0 
        # for fruit in fruits:
        #     for i in range(N):
        #         if baskets[i] >= fruit:
        #             baskets[i] = -1
        #             break
        #     else:
        #         ans +=1
        # return ans
        #diff between yesterday is size n**5..will not work for time

#Time Limit Exceeded as expected
#---------------------------------------
        #Lets try sort basket and use bisection  O(nlogn)
        # N = len(fruits)
        # baskets.sort()  
        # ans = 0

        # for fruit in fruits:
        #     print(baskets)
        #     l = 0
        #     r = len(baskets)-1
        #     fruit_idx = -1
        #     while l<=r:
        #         m =  (l+r)//2
        #         print(fruit,l,m,r,baskets[m],baskets[m] < fruit,fruit_idx,ans )
        #         if baskets[m] < fruit:
        #             l = m + 1        
        #         else:
        #             fruit_idx = m
        #             r = m - 1

        #     if fruit_idx == -1:
        #         ans +=1
        #     else:
        #         print("fruit_idx:",fruit_idx,"baskets[fruit_idx]:",baskets[fruit_idx] )
        #         del baskets[fruit_idx]

        # return ans

#no funciona
#------------------------------------------------------------------------
        #usar un heap??
    
        # bask_idx = [(i,v) for i,v in enumerate(baskets)]  
        # heapq.heapify(bask_idx)
        # ans = 0

        # for fruit in fruits:
        #     #print(bask_idx)
        #     temp = []
        #     while bask_idx and bask_idx[0][1] < fruit:
        #         heapq.heappush(temp, heapq.heappop(bask_idx))

        #     if bask_idx:
        #         heapq.heappop(bask_idx)
        #         while temp:
        #             heapq.heappush(bask_idx,heapq.heappop(temp))
        #     else:
        #         bask_idx = temp
        #         ans +=1


        # return ans

#Time Limit Exceeded the same,
#--------------------------------------------------------------------

        sect_mx = []
        m = len(baskets)
        a = int(math.sqrt(m))  # size of one array

        cnt = 0
        mx = 0
        for i in range(m):
            if cnt == a:
                # creating sector of size a
                sect_mx.append(mx)
                mx = baskets[i]
                cnt = 1
            else:
                cnt += 1
                mx = max(mx, baskets[i])

        # last sector
        sect_mx.append(mx)

        remain = 0

        # start allocating
        for fruit in fruits:
            k = 0
            set_flag = 1

            for j in range(0, m, a):
                if sect_mx[k] < fruit:
                    # skip this segment
                    k += 1
                    continue

                # find place to allocate
                for r in range(j, min(j + a, m)):
                    if baskets[r] >= fruit:
                        set_flag = 0
                        baskets[r] = 0
                        break

                # if fruit is allocated in a sector
                if set_flag == 0:
                    sect_mx[k] = 0  # find new mx
                    # update new sector mx
                    for r in range(j, min(j + a, m)):
                        sect_mx[k] = max(baskets[r], sect_mx[k])
                    break

            remain += set_flag

        return remain








        






