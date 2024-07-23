class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
#         ctr = Counter(nums).items()                         # <-- 1)

#         arr = sorted(ctr, key = lambda x: (x[1], -x[0]))    # <-- 2)

#         return chain(*[[n]* cnt for n,cnt in arr])          # <-- 3)        
        
        
        
#         freq = Counter(nums)
#         nums.sort(key=lambda x: (freq[x], -x))
#         return nums
        
# This line sorts the nums array in place using a custom key. The key parameter of the sort method is a function that extracts a comparison key from each list element.
# The lambda function lambda x: (freq[x], -x) returns a tuple for each element x in nums. This tuple contains two values:

# freq[x]: The frequency of the element x.
# -x: The negative value of x.
# The sort method sorts primarily by the first element of the tuple (frequency), in ascending order (lower frequency comes first). If two elements have the same frequency, it uses the second element of the tuple to break the tie, sorting in descending order (higher value comes first) because -x will make higher values appear before lower values.

# Example:
# For nums = [4, 4, 2, 3, 2, 2]:

# Frequencies: {2: 3, 4: 2, 3: 1}
# The lambda function will generate the keys as follows:
# For 4: (2, -4)
# For 2: (3, -2)
# For 3: (1, -3)
# So, the sorted keys will be [(1, -3), (2, -4), (2, -4), (3, -2), (3, -2), (3, -2)], resulting in the sorted array [3, 4, 4, 2, 2, 2].
        
        
        
        
        
# My solution:
#         #hashmap

        hasnums = defaultdict(int)
        for n in nums: hasnums[n] += 1
        
        num_vect = [ [n,cant] for n,cant in hasnums.items()]
        print(num_vect)
        
        num_vect.sort(reverse = True)
        print(num_vect)
        
        num_vect = sorted(num_vect, key=lambda x: x[1])
        print(num_vect)
        
        ans = []
        for n,cant in num_vect:
            ans += [n]*cant
            
        return ans
        
        
        
        
        
        
        