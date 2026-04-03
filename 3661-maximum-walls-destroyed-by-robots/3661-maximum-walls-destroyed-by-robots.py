from bisect import bisect_left, bisect_right

class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:


            # fire_range =[]
            # for r,d in zip(robots,distance):
            #     fire_range.append(((r-d),1))
            #     fire_range.append(((r+d+1),-1))

            # fire_range.sort()
            # walls.sort()


            # print(fire_range)
            # print(walls)
            # i = 1
            # j = 0
            # count = 0
            # in_range = 1

            # # while i<len(fire_rage) and j<len(walls):
                
            # #     if walls[j]<fire_rage[i][0] and in_range ==1:
            # #j+1 , no count
            # #if walls[j] == range[i]:
            # #count +=1, j+1
            # #else:
            # # i +=1
            # #     in_range += fire_rage[i][1]
            # #     pass

            # return count


#nooooooooooooooooooooooooooooooooooooooo
#----------------------------------------------------------


# Sort robots
# For each robot:
# Find nearest robot on left/right
# Build two valid intervals:
# Left interval: [max(r-d, left_robot+1), r]
# Right interval: [r, min(r+d, right_robot-1)]

# Now problem becomes:

# Pick at most ONE interval per robot to maximize covered walls

# This is classic:

# Interval Scheduling + Greedy with walls

        

    
            n = len(robots)
            robots_sorted = sorted(zip(robots, distance))
            robots_pos = [r for r, _ in robots_sorted]
            
            walls.sort()

            intervals = []

            # Build valid intervals considering robot blocking
            for i, (r, d) in enumerate(robots_sorted):
                
                # LEFT
                left_limit = r - d
                if i > 0:
                    left_limit = max(left_limit, robots_pos[i-1] + 1)
                intervals.append((left_limit, r, i))  # (L, R, robot_id)

                # RIGHT
                right_limit = r + d
                if i < n - 1:
                    right_limit = min(right_limit, robots_pos[i+1] - 1)
                intervals.append((r, right_limit, i))

            # Precompute how many walls each interval covers
            interval_values = []
            for L, R, idx in intervals:
                left = bisect_left(walls, L)
                right = bisect_right(walls, R)
                count = right - left
                if count > 0:
                    interval_values.append((L, R, idx, count))

            # Sort by right endpoint (greedy)
            interval_values.sort(key=lambda x: x[1])

            used_robot = set()
            total = 0
            last_end = -1

            for L, R, idx, val in interval_values:
                if idx in used_robot:
                    continue
                if L > last_end:
                    total += val
                    last_end = R
                    used_robot.add(idx)

            return total
