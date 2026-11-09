
import heapq
from typing import List

class Solution:
    def busiestServers(
        self,
        k: int,
        arrival: List[int],
        load: List[int]
    ) -> List[int]:

        # -----------------------------------------
        # STEP 1: Initialize the Segment Tree
        # -----------------------------------------

        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Every server starts as available (1).
        for i in range(k):
            tree[size + i] = 1

        # Build the tree.
        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        # -----------------------------------------
        # STEP 2: Update server availability
        # -----------------------------------------

        def update(server, available):

            pos = size + server

            tree[pos] = available

            pos //= 2

            while pos >= 1:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        # -----------------------------------------
        # STEP 3: Find first available server
        # in the interval [ql, qr].
        # -----------------------------------------

        def find_first(node, left, right, ql, qr):

            # Outside the requested interval
            # or no available servers in this range.
            if right < ql or left > qr or tree[node] == 0:
                return -1

            # We found an available server.
            if left == right:
                return left

            mid = (left + right) // 2

            # Search left side first because we want
            # the smallest available server ID.
            result = find_first(
                node * 2, left, mid, ql, qr
            )

            if result != -1:
                return result

            # If not found, search right side.
            return find_first(
                node * 2 + 1, mid + 1, right, ql, qr
            )

        # -----------------------------------------
        # STEP 4: Initialize busy heap and counters
        # -----------------------------------------

        # (finish_time, server_id)
        busy = []

        used = [0] * k

        # -----------------------------------------
        # STEP 5: Process requests
        # -----------------------------------------

        for i, (a, l) in enumerate(zip(arrival, load)):

            # Release every server that has finished
            # its request by the current arrival time.
            while busy and busy[0][0] <= a:

                finish_time, server = heapq.heappop(busy)

                update(server, 1)

            # Preferred server for this request.
            start = i % k

            # Search from preferred server to the end.
            server = find_first(1, 0, size - 1, start, k - 1)

            # If not found, wrap around and search
            # from server 0 to start - 1.
            if server == -1 and start > 0:
                server = find_first(1, 0, size - 1, 0, start - 1)

            # All servers are busy: drop the request.
            if server == -1:
                continue

            # Assign request to the selected server.
            used[server] += 1

            # Mark server as busy.
            update(server, 0)

            # Insert its finishing time into the heap.
            heapq.heappush(busy, (a + l, server))

        # -----------------------------------------
        # STEP 6: Find busiest servers
        # -----------------------------------------

        max_requests = max(used)

        return [
            i for i, count in enumerate(used)
            if count == max_requests
        ]



























        #Aproach .make a heap

        # # heap() next_time_free, server_num

        # disponibility = [ (0,n) for n in range(k)]
        # used = [0]*k

        # heapq.heapify(disponibility)

        # for a,l in zip(arrival,load):
        #     nextime_free, curr_server = disponibility[0]

        #     if  nextime_free < a:
        #         used[curr_server] += 1
        #         heapq.heapreplace(disponibility, (a+l,curr_server ))
        #     #print(disponibility,used,a,l,nextime_free < a,nextime_free)


        # return [ i for i,n in enumerate(used) if  n == max(used)]