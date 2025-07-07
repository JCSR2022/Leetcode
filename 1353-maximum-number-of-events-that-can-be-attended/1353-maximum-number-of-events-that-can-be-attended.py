class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:

        #brute force:
        # events.sort()
        # print(events)
        # ans = 0
        # days_taken = set()
        # for d1,d2 in events:
        #     for day in range(d1,d2+1):
        #         if day not in days_taken:
        #             ans +=1
        #             days_taken.add(day)
        #             break
        #     print((d1,d2),ans,days_taken)

        # return ans
#no imbecil, hasta cuando vas a cagarla!!!!!!
#--------------------------------------------------------------------

        #imbecil , solo puedes hacer un backtrack 
        # #y no va a funcionar por tiempo

        # max_events = 0
        # def recursion(i=0,curr_event=False,end_date = 0,total_events):
        #     nonlocal max_events 
            
        #     if i == len(events):
        #         max_events = max(max_events,total_events)

        #     if not current ev

#------------------------------------------------

        events.sort(key=lambda x: (x[1], x[0]))
        ans = 0  
        days_taken = set()
        for d1,d2 in events:
            for day in range(d1,d2+1):
                if day not in days_taken:
                    ans +=1
                    days_taken.add(day)
                    break
        return ans




                      
        