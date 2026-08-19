class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:


        #greedey

        # reservedSeats = { (i,j) for i,j in reservedSeats }
        # count_blocks = 0
        # for i in range(1,n+1):
        #     print( sorted(list(reservedSeats  )))
        #     cnt_free = 0
        #     for j in range(2,10):
        #         if (i,j) in reservedSeats:
        #             cnt_free = 0
        #         else:
        #             cnt_free +=1
                
        #         if cnt_free == 4:
        #             count_blocks += 1
        #             cnt_free = 0
        #         print((i,j),(i,j) in reservedSeats,cnt_free,count_blocks )

        # return count_blocks


#-------------------------------------------------------------


#Se jooio, no tengo tiempo
        # reservedSeats = { (i,j) for i,j in reservedSeats }

        # pos_blocks = { [2,3,4,5],[4,5,6,7],[6,7,8,9]  }

        # count_blocks = 0
        # for i in range(1,n+1):
        #     print( sorted(list(reservedSeats  )))
        #     cnt_free = set()
        #     for j in range(2,10):
        #         if (i,j) in reservedSeats:
        #             cnt_free = []
        #         else:
        #             cnt_free.add(i)
                
        #         if cnt_free == 4:
        #             count_blocks += 1
        #             cnt_free = 0
        #         print((i,j),(i,j) in reservedSeats,cnt_free,count_blocks )

        # return count_blocks


# ---------------------------------------------------------
        # Create a dictionary of sets to store the reserved seats by row
        seats = collections.defaultdict(set)
        # Iterate through the reserved seats
        for i,j in reservedSeats:
            # If the seat is an outside seat in the row, add it to tallies 0 and 1
            if j in {4,5}: 
                seats[i].add(0) 
                seats[i].add(1)
            # If the seat is a middle seat in the row, add it to tallies 1 and 2
            elif j in {6,7}: 
                seats[i].add(1)
                seats[i].add(2)
            # If the seat is another type of seat, add it to the corresponding tally
            elif j in {8,9}: 
                seats[i].add(2)
            elif j in {2,3}:
                seats[i].add(0)
            # Initialize the result to twice the number of rows
            res = 2*n
            # Iterate through the rows of seats
        for i in seats:
            # If a row has all three tallies, subtract two from the result
            if len(seats[i]) == 3: res -= 2
            # Otherwise, subtract one from the result
            else: res -= 1

        # Return the final result
        return res
