class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        
        l = 0
        window = 0
        max_window = 0
        statisfied = 0
        for r in range(len(customers)):
            if grumpy[r]:
                window += customers[r]
            else:
                statisfied += customers[r]
                
            if r - l + 1 > minutes:
                if grumpy[l]:
                    window -= customers[l]
                l += 1
            max_window = max(max_window,window)
            
        return statisfied+max_window
                
        
        
        
#         SumSatCus = sum(c for c, g in zip(customers, grumpy) if g == 0)
#         UnSatCus = [c if g == 1 else 0 for c, g in zip(customers, grumpy)]

#         #print(SumSatCus,UnSatCus)
#         SumUnSatCus = 0
#         for i in range(len(UnSatCus)):
#             #print(UnSatCus[i:i+minutes], sum(UnSatCus[i:i+minutes]))
#             SumUnSatCus = max(SumUnSatCus,sum(UnSatCus[i:i+minutes]))
#         return SumUnSatCus + SumSatCus