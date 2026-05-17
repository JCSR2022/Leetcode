class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        #brute force dfs

        limit = len(arr)
        visited = set([start])
        dq = deque([start])

        while dq:
            current = dq.popleft()
            if arr[current] == 0:
                return True


            right = current + arr[current]
            if  right  < limit and right not in visited:
                visited.add(right)
                dq.append(right)

            left =  current - arr[current]
            if  left >= 0 and left not in visited:
                visited.add(left)
                dq.append(left)

        return False



