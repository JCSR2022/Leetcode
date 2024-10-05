class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #brute force
        # Make a hash map of s1 
        # for each letter in s2 check if in s1_hash
        #  if in s1 -=1 for each letter if sum values on hashMap == 0, return True
        
#         hash_s1_org = Counter(s1)
#         hash_s1 = hash_s1_org.copy()
#         review = False
        
#         for s in s2:
#             #first letter found
#             if not review and s in hash_s1:
#                 review = True
#                 hash_s1[s] -=1
            
#             #next letter found
#             if review and s in hash_s1:
#                 if hash_s1[s] != 0:
#                     hash_s1[s] -=1
            
#             if sum(hash_s1.values()) == 0:
#                 return True
            
#             # false substring
#             if review and s not in hash_s1:
#                 hash_s1 = hash_s1_org.copy()
#                 review = False
                
#         return False


#----------------------------------------------------

        #Aproach - hash / window
    
        
#         hash_s1 = Counter(s1)
#         print(hash_s1)
#         l = 0
#         size = len(s1)
#         hash_s2 = Counter(s2[l:l+size-1])
        
        
        
#         if hash_s2 == hash_s1:
#             return True
        
#         while l+size < len(s2)-1:
#             l +=1
#             hash_s2[s2[l-1]] -= 1
#             hash_s2[s2[l+size-1]] += 1
            
#             print(l,hash_s2)
#             if hash_s2 == hash_s1:
#                 return True
            
#         return False
        
#---------------------------------------------------------
        mp = defaultdict(int)
        mp2 = defaultdict(int)

        # Fill in the frequency map for s1
        for ch in s1:
            mp2[ch] += 1

        i, j = 0, 0
        k = len(s1)
        n = len(s2)

        while j < n:
            mp[s2[j]] += 1
            j += 1

            # When the window size is equal to s1's length
            if j - i == k:
                if mp == mp2:
                    return True
                
                # Sliding the window: remove character at i from the map
                mp[s2[i]] -= 1
                if mp[s2[i]] == 0:
                    del mp[s2[i]]
                i += 1

        return False
        