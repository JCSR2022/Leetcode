class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        # op_val = {"++X":1,"X++":1,"--X":-1,"X--":-1}
        # x = 0
        # for op in operations:
        #     x += op_val[op]
        # return x
#-----------------------------------------------

        #this is faster!!!!??? with 2 if?

        ans = 0
        for o in operations:
            if '+' in o:
                ans = ans + 1
            elif '-' in o:
                ans = ans - 1
        return ans