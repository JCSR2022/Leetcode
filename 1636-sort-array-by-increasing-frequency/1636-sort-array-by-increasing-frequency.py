class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        #hashmap

        hasnums = defaultdict(int)
        for n in nums: hasnums[n] += 1
        
        num_vect = [ [n,cant] for n,cant in hasnums.items()]
        #print(num_vect)
        
        num_vect.sort(reverse = True)
        #print(num_vect)
        
        num_vect = sorted(num_vect, key=lambda x: x[1])
        #print(num_vect)
        
        ans = []
        for n,cant in num_vect:
            ans += [n]*cant
            
        return ans
        
        
        
        
        
        
        