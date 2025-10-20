class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        op_val = {"++X":1,"X++":1,"--X":-1,"X--":-1}
        x = 0
        for op in operations:
            x += op_val[op]
        return x