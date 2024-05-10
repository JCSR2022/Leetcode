class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # brute force n**2 solution
        ans = []
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                ans.append([arr[i],arr[j],arr[i]/arr[j]])
                
        ans = sorted(ans,key = lambda x:x[2])
        
        return ans[k-1][:2]