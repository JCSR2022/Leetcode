class Solution:
    def nearestPalindromic(self, n: str) -> str:
        
        """
        Explanation of the Code
            1. Initialization:
                We first calculate the length of the string n and convert 
                n to an integer original_number for comparison purposes.

            2. Edge Case Candidates:
                Generate two special edge cases:
                    10**(length - 1) - 1: The largest number with 
                    one less digit than n (e.g., 999 for n=1000).
            
                    10**length + 1: The smallest number with 
                    one more digit than n (e.g., 10001 for n=9999).
            
            3.Generate Palindromes by Modifying the First Half:
                We extract the first half of n, convert it to an integer, and then
                consider three cases: decrementing by 1, keeping it the same, and 
                incrementing by 1. For each of these, we create a palindrome:

                    If the length of n is even, we mirror the entire prefix.
                    
                    If the length of n is odd, we mirror the prefix excluding 
                    the last character.
            
            4. Remove the Original Number:
                We remove the original number from the set of candidates to ensure 
                we do not return n itself.

            5. Select the Closest Palindrome:
                We find the closest palindrome by comparing the absolute difference 
                between n and each candidate. If there is a tie, the smaller 
                palindrome is chosen.

            6. Return the Result:
                Finally, we convert the closest  palindrome back to a string 
                and return it as the result.
        
        """
        
        
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
    
    
