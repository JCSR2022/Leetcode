class Solution:
    def findKthNumber(self, n, k):
        current_prefix = 1
        k -= 1  # Decrement k to handle zero-based indexing
        
        while k > 0:
            count = self.countNumbersWithPrefix(current_prefix, n)
            if k >= count:
                current_prefix += 1  # Move to the next prefix
                k -= count
            else:
                current_prefix *= 10  # Go deeper in the current prefix
                k -= 1
        
        return current_prefix

    def countNumbersWithPrefix(self, prefix, n):
        first_number = prefix
        next_number = prefix + 1
        total_count = 0

        while first_number <= n:
            total_count += min(n + 1, next_number) - first_number
            first_number *= 10
            next_number *= 10

        return total_count



# class Solution:
#     def findKthNumber(self, n: int, k: int) -> int:
        
#         cont = [0]
#         record = []
#         def recursive(value):
#             cont[0] +=1
            
#             if cont[0] == k:
#                 record.append(value)
#                 return
            
#             if cont[0] > k:
#                 return
            
#             if (value * 10) <= n:
#                 recursive(value * 10)
#             if value + 1 <= n and int(str(value)[-1]) < 9:
#                 recursive(value + 1)
                
#         recursive(1)
        
#         #print(ans)

#         return  record [0]