class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        #will not work for time but lets try backtrack

        #O(nlogn)
        #events.sort(key=lambda x: x[0])

        #O(2**n)
        # my_memo = {}
        # def backtrack(ev_idx,k_use,curr_val):
        #     if k_use == k or ev_idx == len(events):
        #         return curr_val

        #     if (ev_idx,k_use,curr_val) in my_memo:
        #         return my_memo[(ev_idx,k_use,curr_val)]

        #     #use event:
        #     val = events[ev_idx][2]
        #     end = events[ev_idx][1]
        #     nex_idx = ev_idx+1
        #     while nex_idx < len(events) and  end >= events[nex_idx][0]:
        #         nex_idx +=1
        #     op1 = backtrack(nex_idx,k_use+1,curr_val+val)

        #     #skip current event:
        #     op2 = backtrack(ev_idx+1,k_use,curr_val)

        #     my_memo[(ev_idx,k_use,curr_val)] = max(op1,op2)
        #     return my_memo[(ev_idx,k_use,curr_val)]

        # return backtrack(0,0,0)
            
#as expected Memory Limit Exceeded
#---------------------------------------------------------------
        #2d Aproach: dp solution try

        
        #O(nlogn)
        #events.sort(key=lambda x: x[0])
        ##

#Not a clue
#------------------------------------------------------------------


        #O(nlogn)
        events.sort(key=lambda x: x[0])

        #O(2**n)
        my_memo = {}
        def backtrack(ev_idx,k_use,curr_val):
            if k_use == k or ev_idx == len(events):
                return curr_val

            if (ev_idx,k_use,curr_val) in my_memo:
                return my_memo[(ev_idx,k_use,curr_val)]

            #use event:
            val = events[ev_idx][2]
            end = events[ev_idx][1]
            
            l = ev_idx+1
            r = len(events)-1
            # por si no se encuentra ninguno mayor
            next_idx = len(events)  

            while l <= r:
                m = (l + r) // 2
                if events[m][0] <= end:
                    l = m + 1
                else:
                    next_idx = m
                    r = m - 1
            
            op1 = backtrack(next_idx,k_use+1,curr_val+val)

            #skip current event:
            op2 = backtrack(ev_idx+1,k_use,curr_val)

            my_memo[(ev_idx,k_use,curr_val)] = max(op1,op2)
            return my_memo[(ev_idx,k_use,curr_val)]

        return backtrack(0,0,0)







