class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        #brute force: 
        # try all combination , save in a heap, if no more comb posibles return min

        # def op_add(arr:list[int]):
        #     new_arr = arr.copy()
        #     for i in range(1,len(arr),2):
        #         new_arr[i] = (new_arr[i]+a)%10
        #     return new_arr

        # def op_rotate(arr:list[int]):
        #     new_arr = arr.copy()
        #     return new_arr[-b:] + new_arr[:-b]

        # num_s = [ int(ch) for ch in s]

        # dq = deque([num_s])
        # heap = [num_s]
        
        
        # while dq :
        #     # print("dq:",list(dq))
        #     # print("heap:",list(heap))
        #     # print()
            
        #     curr_s = dq.popleft()

        #     add_s =  op_add(curr_s)
        #     if add_s not in heap:
        #         heapq.heappush(heap,add_s)
        #         dq.append(add_s)

        #     rotate_s = op_rotate(curr_s)
        #     if rotate_s not in heap:
        #         heapq.heappush(heap,rotate_s)
        #         dq.append(rotate_s)

        # return "".join([str(num) for num in heap[0]])


#Time Limit Exceeded of course
#------------------------------------------------------------
#try same logic but a bit faster?


        size = len(s) 
        dq = deque([s])
        seen = set()
        seen.add(s)
        ans = s

        while dq :
            # print("ans:",ans)
            # print("dq:",list(dq))
            # print("seen:",seen)
            # print()
            
            curr_s = dq.popleft()

            #add
            num_s = list(curr_s)
            for i in range(1,size,2):
                num_s[i] = str((int(num_s[i])+a)%10)
            num_s = "".join(num_s)
            if num_s not in seen:
                seen.add(num_s)
                dq.append(num_s)
                ans =min(ans,num_s)

            #rotate
            num_s = list(curr_s)
            num_s = num_s[-b:] + num_s[:-b]
            num_s = "".join(num_s)
            if num_s not in seen:
                seen.add(num_s)
                dq.append(num_s)
                ans =min(ans,num_s)

        return ans








        