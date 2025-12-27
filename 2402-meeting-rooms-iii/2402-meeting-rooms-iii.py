class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
 
 
        # Aproach:
        # heap on meetings (beging, time) 
        # heap_size_n on progress (end time) pop when time == end
        # make for in time

        h_meetings = []
        for m_star,m_end in meetings:
            heapq.heappush(h_meetings,(m_star,m_end-m_star))
   
        count_use = defaultdict(int)

        rooms_free =list(range(n))
        heapq.heapify(rooms_free)

        h_process = [] #(end_time,room) 
        time = h_meetings[0][0]
        while h_meetings:
            # print("time:",time)
            # print("h_meetings:",h_meetings)
            # print("h_process:",h_process)
            # print("rooms_free:",rooms_free)
            # print("count_use:",count_use)
            # print()

            # verify if there was a meeting and end
            while h_process and h_process[0][0] <= time:
                _,room = heapq.heappop(h_process)
                heapq.heappush(rooms_free,room)

            #verify if there is meeting pending and room free
            if  rooms_free:
                _,duration = heapq.heappop(h_meetings)
                room = heapq.heappop(rooms_free)
                count_use[room] += 1
                heapq.heappush(h_process,(time+duration,room)   )
                time = h_meetings[0][0] if h_meetings else time+duration
            else:
                time = h_process[0][0]  
        max_use = max(count_use.values())
        return min([ room for room,use in count_use.items() if use == max_use])















 
#------------------------------------------------------------------
        # meetings.sort()
        
        # available = [i for i in range(n)] # 0,1,2,3.. min_heap
        # used = [] # (end_time, room_number)
        # count = [0] * n  # conunt[n] = meetings schedule
        
        
        # for start, end in meetings:
        #     # Finish meetings
        #     while used and start >= used[0][0]:
        #         _, room = heapq.heappop(used)
        #         heapq.heappush(available,room)
            
        #     # no room is available
        #     if not available:
        #         end_time,room =  heapq.heappop(used)
        #         end = end_time + (end -start)
        #         heapq.heappush(available,room)
                
        #     # a room is available
        #     room =  heapq.heappop(available)
        #     heapq.heappush(used,(end,room))
        #     count[room] +=1

        # return count.index(max(count))
        
            
        
                
                
            
            
            