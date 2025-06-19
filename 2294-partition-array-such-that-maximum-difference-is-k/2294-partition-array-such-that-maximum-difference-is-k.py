class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:

        #Aproach Memory O(n) but time also 2*O(n):
        #create arr size max(nums), create flag on each n of num then group
        N = (max(nums)+1)
        arr = [0] * N
        for n in nums:
           arr[n] = 1

        #print(arr)
        if k == 0:
            return sum(arr)

        i = 0
        ans = 0
        while i < N:
            #print(i,arr[i],i+k+1,ans)
            if arr[i]:
                i += k + 1
                ans += 1
            else:
                i += 1

        return ans





#-----------------------------------------------------------------------------
        # #Aproach : max O(n**2)
        # #group and save dict where key is (min,max) for val

        # groups = defaultdict(set)
        # for n in nums:
        #     is_on_group 
        #     for n_min,n_max in groups.keys():
        #         if n_min <= n <= n_max :
                    
        #will not work because with this procedure i can do 2 groups insted of 1





