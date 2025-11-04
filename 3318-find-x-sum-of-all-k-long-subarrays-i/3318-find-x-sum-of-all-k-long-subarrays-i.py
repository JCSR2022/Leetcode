class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        #brute force


        
        
        frec = defaultdict(int)
        for r in range(k):
            frec[nums[r]] +=1

        arr = sorted([ (val,key) for key,val in frec.items()],reverse=True)[:x]
        sum_arr = sum( i*j for i,j in arr) 
        ans = [sum_arr]
        #print(dict(frec),arr,sum_arr)

        for r in range(k,len(nums)):
            frec[nums[r]] +=1
            frec[nums[r-k]] -=1
            arr = sorted([ (val,key) for key,val in frec.items()],reverse=True)[:x]
            sum_arr =sum( i*j for i,j in arr) 
            #print(dict(frec),arr,sum_arr)
            ans.append(sum_arr)
            
        return ans
         




