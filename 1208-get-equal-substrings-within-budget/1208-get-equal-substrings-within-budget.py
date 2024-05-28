class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        
#         ans = 0
#         for s_ch,t_ch in zip(s,t):
#             diff = ord(s_ch)-ord(t_ch)
#             print(s_ch,t_ch,maxCost,diff )
            
#             if diff < 0:
#                 maxCost += ord(s_ch)-ord(t_ch)
            
#             if maxCost >= 0 :
#                 ans +=1
#             else:
#                 break
            
#         return ans

        start = 0
        current_cost = 0
        max_length = 0

        for end in range(len(s)):
            # Calculate the cost to change s[end] to t[end]
            current_cost += abs(ord(s[end]) - ord(t[end]))

            # If the current cost exceeds maxCost, move the start pointer to reduce the cost
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1

            # Calculate the maximum length of the valid window
            max_length = max(max_length, end - start + 1)
        
        return max_length