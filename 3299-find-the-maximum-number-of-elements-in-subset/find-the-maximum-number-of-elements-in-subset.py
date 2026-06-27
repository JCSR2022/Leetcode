class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        frec_map = Counter(nums)
        visited = set()
        final_ans = 1

        for n in sorted(frec_map.keys()):

            #special case n=1
            if n == 1:
                final_ans = max(final_ans, frec_map[1] - (1 if frec_map[1]%2==0 else 0) )
                continue
            

            ans = 1 
            curr_n = n
            while (curr_n not in visited) and (frec_map[curr_n] >= 2) and (curr_n**2 in frec_map):
                #print(curr_n ,ans )
                visited.add(curr_n)
                curr_n = curr_n**2
                ans +=2
            final_ans = max(final_ans, ans)

        return final_ans 
        