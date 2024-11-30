
#from collections import Counter

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        # bild adjacence list, find euler path
        # https://www.youtube.com/watch?v=F589S4YUUmM
        
#         graph = {}
#         out_degree = Counter()
#         in_degree = Counter()
#         for l,r in pairs:
#             out_degree[l] += 1
#             out_degree[r] += 0
#             in_degree[r] += 1
#             in_degree[l] += 0
#             if l in graph:
#                 graph[l].append(r)
#             else:
#                 graph[l] = [r]
#             if r not in graph:
#                 graph[r] = []
        
#         print(graph)
#         print(out_degree)
#         print(in_degree)
        
#         #find start point
#         start = -1
#         for k,out_v in out_degree.items():
#             if out_v-in_degree[k] == 1:
#                 start = k
#                 break
                
#         if start == -1:
#             start = in_degree[0]
            
                
#         print("start: ",start)
            
            
        
        
#         return pairs

#--------------------------------------------




        # Step 1: Build the graph
        graph = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for start, end in pairs:
            graph[start].append(end)
            out_degree[start] += 1
            in_degree[end] += 1
        
        # Step 2: Find the starting node for the Eulerian path
        start_node = pairs[0][0]
        for node in graph:
            if out_degree[node] > in_degree[node]:
                start_node = node
                break
        
        # Step 3: Hierholzer's algorithm to find the Eulerian path
        stack = [start_node]
        result = []
        
        while stack:
            while graph[stack[-1]]:
                next_node = graph[stack[-1]].popleft()
                stack.append(next_node)
            result.append(stack.pop())
        
        # Step 4: Format the result in reverse order
        result.reverse()
        return [[result[i], result[i + 1]] for i in range(len(result) - 1)]

