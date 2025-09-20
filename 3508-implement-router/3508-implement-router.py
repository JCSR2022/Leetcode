# from collections import deque

# class Router:

#     def __init__(self, memoryLimit: int):
#         self.memoryLimit = memoryLimit
#         self.packets = deque([])
#         self.packets_set =  set()
#         self.destination_time = defaultdict(lambda: defaultdict(int))


#     def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
#         packet = (source,destination,timestamp)
#         if packet not in self.packets_set :
#             if len(self.packets_set) == self.memoryLimit :
#                 remove_packet = self.packets.popleft()
#                 self.packets_set.remove(remove_packet)
#                 self.destination_time[remove_packet[1]][remove_packet[2]] -=1    

#             self.destination_time[destination][timestamp] +=1        
#             self.packets_set.add(packet)
#             self.packets.append(packet)
            
#             return True
#         else:
#             return False


#     def forwardPacket(self) -> List[int]:
#         if self.packets_set:
#             packet = self.packets.popleft()
#             self.packets_set.remove(packet)
#             self.destination_time[packet[1]][packet[2]] -=1 
#             return packet
#         else:
#             return ()  


#     def getCount(self, destination: int, startTime: int, endTime: int) -> int:
#         #O(n)  n is max num of timestamps

#             count = 0

#             for timestamp in self.destination_time[destination]:
#                 if  timestamp >= startTime and timestamp <= endTime :
#                     count +=self.destination_time[destination][timestamp]
            
#             return count 

#Time Limit Exceeded
#----------------------------------------------------------------




class Router:
    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.packets = {}  # key -> [source, destination, timestamp]
        self.counts = defaultdict(list)  # destination -> sorted list of timestamps
        self.queue = deque()  # FIFO order of packets

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = self._encode(source, destination, timestamp)

        # Duplicate check
        if key in self.packets:
            return False

        # If memory full, forward oldest packet
        if len(self.packets) >= self.size:
            self.forwardPacket()

        # Add packet
        self.packets[key] = [source, destination, timestamp]
        self.queue.append(key)
        self.counts[destination].append(timestamp)

        return True

    def forwardPacket(self):
        if not self.packets:
            return []

        key = self.queue.popleft()
        packet = self.packets.pop(key)

        dest = packet[1]
        self.counts[dest].pop(0)  # remove the earliest timestamp

        return packet

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        timestamps = self.counts.get(destination, [])
        if not timestamps:
            return 0

        # Binary search for range
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)

        return right - left

    def _encode(self, source: int, destination: int, timestamp: int) -> int:
        # Encode uniquely into 1 number
        return (source << 40) | (destination << 20) | timestamp















# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)