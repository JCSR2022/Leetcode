class Solution:
    def countBalancedPermutations(self, num: str) -> int:

        #bruteforce only for reference

        # MOD = 10**9+7

        # ans = 0
        
        # for permute in set(itertools.permutations(num)):
        #     even_sum = 0
        #     odd_sum = 0
        #     for i,digit in enumerate(permute):
        #         if i%2 == 0:
        #             even_sum += int(digit)
        #         else:
        #             odd_sum += int(digit) 
        #     print(permute, even_sum == odd_sum)
        #     if even_sum == odd_sum:
        #         ans+=1
        
        # return ans%MOD

#Time Limit Exceeded for sure!!!!  jajaj
#-----------------------------------------------------------------

        #aproach DFS with memory

        # MOD = 10**9+7

        # hash_num = defaultdict(int)
        # for n in num:
        #      hash_num[int(n)] += 1

        # max_value = sum( [n*cnt for n,cnt in hash_num.items()] )//2
        
        # # hash_memory = {}
        # def dfs(hash_num,even_sum,odd_sum,odd):
        #     #print(dict(hash_num),even_sum,odd_sum,odd)

        #     # if (hash_num,even_sum,odd_sum,odd) in hash_memory:
        #     #     return hash_memory[(hash_num,even_sum,odd_sum,odd)]

        #     if len(hash_num) == 0  and even_sum == odd_sum:
        #         return 1
            
        #     if even_sum >max_value  or odd_sum>max_value :
        #         return 0
            
        #     count = 0 
        #     keys = list(hash_num.keys())
        #     for n in keys :
        #         hash_num[n] -= 1
        #         if hash_num[n] == 0:
        #             del hash_num[n]
                
        #         if odd:
        #             odd_sum +=n
        #         else:
        #             even_sum +=n
        #         count += dfs(hash_num,even_sum,odd_sum,not odd)
        #         if odd:
        #             odd_sum -=n
        #         else:
        #             even_sum -=n
        #         hash_num[n] += 1

        #     # hash_memory[(hash_num,even_sum,odd_sum,odd)] = count
        #     return count%MOD

        
        # return dfs(hash_num,0,0,True)
#Time Limit Exceeded
#--------------------------------------------------------------------------


        MOD = 10**9+7

        hash_num = [0]*10
        for n in num:
             hash_num[int(n)] += 1

        max_value = sum( [n*cnt for n,cnt in enumerate(hash_num)] )//2
        
        hash_memory = {}
        def dfs(hash_num,even_sum,odd_sum,odd):
            hash_num = tuple(hash_num)

            if (hash_num,even_sum,odd_sum,odd) in hash_memory:
                return hash_memory[(hash_num,even_sum,odd_sum,odd)]

            if sum(hash_num) == 0  and even_sum == odd_sum:
                return 1
            
            if even_sum >max_value  or odd_sum>max_value :
                return 0
            
            count = 0 
            hash_num = list(hash_num)
            for n in range(10) :
                if hash_num[n] > 0:  
                    hash_num[n] -= 1
                
                    if odd:
                        odd_sum +=n
                    else:
                        even_sum +=n
                    count += dfs(hash_num,even_sum,odd_sum,not odd)
                    if odd:
                        odd_sum -=n
                    else:
                        even_sum -=n
                    hash_num[n] += 1

            hash_num = tuple(hash_num)
            hash_memory[(hash_num,even_sum,odd_sum,odd)] = count%MOD
            return hash_memory[(hash_num,even_sum,odd_sum,odd)]

        
        return dfs(hash_num,0,0,True)