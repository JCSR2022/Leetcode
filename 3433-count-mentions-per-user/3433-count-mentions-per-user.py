class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:

        mentions = [0]*numberOfUsers

        heap = []
        for event,timestamp,mentions_id in events:
            type_event = 0 if event == "OFFLINE" else 1
            heapq.heappush(heap, (int(timestamp),type_event,mentions_id))
        
        active_users = {n:0 for n in range(numberOfUsers)}
        while heap:
            timestamp, event,mentions_id  = heapq.heappop(heap)
            if event == 0:
                active_users[int(mentions_id)] = timestamp+60

            else:
                if mentions_id == 'ALL':
                    for i in range(numberOfUsers): mentions[i] +=1
                elif mentions_id == 'HERE':
                    for user,time_active in active_users.items():
                        if time_active <=  timestamp: mentions[user] +=1
                else:
                    for id_num in mentions_id.split(" "):
                         mentions[int(id_num[2:])] += 1

        return mentions

        