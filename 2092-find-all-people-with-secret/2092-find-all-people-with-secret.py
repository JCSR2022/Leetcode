
# class myUnionFind1:
#     def __init__(self,n):
#         self.arr = [i for i in range(n)]

#     def find(self,val):
#         while self.arr[val] != val:
#                 val = self.arr[val]
#         return val

#     def union(self,x,y):
#         root_x = self.find(x)
#         root_y = self.find(y)

#         if  root_x == root_y:
#             return 
#         self.arr[x] = root_y


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]: 

        # beging_time = float("inf")
        # dict_meetings = defaultdict(set)
        # for x,y,time in meetings:
        #     dict_meetings[time].add((x,y))
        #     if firstPerson in {x,y}:
        #         beging_time = min(beging_time,time)
        # print(beging_time)
        # print(dict(dict_meetings ))

        # my_union = myUnionFind1(n)
        # # print("my_union:",my_union.arr)
        # # print("my_union.find(2):",my_union.find(2))
        # # my_union.union(2,3)
        # # print("my_union.union(2,3), my_union:",my_union.arr)
        # # print("my_union.find(2):",my_union.find(2))


        # for t in sorted(dict_meetings.keys()):
        #     if t >= beging_time:
        #         print(t,dict_meetings[t])


        


        # #Noooooooooooooooooooooooooooooooo
        # return [0,1,2,3]



       
       
    
        secrets = set([0,firstPerson])
        
        time_map = {} # time -. adj list meetings
        
        for src, dst, t in meetings:
            if t not in time_map:
                time_map[t] = defaultdict(list)
            time_map[t][src].append(dst)
            time_map[t][dst].append(src)
            
        def dfs(src,adj):
            if src in visit:
                return
            visit.add(src)
            secrets.add(src)
            for nei in adj[src]:
                dfs(nei,adj)
            
            
        for t in sorted(list(time_map.keys())):
            visit = set()
            for src in time_map[t]:
                if src in secrets:
                    dfs(src,time_map[t])
        
        return list(secrets)

        