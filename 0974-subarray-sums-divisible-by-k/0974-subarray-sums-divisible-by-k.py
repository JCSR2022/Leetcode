class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        
        # # brute force n**2
        # cont = 0
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         if sum(nums[i:j+1])%k == 0:cont += 1
        #         #print(nums[i:j+1],cont)
        # return  cont
        
        
        # https://www.youtube.com/watch?v=bcXy-T4Sc3E&t=24s
        # no le llego!! NPI time  O(n) space O(k)  
        
        
        prefix_sum = 0
        res = 0
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1        
        
        
        for n in nums:
            prefix_sum += n 
            remain = prefix_sum % k
            
            if remain in prefix_cnt:
                res += prefix_cnt[remain]
            prefix_cnt[remain] += 1
            
        return res
        
        
        
        
        