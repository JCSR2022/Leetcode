class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        length = len(n)
        original_number = int(n)
        
        # Special edge case candidates
        candidates = set([
            10**(length - 1) - 1,  # e.g., 999 for n=1000
            10**length + 1          # e.g., 10001 for n=9999
        ])
        
        # Generate candidates by modifying the first half of the number
        first_half = int(n[:(length + 1) // 2])
        for i in range(-1, 2):  # Decrement, same, increment
            prefix = str(first_half + i)
            if length % 2 == 0:
                candidate = int(prefix + prefix[::-1])
            else:
                candidate = int(prefix + prefix[:-1][::-1])
            candidates.add(candidate)
        
        # Remove the original number itself
        candidates.discard(original_number)
        
        # Find the closest palindrome
        closest_palindrome = min(candidates, key=lambda x: (abs(x - original_number), x))
        
        return str(closest_palindrome)
    
    
    
        # return (l:=len(n),p:=int(n[:(l+1)//2])) and str(min({10**(l-1)-1,10**l+1,*(int((t:=str(p+q))+t[-1-l%2::-1]) for q in (-1,0,1))}-{n:=int(n)},key=lambda v:(abs(v-n),v)))
